## About the Data

The data used in this project is synthetic data generated (by ChatGPT) to mimic a personal job application tracker. It captures job applications submitted across various Philippine tech hubs, local hiring platforms, and common tech job roles.

- **Source File**: `data/job_applications.csv`
- **Target Bronze Table**: `bronze_job_applications`
- **Total Records**: 80 rows
- **Total Attributes**: 14 columns
- **Currency**: Philippine Peso (PHP)
- **Primary Geographies**: Manila, Quezon City, Taguig, Pasig, Makati, Cebu City

> *The dataset contains bad data quality on purpose to mimic a real-life dataset for practice.*

---

## Data Dictionary

| Column Name | Data Type | Null Count | Null % | Description & Sample Values |
| :--- | :--- | :--- | :--- | :--- |
| `application_id` | `INTEGER` | 0 | 0.00% | Unique record identifier for each job application. Sample: `1`, `2`, `3` |
| `applicant_name` | `TEXT` | 0 | 0.00% | Full name of the applicant. Represents the candidate entity across multiple submissions. Sample: `Jamie Santos`, `Cameron Dela Cruz` |
| `email` | `TEXT` | 0 | 0.00% | Applicant email address. Sample: `jamie.santos@example.com` |
| `company` | `TEXT` | 0 | 0.00% | Name of the prospective employer. Raw data includes inconsistent casing and whitespace. Sample: `FoodHub PH`, `BRIGHTBANK`, `DataBridge Analytics ` |
| `industry` | `TEXT` | 0 | 0.00% | Industry sector of the hiring organization. Sample: `Technology`, `Finance`, `E-commerce`, `Healthcare`, `Construction` |
| `job_title` | `TEXT` | 0 | 0.00% | Job position applied for. Raw data contains mixed casing. Sample: `Backend Developer`, `full stack developer`, `Data Analyst` |
| `location` | `TEXT` | 0 | 0.00% | Office or job location city. Raw data contains mixed casing and trailing spaces. Sample: `Manila`, `quezon city`, `Taguig ` |
| `source` | `TEXT` | 0 | 0.00% | Channel or platform through which the application was submitted. Sample: `LinkedIn`, `JobStreet`, `KALIBRR`, `Referral`, `Company Website` |
| `application_date` | `TEXT (Date: DD/MM/YYYY)` | 3 | 3.75% | Date the application was submitted in `DD/MM/YYYY` text format. Sample: `13/07/2026` |
| `stage` | `TEXT` | 0 | 0.00% | Current status in the hiring pipeline. Sample: `Applied`, `Screening`, `Technical Interview`, `Final Interview`, `Offer`, `Rejected`, `Withdrawn` |
| `salary_expected` | `NUMERIC` | 5 | 6.25% | Candidate expected monthly compensation in PHP (range: 30,000 to 80,000). Sample: `45000`, `80000` |
| `recruiter` | `TEXT` | 6 | 7.50% | Assigned recruiter or hiring contact name. Sample: `Ana Santos`, `Nina Tan`, `Ken Flores` |
| `interview_date` | `TEXT (Date: DD/MM/YYYY)` | 37 | 46.25% | Scheduled interview date in `DD/MM/YYYY` text format. Populated primarily when an interview stage is reached. Sample: `18/03/2026` |
| `notes` | `TEXT` | 9 | 11.25% | Candidate notes, action items, or status remarks. Sample: `Follow up next week`, `Need to prepare SQL`, `Salary discussion pending` |

---

## Data Characteristics & Ingestion Notes (Bronze Layer)

As a raw ingestion layer (Bronze), the data is loaded as-is without destructive transformations:

1. **Raw Ingestion Fidelity**: Data types for dates (`application_date`, `interview_date`) are initially loaded as raw strings (`TEXT`), preserving original representations for auditing before casting in the Silver layer.
2. **Text Standardization Needed**: Several categorical text columns contain leading/trailing whitespaces (for example, `Taguig `, `LogiFast `) and uppercase variations (such as `BRIGHTBANK`, `BUILDRIGHT`, `JOBSTREET`, `REFERRAL`).
3. **Null Handling Context**:
   - `interview_date` (46.25% null): Expected domain behavior because applications at `Applied`, `Rejected`, or `Withdrawn` stages may never have scheduled interviews.
   - `salary_expected` (6.25% null): Undisclosed or unstated compensation expectations.
   - `recruiter` (7.50% null): Unassigned or unknown recruiter at submission time.
   - `application_date` (3.75% null): Missing user input during tracking.
4. **Relational Normalization Target**: Candidate information (`applicant_name`, `email`) is repeated across multiple applications. In the Silver layer, this flat structure is normalized into Third Normal Form (3NF) entities: `applicants` and `applications`. 