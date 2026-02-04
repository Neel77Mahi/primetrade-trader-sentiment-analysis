
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Page Config
st.set_page_config(page_title="Trader Sentiment Dashboard", layout="wide")

st.title("📊 Trader Performance vs Market Sentiment Dashboard")

st.markdown("""
This dashboard explores how Bitcoin market sentiment (Fear/Greed Index) impacts trader behavior and performance on Hyperliquid.
""")

# Upload merged dataset (export from notebook)
uploaded_file = st.file_uploader("Upload merged dataset CSV", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.success("Dataset Loaded Successfully!")

    # Sidebar Filters
    st.sidebar.header("Filters")

    sentiment_filter = st.sidebar.selectbox(
        "Select Market Sentiment",
        options=["All", "Fear", "Greed"]
    )

    if sentiment_filter != "All":
        df = df[df["sentiment_group"] == sentiment_filter]

    # ============================
    # KPI Metrics
    # ============================

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Total Trades", len(df))

    with col2:
        win_rate = (df["win"].mean()) * 100
        st.metric("Win Rate (%)", round(win_rate, 2))

    with col3:
        avg_size = df["Size USD"].mean()
        st.metric("Avg Position Size (USD)", round(avg_size, 2))

    st.divider()

    # ============================
    # PnL Distribution
    # ============================

    st.subheader("PnL Distribution")

    fig1, ax1 = plt.subplots()
    sns.boxplot(x="sentiment_group", y="Closed PnL", data=df, ax=ax1)
    st.pyplot(fig1)

    # ============================
    # Trade Frequency
    # ============================

    st.subheader("Average Trades Per Day")

    trades_per_day = df.groupby(["date","sentiment_group"]).size().reset_index(name="count")
    avg_trades = trades_per_day.groupby("sentiment_group")["count"].mean()

    fig2, ax2 = plt.subplots()
    avg_trades.plot(kind="bar", ax=ax2)
    st.pyplot(fig2)

    # ============================
    # Long vs Short Bias
    # ============================

    st.subheader("Long vs Short Positioning")

    df["position_type"] = df["Direction"].apply(
        lambda x: "Long" if "Long" in x else ("Short" if "Short" in x else "Other")
    )

    pos_dist = df.groupby(["sentiment_group","position_type"]).size().unstack()
    pos_pct = pos_dist.div(pos_dist.sum(axis=1), axis=0) * 100

    fig3, ax3 = plt.subplots()
    pos_pct[["Long","Short"]].plot(kind="bar", stacked=True, ax=ax3)
    st.pyplot(fig3)

else:
    st.warning("Please upload the merged dataset CSV file to begin.")
