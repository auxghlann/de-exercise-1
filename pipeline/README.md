# Data Pipeline

The data pipeline implementation structured according to the Medallion Architecture pattern: 
   - **Bronze** (raw ingestion)
   - **Silver** (cleaned and normalized), 
   - **Gold** (aggregated analytical views).

---

## Architecture Overview

```mermaid
flowchart LR
    CSV["job_applications.csv\n(Raw File)"] --> Bronze["Bronze Layer\n(bronze_job_applications)"]
    Bronze --> Silver["Silver Layer\n(applicants, applications)"]
    Silver --> Gold["Gold Layer\n(Reporting Marts / Views)"]
```
