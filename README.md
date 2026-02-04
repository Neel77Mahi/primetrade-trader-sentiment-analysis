# Trader Performance vs Market Sentiment Analysis

## Project Summary

This project analyzes the relationship between Bitcoin market sentiment (Fear/Greed Index) and trader behavior on Hyperliquid to understand how sentiment regimes influence trading performance, risk exposure, and behavioral patterns.

Key findings reveal that market sentiment significantly impacts trader activity and outcomes. Fear periods trigger aggressive trading behavior characterized by higher trade frequency and larger position sizes, while Greed periods exhibit improved win rates and more balanced long-short participation. Infrequent traders consistently outperform frequent traders, and high exposure trades generate substantially higher profitability across both sentiment regimes.

In addition to behavioral analysis, a Random Forest classification model was developed to predict trade profitability using sentiment and behavioral features, achieving strong predictive performance as an exploratory benchmark. Furthermore, unsupervised clustering was applied to identify distinct trader archetypes, including high-risk high-reward traders, balanced retail traders, and high-frequency scalpers.

Overall, this analysis provides data-driven insights and actionable strategy recommendations that adapt trading behavior and risk exposure based on prevailing market sentiment conditions.

--------------------------------------------------

OBJECTIVE

- Analyze trader performance differences across Fear and Greed market regimes  
- Study behavioral changes such as trade frequency, position sizing, and directional bias  
- Segment traders based on activity and exposure  
- Build optional predictive and clustering models for deeper insights  

--------------------------------------------------

DATASETS USED

1. Bitcoin Fear/Greed Index Dataset  
2. Hyperliquid Historical Trading Dataset  

--------------------------------------------------

KEY ANALYSIS PERFORMED

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

--------------------------------------------------

BONUS ANALYSIS

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

HOW TO RUN THE PROJECT

1. Install dependencies:

pip install pandas numpy matplotlib seaborn scikit-learn

2. Open the notebook:

Primetrade_Trader_Sentiment_Analysis.ipynb

3. Run all cells sequentially.

--------------------------------------------------

OUTPUT FILES

All important charts and visualizations are stored inside:

outputs/charts/

--------------------------------------------------

AUTHOR

Neeladri Bandopadhyay  
Data Science Internship Assignment Submission

