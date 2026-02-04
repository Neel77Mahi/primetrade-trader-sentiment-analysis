# Trader Performance vs Market Sentiment Analysis

## Project Summary

This project analyzes the relationship between Bitcoin market sentiment (Fear/Greed Index) and trader behavior on Hyperliquid to understand how sentiment regimes influence trading performance, risk exposure, and behavioral patterns.

Key findings reveal that market sentiment significantly impacts trader activity and outcomes. Fear periods trigger aggressive trading behavior characterized by higher trade frequency and larger position sizes, while Greed periods exhibit improved win rates and more balanced long-short participation. Infrequent traders consistently outperform frequent traders, and high exposure trades generate substantially higher profitability across both sentiment regimes.

In addition to behavioral analysis, a Random Forest classification model was developed to predict trade profitability using sentiment and behavioral features, achieving strong predictive performance as an exploratory benchmark. Furthermore, unsupervised clustering was applied to identify distinct trader archetypes, including high-risk high-reward traders, balanced retail traders, and high-frequency scalpers.

Overall, this analysis provides data-driven insights and actionable strategy recommendations that adapt trading behavior and risk exposure based on prevailing market sentiment conditions.

--------------------------------------------------

## OBJECTIVE

- Analyze trader performance differences across Fear and Greed market regimes  
- Study behavioral changes such as trade frequency, position sizing, and directional bias  
- Segment traders based on activity and exposure  
- Build optional predictive and clustering models for deeper insights  

--------------------------------------------------

## DATASETS USED

1. Bitcoin Fear/Greed Index Dataset  
2. Hyperliquid Historical Trading Dataset  

--------------------------------------------------

## KEY ANALYSIS PERFORMED

DATA PREPARATION  
- Timestamp conversion and daily alignment  
- Sentiment normalization (Fear vs Greed)  
- Removal of Neutral sentiment days  
- Dataset merging at daily granularity  

PERFORMANCE INSIGHTS  
- Greed sentiment periods show higher average win rates  
- Fear periods exhibit significantly higher trading activity  
- High exposure trades generate substantially higher profitability  

BEHAVIORAL INSIGHTS  
- Fear markets trigger aggressive trading and larger position sizes  
- Greed markets show balanced long and short positioning  
- Infrequent traders outperform frequent traders across both sentiment regimes  

PREDICTIVE MODELING  
A Random Forest classifier was trained to predict trade profitability using sentiment and behavioral features.  
The model achieved approximately 92 percent accuracy as an exploratory benchmark.  
The model is intended for analytical insight rather than production deployment due to potential feature correlation effects.

TRADER CLUSTERING  
Three behavioral trader archetypes were identified using KMeans clustering:

1. High-Risk High-Reward Traders  
2. Balanced Retail Traders  
3. High-Frequency Scalpers  

--------------------------------------------------

KEY INSIGHTS SUMMARY

- Greed sentiment periods show higher average win rates (~42%) compared to Fear periods (~41%).

- Trading activity increases significantly during Fear markets, with more than 2.5x higher daily trade volume.

- Average position size is substantially higher during Fear sentiment (~$7,182) compared to Greed (~$4,574), indicating aggressive risk exposure.

- Infrequent traders consistently outperform frequent traders across both market conditions, highlighting the negative impact of overtrading.

- High exposure trades generate significantly higher profitability, especially during volatile Fear periods.

- Long bias dominates during Fear markets, while Greed periods show increased short participation and two-sided trading behavior.

- Clustering analysis identified three trader archetypes: High-Risk High-Reward Traders, Balanced Retail Traders, and High-Frequency Scalpers.

--------------------------------------------------

## HOW TO RUN THE PROJECT

1. Install dependencies:
```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```
2. Open the notebook:
```bash
Primetrade_Trader_Sentiment_Analysis.ipynb
```
3. Run all cells sequentially.

--------------------------------------------------

## STREAMLIT DASHBOARD

A lightweight interactive dashboard was built using Streamlit to visualize trader performance and behavioral patterns across market sentiment regimes.

Dashboard Features:
- Sentiment filter (Fear / Greed)
- Win rate and trade volume KPIs
- PnL distribution visualization
- Trade frequency comparison
- Long vs Short positioning analysis

How to Run Locally:

1. Install dependencies:
```bash
pip install -r requirements.txt
```
2. Run dashboard:
```bash
python -m streamlit run app.py
```
3. Upload merged dataset CSV exported from notebook.

--------------------------------------------------

## Dashboard Preview:
![Dashboard Preview](outputs/charts/dashboard_preview.png)

--------------------------------------------------

## OUTPUT FILES

All important charts and visualizations are stored inside:

outputs/charts/

--------------------------------------------------

## AUTHOR

Neeladri Bandopadhyay  
Data Science Internship Assignment Submission








