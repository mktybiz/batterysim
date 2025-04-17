import streamlit as st
import matplotlib.pyplot as plt
import japanize_matplotlib  # 日本語表示用

def simulate_battery(battery_drain_per_day, driving_days_interval, driving_hours_per_day, charging_rate_per_hour=10):
    days = 90
    battery = 100
    battery_history = []

    for day in range(1, days + 1):
        if (day - 1) % driving_days_interval == 0:
            battery += driving_hours_per_day * charging_rate_per_hour
        else:
            battery -= battery_drain_per_day

        battery = max(0, min(100, battery))
        battery_history.append(battery)

    return battery_history

# Streamlit UI
st.title("📱 スマホバッテリーシミュレーター（3ヶ月間）")

battery_drain_per_day = st.slider("1日あたりのバッテリー消費量（%）", 0, 30, 5)
driving_days_interval = st.slider("運転する間隔（日）", 1, 14, 2)
driving_hours_per_day = st.slider("運転する時間（時間/日）", 0.0, 10.0, 2.0, step=0.25)  # ← 15分単位に変更
charging_rate_per_hour = st.slider("充電レート（%/時）", 1, 30, 10)

if st.button("シミュレーション実行"):
    battery_history = simulate_battery(
        battery_drain_per_day,
        driving_days_interval,
        driving_hours_per_day,
        charging_rate_per_hour
    )

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(range(1, 91), battery_history, label="バッテリー残量")
    ax.set_title("スマホのバッテリー残量（90日間）")
    ax.set_xlabel("日数")
    ax.set_ylabel("バッテリー（%）")
    ax.set_ylim(0, 100)
    ax.grid(True)
    ax.legend()
    st.pyplot(fig)
