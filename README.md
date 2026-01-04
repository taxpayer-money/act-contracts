# Australian Government Contracts - Open Data

**Comprehensive datasets and insights on Australian Federal and ACT Government contracts 2025**

This repository contains publicly available contract data from AusTender (Federal) and the ACT Government Tenders Portal, along with detailed narrative analysis revealing spending patterns, supplier concentration, and procurement transparency.

**🌐 Live Site**: [https://taxpayer-money.github.io/australian-government-contracts/](https://taxpayer-money.github.io/australian-government-contracts/)

**Total Public Data**: $99.33 billion across 66,226 contracts

---

## 📊 Datasets Overview

### Federal Government Contracts (AusTender 2025)
- **Total Contracts**: 64,930
- **Total Value**: $97.69 billion
- **Data Coverage**: All federal agencies
- **File**: [`data/austender_2025_contracts.csv`](data/austender_2025_contracts.csv)

**Key Statistics**:
- **Unique Suppliers**: 21,789
- **Largest Contract**: $3.69B (Spotless Facility Services)
- **Median Contract**: $63,695
- **Average Contract**: $1.50M
- **Top Agency**: Department of Defence ($49.09B, 50%)

### ACT Government Contracts (2025)
- **Total Contracts**: 1,296
- **Total Value**: $1.64 billion
- **Data Coverage**: All ACT directorates
- **File**: [`data/act_contracts_2025.csv`](data/act_contracts_2025.csv)

**Key Statistics**:
- **Unique Suppliers**: 772
- **Largest Contract**: $420M (SG Fleet - fleet management)
- **Median Contract**: $66,900
- **Average Contract**: $1.26M
- **Top Directorate**: Health ($400M, 24%)

---

## 📈 Key Insights

### Federal Government (AusTender)

**Procurement Transparency**:
- 57.7% of contracts are limited tenders (restricted competition)
- Open tenders account for 62.6% of value ($61.15B)
- Defence drives down transparency: civilian agencies 79.4% open tender

**Supplier Concentration**:
- Top 10 suppliers control $22.94B (23.5% of total)
- Top 100 suppliers control $60.54B (62.0% of total)
- 21,789 suppliers compete, but market highly concentrated

**Employment Services Industry** ($12.0B, 12.3% of federal spending):
- Top 5 providers: Serendipity ($1.40B), Atwork ($1.19B), Sureway ($0.91B)
- 30 mega-contracts control 60% of employment services value
- Department of Social Services: $11.89B (99% of employment spending)

**Geographic Distribution**:
- NSW: $34.06B (34.9%) - Sydney dominates
- VIC: $23.73B (24.3%) - Melbourne second
- ACT: $12.84B (13.1%) - Canberra proximity benefit

### ACT Government

**Key Findings**:
- Top 2 suppliers control 43% of 2025 market with just 2 contracts
- October 2025 saw $604M in contracts - 10x quiet months
- Multi-year contracts average 13.9x more valuable than single-year
- 826 contracts (63.7%) under $200K - accessible to SMEs

**[Read Full ACT Report →](https://taxpayer-money.github.io/australian-government-contracts/act-report.html)**

**[Read Full Federal Report →](https://taxpayer-money.github.io/australian-government-contracts/federal-report.html)**

---

## 📁 Data Schema

### Federal Dataset (austender_2025_contracts.csv)

| Field | Description |
|-------|-------------|
| `contract_id` | Contract notice number (e.g., CN4211286) |
| `ocid` | Open Contracting ID (OCDS standard) |
| `title` | Contract title |
| `description` | Detailed description |
| `supplier_name` | Supplier/contractor name |
| `supplier_abn` | Australian Business Number |
| `supplier_locality` | Supplier city |
| `supplier_region` | Supplier state/territory |
| `supplier_country` | Supplier country |
| `amount` | Contract value (AUD) |
| `currency` | Currency (AUD) |
| `date_signed` | Contract signing date |
| `date_start` | Contract start date |
| `date_end` | Contract end date |
| `duration_days` | Contract duration in days |
| `procuring_entity` | Federal agency/department |
| `procurement_method` | open/limited/selective |
| `procurement_details` | Procurement method details |
| `unspsc_code` | UN Standard Products/Services Code |
| `status` | Contract status |
| `award_date` | Award date |

### ACT Dataset (act_contracts_2025.csv)

| Field | Description |
|-------|-------------|
| `contract_number` | Unique contract identifier |
| `procurement_unique_id` | Procurement ID |
| `title` | Contract title/description |
| `directorate` | ACT Government directorate |
| `contract_type` | Type (Contract, Panel, etc.) |
| `slj_initiative` | Social/Local Jobs initiative (Yes/No) |
| `status` | Contract status |
| `execution_date` | Contract start date |
| `expiry_date` | Contract end date |
| `amount` | Contract value (AUD) |
| `suppliers` | Winning supplier(s) |
| `details_url` | Link to full contract details |
| `has_attachments` | Whether contract has attachments |

---

## 🎯 Use Cases

### For Suppliers
- Identify opportunity zones by contract size
- Analyze competitor success rates
- Track directorate spending patterns
- Find optimal contract value ranges

### For Researchers
- Government procurement analysis
- Market concentration studies
- Temporal spending patterns
- Supplier diversity research

### For Journalists
- Investigate large contracts and mega-deals
- Track spending anomalies and concentration
- Analyze supplier relationships and oligopolies
- Monitor procurement transparency (open vs limited tenders)
- Compare federal vs state spending patterns
- Employment services industry investigation

### For Policy Makers
- Benchmark procurement practices
- Assess SME participation
- Evaluate spending efficiency
- Track multi-year contract trends

---

## 📜 Data Sources

**Federal Contracts**: [AusTender OCDS API](https://api.tenders.gov.au/)
- Open Contracting Data Standard (OCDS) format
- All federal government agencies
- Updated: January 2026

**ACT Contracts**: [ACT Government Tenders Portal](https://www.tenders.act.gov.au/contract/search)
- All ACT Government directorates
- Updated: January 2026

All data is publicly available and was collected in accordance with the respective portals' terms of use.

---

## 📄 License

This dataset is provided under the **Creative Commons Zero (CC0)** license - free to use for any purpose without attribution.

See [LICENSE](LICENSE) for details.

---

## 🤝 Contributing

Found an issue with the data? Have suggestions for additional analysis?

- **Report Issues**: [GitHub Issues](https://github.com/taxpayer-money/australian-government-contracts/issues)
- **Data Corrections**: Please include contract ID and source for verification
- **Analysis Suggestions**: Open an issue with your proposed analysis

---

## ⚠️ Disclaimer

This is an independent analysis of publicly available data. It is not affiliated with or endorsed by any Australian government agency.

Data accuracy depends on the source portals. While we strive for accuracy, please verify critical information with official sources.

**Contract Verification**: Any contract can be verified on the official portals:
- Federal: [AusTender](https://www.tenders.gov.au/) (search by contract ID)
- ACT: [ACT Tenders Portal](https://www.tenders.act.gov.au/contract/search)

---

**Built with ❤️ for transparency in government procurement**
