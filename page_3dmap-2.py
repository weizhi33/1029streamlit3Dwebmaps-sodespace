import streamlit as st
import plotly.express as px
import pandas as pd
st.title("Plotly 3D W (Uß - Q)")
# --- 1. / Plotly wöÏ ---
df = px.data.gapminder().query("year == 2007")
# --- 2.  3D vW (scatter_geo) ---
fig = px.scatter_geo(
df,
locations="iso_alpha", # _ïü
color="continent", # wN
hover_name="country", # _]
size="pop", # ö//ï?
# *** :o "orthographic" Ï 3D 
Q ***
projection="orthographic"
)
# --- 3.  Streamlit o ---
st.plotly_chart(fig, use_container_width=True)
