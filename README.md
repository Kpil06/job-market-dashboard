# Job Market Dashboard

An interactive Streamlit dashboard visualising Irish data job market listings, built on top of the database from jobm-market-sql. Third project in a portfolio series.

## What it does 

- Reads job listings data from a SQLite database (built in job-market-sql)
- Displays key metrics: total listings, unique companies, percentage missing salary info
- Shows a bar chart of job count by category
- Shows a bar chart of top hiring companies
- Proivides a filerable, browseable table of all listings by category 

## Tech stack 

Python, Streamlit, pandas, Plotly, SQLite 

## Setup 

1. Clone this repo and create a virtual environment:
    python3 -m venv venv 
    source venv/bin/activate
    pip install -r requiremnets.txt

2. Run the app:
    streamlit run app.py

3. It will open automatically in your browser at localhost:8501

## Data notes 

- jobs.db is commited directly to this repo(unlike the job-market-sql project) so the dashboard works immediately after cloning, without needing to rebuild the database from a CSV first.
- One listings company field contains "Design Full-time" instead of an actual company name - a parsing arteact from the original source data (Jooble). It is left as-is to keep the dashboard as an honest reflection of the data.

## Some possible nect steps

- Deploy live via Streamlit Community Cloud for a shareable link
- Add a chart showing listings over time as the dataset grows
- Add search/filter by company, not just category 


