import sqlite3 
import pandas as pd 
import streamlit as st 
import plotly.express as px 

DB_PATH = "jobs.db"

@st.cache_data 
def load_data():
    """
    Load the jobs table into a DataFrame. Cached so teh app doesn't re-read the database on eevery interaction.
    """

    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query("SELECt * FROM jobs", conn)
    conn.close()
    return df 

def main():
    st.set_page_config(page_title="Irish Data Jobs Market", layout="wide")
    st.title("Irish Data Job Market Dashboard")
    st.caption(
        "Live view of job listings collected via a Python & SQLite pipeline."
        "Part of a portfolio series (job-market-tracker and job-market-sql)."
    )

    df = load_data()

    # --- Top level stats --- 
    col1, col2, col3 = st.columns(3)
    col1.metric("Total listings", len(df))
    col2.metric("Unique companies", df["company"].nunique())
    missing_salary_pct = round(
        100 * df["salary"].isna().sum() / len(df), 1
    )
    col3.metric("Missing salary info", f"{missing_salary_pct}%")

    st.divider()

    # -- Category Breakdown
    st.subheader("Job count by category")
    category_counts = df["category"].value_counts().reset_index()
    category_counts.columns = ["category", "count"]
    fig1 = px.bar(category_counts, x="category", y="count")
    st.plotly_chart(fig1, use_container_width=True)


    # -- Top companies --
    st.subheader("Top hiring companies")
    top_companies = df["company"].value_counts().head(10).reset_index()
    top_companies.columns = ["company", "count"]
    fig2 = px.bar(top_companies, x="count", y="company", orientation="h")
    st.plotly_chart(fig2, use_container_width=True)
    
    st.divider()

    # -- Filterable table -- 
    st.subheader("Browse listings")
    categories = ["All"] + sorted(df["category"].dropna().unique().tolist())
    selected_category = st.selectbox("Filter by category", categories)

    filtered_df = df if selected_category == "All" else df[df["category"] == selected_category]
    st.dataframe(
        filtered_df[["title", "company", "category", "date_posted", "url"]],
        use_container_width=True
    )

if __name__ == "__main__":
    main()