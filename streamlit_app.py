import streamlit as st
from snowflake.snowpark.context import get_active_session

st.title("Customer Analytics Dashboard")

session = get_active_session()

query = """
SELECT CITY, SUM(SALES) AS TOTAL_SALES
FROM ANALYTICS_DB.DEV.CUSTOMERS
GROUP BY CITY
"""

df = session.sql(query).to_pandas()

st.dataframe(df)

st.bar_chart(df.set_index("CITY"))