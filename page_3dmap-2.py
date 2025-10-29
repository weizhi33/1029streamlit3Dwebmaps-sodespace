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

# --- 1. 讀取範例 DEM 資料 ---
# 將 Mt. Bruno 的資料連結替換為 Mount Hood (胡德山) 的資料連結
# 資料來源：Plotly 內建的 Mount Hood DEM 數據 (儲存為 CSV)
z_data = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/api_docs/mt_hood_elevation.csv")

# --- 2. 建立 3D Surface 圖 (其餘部分不變) ---
fig = go.Figure(
    data=[
        go.Surface(
            z=z_data.values,
            colorscale="Viridis"
        )
    ]
)

# --- 3. 調整 3D 視角和外觀 ---
# 同時修改標題以符合新的資料
fig.update_layout(
    title="**Mount Hood (胡德山) 3D 地形圖 (可旋轉)**", # 標題修改
    width=800,
    height=700,
    scene=dict(
        xaxis_title='經度 (X)',
        yaxis_title='緯度 (Y)',
        zaxis_title='海拔 (Z)'
    )
)

# --- 4. 在 Streamlit 中顯示 ---
st.plotly_chart(fig)