import streamlit as st
import plotly.express as px
import pandas as pd
st.title("Plotly 3D ")
# --- 1. / Plotly wöÏ ---
df = px.data.gapminder().query("year == 2007")
# --- 2.  3D  (scatter_geo) ---
fig = px.scatter_geo(
df,
locations="iso_alpha", # _
color="continent", # wN
hover_name="country", # 
size="pop", # ö//ï?
# *** : "orthographic" 
Q ***
projection="orthographic"
)
# --- 3. Streamlit o ---
st.plotly_chart(fig, use_container_width=True)
