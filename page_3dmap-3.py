import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import numpy as np # 用於處理網格數據

# ----------------------------------------------------
# 設定檔案與欄位名稱 (請根據您的實際 CSV 檔案調整！)
# ----------------------------------------------------
# 注意：Streamlit 在部署時會以專案根目錄為基準。
# 如果您的 DTM.csv 就在 app.py 旁邊，路徑會是 'DTM.csv'
# 如果 DTM.csv 在子資料夾 data/ 內，路徑是 'data/DTM.csv'
# 根據您的路徑 /workspaces/1029streamlit3Dwebmaps-sodespace/DTM.csv
# 在 codespace 專案根目錄下，通常就是 'DTM.csv'
DATA_FILE_PATH = 'DTM.csv' 

# 假設您的 CSV 檔案的欄位名稱 (請務必確認這三欄的名稱！)
# DTM 資料通常使用 TWD97 (平面座標)
X_COL_NAME = 'X' 
Y_COL_NAME = 'Y' 
Z_COL_NAME = 'Z' # 高程值

st.set_page_config(
    page_title="小琉球 DTM 3D 模型", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

@st.cache_data
def load_and_structure_dtm(file_path):
    """
    讀取 DTM CSV 數據，並將其轉換為 Plotly 繪圖所需的 Z 矩陣。
    這一步驟非常關鍵，將點雲數據轉換為規則的網格 (Grid)。
    """
    try:
        # 1. 讀取數據 (假設 CSV 沒有額外的 Index 欄位)
        df = pd.read_csv(file_path) 
        
        # 2. 篩選：移除缺失值 (若有)
        df = df.dropna(subset=[X_COL_NAME, Y_COL_NAME, Z_COL_NAME])
        
        # 3. 準備 X, Y 唯一值
        # 由於是規則網格，我們按順序取出 X, Y 的唯一座標
        unique_x = sorted(df[X_COL_NAME].unique())
        unique_y = sorted(df[Y_COL_NAME].unique())
        
        nx = len(unique_x)
        ny = len(unique_y)
        
        st.info(f"DTM 數據點數: {len(df)}