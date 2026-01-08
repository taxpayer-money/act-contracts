#!/usr/bin/env python3
"""
Federal Procurement Analysis - Generate Statistics for Report

This script analyzes the AusTender 2025 contracts dataset and generates
all statistics referenced in the federal-report.md file.

Data Source: AusTender OCDS API (https://api.tenders.gov.au)
Dataset: data/austender_2025_contracts.csv

All figures in the report are generated from this analysis.
"""

import csv
from collections import defaultdict
from datetime import datetime

print("=" * 80)
print("FEDERAL PROCUREMENT ANALYSIS - 2025 CONTRACTS")
print("=" * 80)
print(f"Analysis Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print("Data Source: AusTender OCDS API")
print("=" * 80)

contracts = []
print("\nLoading contracts from data/austender_2025_contracts.csv...")

with open('data/austender_2025_contracts.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        try:
            row['value'] = float(row['amount'])
            contracts.append(row)
        except (ValueError, KeyError):
            continue

print(f"Loaded {len(contracts):,} contracts")

print("\n" + "=" * 80)
print("1. BASIC STATISTICS")
print("=" * 80)

total_contracts = len(contracts)
total_value = sum(c['value'] for c in contracts)
unique_suppliers = len(set(c['supplier_name'] for c in contracts))

print(f"Total Contracts: {total_contracts:,}")
print(f"Total Value: ${total_value:,.2f}")
print(f"Total Value (Billions): ${total_value/1e9:.2f}B")
print(f"Unique Suppliers: {unique_suppliers:,}")
print(f"Average Contract Value: ${total_value/total_contracts:,.2f}")

print("\n" + "=" * 80)
print("2. MARKET CONCENTRATION - TOP SUPPLIERS")
print("=" * 80)

supplier_totals = defaultdict(lambda: {'value': 0, 'count': 0})
for c in contracts:
    supplier_totals[c['supplier_name']]['value'] += c['value']
    supplier_totals[c['supplier_name']]['count'] += 1

sorted_suppliers = sorted(supplier_totals.items(), key=lambda x: x[1]['value'], reverse=True)

top_20_value = sum(s[1]['value'] for s in sorted_suppliers[:20])
top_20_pct = (top_20_value / total_value) * 100

top_100_value = sum(s[1]['value'] for s in sorted_suppliers[:100])
top_100_pct = (top_100_value / total_value) * 100

print(f"\nTop 20 Suppliers:")
print(f"  Total Value: ${top_20_value:,.2f} (${top_20_value/1e9:.2f}B)")
print(f"  Percentage: {top_20_pct:.2f}%")
print(f"  Remaining {unique_suppliers - 20:,} suppliers: {100 - top_20_pct:.2f}%")

print(f"\nTop 100 Suppliers:")
print(f"  Total Value: ${top_100_value:,.2f} (${top_100_value/1e9:.2f}B)")
print(f"  Percentage: {top_100_pct:.2f}%")

print(f"\nTop 20 Suppliers by Value:")
for i, (supplier, data) in enumerate(sorted_suppliers[:20], 1):
    pct = (data['value'] / total_value) * 100
    print(f"{i:2d}. {supplier[:50]:<50} ${data['value']/1e9:>6.2f}B ({pct:>5.2f}%) - {data['count']:>5} contracts")

print("\n" + "=" * 80)
print("3. CONTRACT SIZE DISTRIBUTION")
print("=" * 80)

mega_contracts = [c for c in contracts if c['value'] >= 100_000_000]
large_contracts = [c for c in contracts if 10_000_000 <= c['value'] < 100_000_000]
medium_contracts = [c for c in contracts if 1_000_000 <= c['value'] < 10_000_000]
small_contracts = [c for c in contracts if c['value'] < 1_000_000]

mega_value = sum(c['value'] for c in mega_contracts)
large_value = sum(c['value'] for c in large_contracts)
medium_value = sum(c['value'] for c in medium_contracts)
small_value = sum(c['value'] for c in small_contracts)

print(f"\nMega-contracts (≥$100M):")
print(f"  Count: {len(mega_contracts):,} ({len(mega_contracts)/total_contracts*100:.1f}%)")
print(f"  Value: ${mega_value/1e9:.2f}B ({mega_value/total_value*100:.1f}%)")
print(f"  Average: ${mega_value/len(mega_contracts)/1e6:.1f}M")

print(f"\nLarge contracts ($10M-$100M):")
print(f"  Count: {len(large_contracts):,} ({len(large_contracts)/total_contracts*100:.1f}%)")
print(f"  Value: ${large_value/1e9:.2f}B ({large_value/total_value*100:.1f}%)")

print(f"\nMedium contracts ($1M-$10M):")
print(f"  Count: {len(medium_contracts):,} ({len(medium_contracts)/total_contracts*100:.1f}%)")
print(f"  Value: ${medium_value/1e9:.2f}B ({medium_value/total_value*100:.1f}%)")

print(f"\nSmall contracts (<$1M):")
print(f"  Count: {len(small_contracts):,} ({len(small_contracts)/total_contracts*100:.1f}%)")
print(f"  Value: ${small_value/1e9:.2f}B ({small_value/total_value*100:.1f}%)")
print(f"  Average: ${small_value/len(small_contracts):,.0f}")

print("\n" + "=" * 80)
print("4. SPOTLESS vs THALES COMPARISON")
print("=" * 80)

spotless_contracts = [c for c in contracts if 'SPOTLESS' in c['supplier_name'].upper()]
spotless_value = sum(c['value'] for c in spotless_contracts)
spotless_max = max(c['value'] for c in spotless_contracts) if spotless_contracts else 0

thales_main = [c for c in contracts if c['supplier_name'] == 'THALES AUSTRALIA']
thales_main_value = sum(c['value'] for c in thales_main)

print(f"\nSpotless Facility Services (all entities):")
print(f"  Contracts: {len(spotless_contracts)}")
print(f"  Total Value: ${spotless_value/1e9:.2f}B")
print(f"  Largest Contract: ${spotless_max/1e9:.2f}B")
print(f"  Market Share: {spotless_value/total_value*100:.2f}%")

print(f"\nThales Australia (main entity only):")
print(f"  Contracts: {len(thales_main)}")
print(f"  Total Value: ${thales_main_value/1e6:.2f}M")
print(f"  Average: ${thales_main_value/len(thales_main):,.0f}")
print(f"  Market Share: {thales_main_value/total_value*100:.2f}%")

print(f"\nComparison:")
print(f"  Spotless largest contract: ${spotless_max/1e9:.2f}B")
print(f"  Thales total (474 contracts): ${thales_main_value/1e6:.2f}M")
print(f"  Ratio: {spotless_max/thales_main_value:.1f}x")

print("\n" + "=" * 80)
print("5. DEPARTMENT OF DEFENCE")
print("=" * 80)

defence_contracts = [c for c in contracts if 'DEFENCE' in c['procuring_entity'].upper()]
defence_value = sum(c['value'] for c in defence_contracts)

print(f"\nDepartment of Defence:")
print(f"  Contracts: {len(defence_contracts):,}")
print(f"  Total Value: ${defence_value/1e9:.2f}B")
print(f"  Percentage of Total: {defence_value/total_value*100:.2f}%")
print(f"  Average Contract: ${defence_value/len(defence_contracts):,.0f}")

print("\n" + "=" * 80)
print("6. EMPLOYMENT SERVICES")
print("=" * 80)

social_services = [c for c in contracts if 'SOCIAL SERVICES' in c['procuring_entity'].upper()]
employment_workplace = [c for c in contracts if 'EMPLOYMENT' in c['procuring_entity'].upper() and 'WORKPLACE' in c['procuring_entity'].upper()]

social_value = sum(c['value'] for c in social_services)
employment_value = sum(c['value'] for c in employment_workplace)
combined_value = social_value + employment_value

print(f"\nDepartment of Social Services:")
print(f"  Contracts: {len(social_services):,}")
print(f"  Value: ${social_value/1e9:.2f}B")

print(f"\nDepartment of Employment and Workplace Relations:")
print(f"  Contracts: {len(employment_workplace):,}")
print(f"  Value: ${employment_value/1e9:.2f}B")

print(f"\nCombined Employment Services:")
print(f"  Total Value: ${combined_value/1e9:.2f}B")
print(f"  Percentage: {combined_value/total_value*100:.2f}%")

employment_suppliers = defaultdict(float)
for c in social_services + employment_workplace:
    employment_suppliers[c['supplier_name']] += c['value']

print(f"\nTop 10 Employment Services Suppliers:")
for i, (supplier, value) in enumerate(sorted(employment_suppliers.items(), key=lambda x: x[1], reverse=True)[:10], 1):
    print(f"{i:2d}. {supplier[:50]:<50} ${value/1e9:>5.2f}B")

print("\n" + "=" * 80)
print("7. PROCUREMENT METHODS")
print("=" * 80)

method_stats = defaultdict(lambda: {'count': 0, 'value': 0})
for c in contracts:
    method = c['procurement_method']
    method_stats[method]['count'] += 1
    method_stats[method]['value'] += c['value']

for method, data in sorted(method_stats.items(), key=lambda x: x[1]['value'], reverse=True):
    pct_count = (data['count'] / total_contracts) * 100
    pct_value = (data['value'] / total_value) * 100
    print(f"\n{method}:")
    print(f"  Contracts: {data['count']:,} ({pct_count:.1f}%)")
    print(f"  Value: ${data['value']/1e9:.2f}B ({pct_value:.1f}%)")

print("\n" + "=" * 80)
print("8. GEOGRAPHIC DISTRIBUTION")
print("=" * 80)

geo_stats = defaultdict(lambda: {'count': 0, 'value': 0})
for c in contracts:
    state = c.get('supplier_region', 'UNKNOWN')
    geo_stats[state]['count'] += 1
    geo_stats[state]['value'] += c['value']

print(f"\nTop 10 States/Territories by Value:")
for i, (state, data) in enumerate(sorted(geo_stats.items(), key=lambda x: x[1]['value'], reverse=True)[:10], 1):
    pct = (data['value'] / total_value) * 100
    print(f"{i:2d}. {state:<30} ${data['value']/1e9:>6.2f}B ({pct:>5.1f}%) - {data['count']:>6,} contracts")

print("\n" + "=" * 80)
print("ANALYSIS COMPLETE")
print("=" * 80)
print("\nAll statistics in federal-report.md are derived from this analysis.")
print("Data source: data/austender_2025_contracts.csv")
print("Raw data available at: https://github.com/taxpayer-money/australian-government-contracts")
print("=" * 80)
