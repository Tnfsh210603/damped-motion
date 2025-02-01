#引入函式庫
import math
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st


# Streamlit 標題
st.header("科展")  # 顯示整個頁面的主標題，說明研究主題


# Streamlit 敘述
st.subheader("阻尼震盪軌跡預測")  # 顯示子標題，介紹第一部分的內容
st.text("不考慮震幅過大導致物體與銅板產生碰撞的情況。")  # 提供額外說明，避免誤解模擬範圍


# 使用者輸入
mass = st.slider('質量 (kg)', min_value=0.1, max_value=0.25, value=0.1, step=0.01)  # 透過滑桿讓使用者選擇物體的質量
amplitude = st.slider('原始震幅 (m)', min_value=0.005, max_value=0.1, value=0.005, step=0.001, format="%.3f")  # 透過滑桿設定初始震幅
height = st.slider('高度 (m)', min_value=0.01, max_value=0.08, value=0.01, step=0.01)  # 透過滑桿選擇物體與銅板的初始距離
spring_constant = st.slider('彈力常數 (N/m)', min_value=10, max_value=20, value=10, step=1)  # 設定彈簧的彈力常數


# 定義周期與阻尼系數
T = (2 * math.pi * (mass / spring_constant) ** 0.5)  # 根據質量和彈簧常數計算系統的振盪周期
k = 0.000026386269  # 固定比例常數，用於計算阻尼係數
thickness = 5  # 固定的銅板厚度值
b = k * (height ** -3) * (mass ** -0.75) * (0.1348-0.1308*(np.e ** (-0.107*thickness)))  # 計算阻尼係數，考慮高度、質量與厚度


# 圖表生成
fig1, ax1 = plt.subplots(figsize=(8, 5))  # 初始化第一個圖表，設置大小
ax1.set_title('Y-T Plot')  # 設置圖表標題，表示位移隨時間變化
ax1.set_xlabel('Time(s)')  # 設置橫軸標籤
ax1.set_ylabel('Displacement (m)')  # 設置縱軸標籤
ax1.grid(True)  # 顯示網格線


# 計算位移
time_values = np.linspace(0, 15, 1500)  # 時間點範圍，模擬15秒的運動
# 根據位移公式計算位移值
displacement_values = amplitude * np.exp(-b * time_values) * np.cos(2 * np.pi * time_values / T)
ax1.plot(time_values, displacement_values, label="Displacement")  # 在圖表中繪製位移曲線，並設置標籤
ax1.legend()  # 添加圖例


# 展示圖表
st.pyplot(fig1)  # 使用 Streamlit 在網頁上顯示第一個圖表
