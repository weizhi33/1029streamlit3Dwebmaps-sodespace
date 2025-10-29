import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd


st.title("Plotly 3D 地圖 (向量 - 地球儀)")

# --- 1. 載入 Plotly 內建的範例資料 ---
df = px.data.gapminder().query("year == 2007")
# px.data 提供了幾個內建的範例資料集，方便使用者練習或展示。
# gapminder() 是其中一個內建函式，它會載入著名的 Gapminder 資料集。
# 這個資料集包含了世界各國多年的平均壽命 (lifeExp)、人均 GDP (gdpPercap) 和人口 (pop) 等數據。
# .query("year == 2007")是 pandas DataFrame 提供的一個方法，用於根據字串表達式來篩選資料框的列 (rows)。
# "year == 2007" 是一個字串形式的查詢條件，意思是「選取 'year' 欄位的值等於 2007 的那些列」。

# --- 2. 建立 3D 地理散點圖 (scatter_geo) ---
fig = px.scatter_geo(
    df,
    locations="iso_alpha",  # 國家代碼
    color="continent",      # 依據大陸洲別上色
    hover_name="country",   # 滑鼠懸停時顯示國家名稱
    size="pop",             # 點的大小代表人口數

    # *** 關鍵：使用 "orthographic" 投影法來建立 3D 地球儀 ***
    projection="orthographic"
)
# "orthographic" 投影會將地球渲染成一個從太空中看到的球體，
# 從而產生類似 3D 地球儀的視覺效果。
# 其他常見投影如 "natural earth", "mercator" 等通常是 2D 平面地圖。


# --- 3. 在 Streamlit 中顯示 ---
st.plotly_chart(fig, use_container_width=True)
# use_container_width=True:當設定為 True 時，Streamlit 會忽略 Plotly 圖表物件本身可能設定的寬度，
# 並強制讓圖表的寬度自動延展，以填滿其所在的 Streamlit 容器 (例如，主頁面的寬度、某個欄位 (column) 的寬度，
# 或是一個展開器 (expander) 的寬度)。



st.title("Plotly 3D 地圖 (網格 - DEM 表面)")

# --- 1. 讀取範例 DEM 資料 (使用內建數據集) ---

# Plotly 內建的 "volcano" (火山) DEM 數據。
# px.data.volcano() 載入的是一個 Pandas DataFrame
# .values 會提取 DataFrame 底層的 NumPy 2D 陣列，每個格子的值就是海拔 (Z)
try:
    z_data = px.data.volcano().values
except Exception as e:
    # 如果載入內建數據也失敗 (極罕見)，則給出提示並使用一個模擬數據
    st.error(f"無法載入 Plotly 內建的 'volcano' 數據: {e}")
    # 創建一個簡單的模擬平面數據作為備用
    z_data = [[i*j for i in range(10)] for j in range(10)]


# --- 2. 建立 3D Surface 圖 ---
# 建立一個 Plotly 的 Figure 物件
fig = go.Figure(
    data=[
        # 建立一個 Surface (曲面) trace
        go.Surface(
            # 使用內建的 volcano 數據的 2D 陣列
            z=z_data, 

            # colorscale 參數指定用於根據 z 值 (高度) 對曲面進行著色的顏色映射方案。
            # 這裡使用 "Plasma" 顏色，視覺效果鮮明。
            colorscale="Plasma" 
        )
    ] 
)

# --- 3. 調整 3D 視角和外觀 ---
# 使用 update_layout 方法來修改圖表的整體佈局和外觀設定
fig.update_layout(
    # 設定圖表的標題文字，以匹配新的資料
    title="Plotly 內建 Volcano 3D 地形圖 (可旋轉)", 

    # 設定圖表的寬度和高度 (單位：像素)
    width=800,
    height=700,

    # scene 參數用於配置 3D 圖表的場景 (座標軸、攝影機視角等)
    scene=dict(
        # 設定 X, Y, Z 座標軸的標籤文字
        xaxis_title='X 網格索引',
        yaxis_title='Y 網格索引',
        zaxis_title='海拔/高度 (Z)'
        # 由於是內建的純粹數學網格，軸標籤可以更通用
    )
)

# --- 4. 在 Streamlit 中顯示 ---
st.plotly_chart(fig)