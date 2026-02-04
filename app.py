import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="Trader Sentiment Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- CUSTOM STYLE ---------------- #

st.markdown("""
<style>
section[data-testid="stSidebar"] {
    width: 260px !important;
}
.metric-card {
    background-color: #111827;
    padding: 15px;
    border-radius: 10px;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ---------------- #

st.title("Trader Performance vs Market Sentiment")
st.caption("Interactive analysis of Hyperliquid trader behavior across Fear and Greed market regimes")

st.divider()

# ---------------- FILE UPLOAD ---------------- #

uploaded_file = st.file_uploader(
    "Upload merged dataset (CSV)",
    type=["csv"]
)

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    # ---------------- SIDEBAR ---------------- #

    st.sidebar.header("Filters")

    sentiment_filter = st.sidebar.selectbox(
        "Market Sentiment",
        ["All", "Fear", "Greed"]
    )

    if sentiment_filter != "All":
        df = df[df["sentiment_group"] == sentiment_filter]

    # ---------------- KPIs ---------------- #

    st.subheader("Key Metrics")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Total Trades", f"{len(df):,}")

    with col2:
        win_rate = df["win"].mean() * 100
        st.metric("Win Rate", f"{win_rate:.2f}%")

    with col3:
        avg_size = df["Size USD"].mean()
        st.metric("Avg Position Size", f"${avg_size:,.0f}")

    with col4:
        avg_pnl = df["Closed PnL"].mean()
        st.metric("Avg Trade PnL", f"${avg_pnl:.2f}")

    st.divider()

    # ---------------- ROW 1 ---------------- #

    col_left, col_right = st.columns(2)

    with col_left:
        st.subheader("PnL Distribution")

        fig1, ax1 = plt.subplots(figsize=(5, 4))
        sns.boxplot(
            x="sentiment_group",
            y="Closed PnL",
            data=df,
            ax=ax1
        )
        ax1.set_xlabel("")
        st.pyplot(fig1, use_container_width=True)

    with col_right:
        st.subheader("Trade Frequency (Avg per Day)")

        trades_per_day = df.groupby(["date","sentiment_group"]).size().reset_index(name="count")
        avg_trades = trades_per_day.groupby("sentiment_group")["count"].mean()

        fig2, ax2 = plt.subplots(figsize=(5, 4))
        avg_trades.plot(kind="bar", ax=ax2)
        ax2.set_ylabel("Trades")
        ax2.set_xlabel("")
        st.pyplot(fig2, use_container_width=True)

    st.divider()

    # ---------------- ROW 2 ---------------- #

    st.subheader("Long vs Short Positioning")

    df["position_type"] = df["Direction"].apply(
        lambda x: "Long" if "Long" in x else ("Short" if "Short" in x else "Other")
    )

    pos_dist = df.groupby(["sentiment_group","position_type"]).size().unstack()
    pos_pct = pos_dist.div(pos_dist.sum(axis=1), axis=0) * 100

    fig3, ax3 = plt.subplots(figsize=(6, 4))
    pos_pct[["Long","Short"]].plot(kind="bar", stacked=True, ax=ax3)
    ax3.set_ylabel("Percentage")
    ax3.set_xlabel("")
    st.pyplot(fig3, use_container_width=True)

    st.success("Dashboard Loaded Successfully")

else:
    st.info("⬆ Upload the merged dataset CSV file to start the dashboard.")
