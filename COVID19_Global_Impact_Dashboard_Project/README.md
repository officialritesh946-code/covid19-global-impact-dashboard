# COVID-19 Global Impact Dashboard

## Project overview
This project analyzes a historical global COVID-19 dataset to identify trends in confirmed cases, deaths, recoveries and active cases. The work follows the internship brief and focuses on a clear, non-technical story supported by reproducible calculations.

**Analysis period:** 22 Jan 2020 to 27 Jul 2020  
**Final global confirmed cases:** 16,480,485  
**Final global deaths:** 654,036  
**Final global recoveries:** 9,468,087

## Business/analytics question
**How did the global COVID-19 case trajectory evolve, and which countries/regions accounted for the largest cumulative case burden by the end of the available period?**

## Deliverables
- `COVID19_Global_Impact_Dashboard.xlsx` — professional analysis workbook with daily analysis, country analysis, region summary, data-quality checks and data dictionary.
- `COVID19_Global_Impact_Dashboard.png` — dashboard visual for the project submission/LinkedIn post.
- `COVID19_Cleaned_Daily.csv` — cleaned daily dataset with 7-day rolling averages, case fatality rate and doubling-time metric.
- `COVID19_Cleaned_Country.csv` — country-level dataset with case fatality and recovery rates.
- `COVID19_Region_Summary.csv` — WHO-region aggregation.
- `Executive_Summary.pdf` — one-page executive summary.
- `analysis.py` — reproducible Python analysis script.
- `COVID19_Global_Impact_Dashboard.ipynb` — notebook structure for GitHub.
- `PROJECT_SUBMISSION_CHECKLIST.md` — submission checklist.

## Key findings
1. The dataset reaches **16,480,485 confirmed cases** and **654,036 deaths** by **27 Jul 2020**.
2. The highest single-day new-case value in the supplied daily table is **282,756 on 23 Jul 2020**.
3. The highest single-day new-death value is **9,966 on 23 Jul 2020**.
4. The highest 7-day rolling average of new cases is approximately **252,425** on **27 Jul 2020**.
5. At the final date, the **Americas** region accounts for **8,839,286 confirmed cases** in the country-level table.
6. The final global case fatality rate calculated from cumulative totals is **3.97%**.

## Data quality and assumptions
- The supplied archive contains six CSV files.
- `day_wise.csv` and `country_wise_latest.csv` reconcile on the final cumulative totals.
- The `Province/State` field has many missing values in the complete time-series file; this is treated as expected for country-level records rather than filled with invented values.
- The complete time-series contains negative numeric entries, which can reflect retrospective reporting corrections. They are **not silently converted to zero**.
- The supplied files do **not** contain vaccination variables. Therefore, this version does not fabricate a vaccination analysis. If vaccination rollout analysis is required, a vaccination dataset should be added as a documented source.
- The dataset is historical and should not be presented as current COVID-19 surveillance.

## Tools
Python, Pandas, Matplotlib, Excel. The workbook can also be used as a source for Power BI or Tableau.

## Reproducibility
Run `analysis.py` after placing the original CSV files in a `raw_data/` directory. The script recalculates the derived metrics and exports analysis-ready files.
