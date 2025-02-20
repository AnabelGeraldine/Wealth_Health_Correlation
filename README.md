# Wealth_Health_Correlation

## Objective
This project aims to explore the relationship between a country's wealth and various health and social indicators, specifically crude death rates, literacy rates, and suicide rates. The primary goal is to determine if economic factors, such as GDP and income levels, significantly influence public health and literacy outcomes. By analyzing these correlations, the study provides insights into potential policy implications and socio-economic trends.

## Methods and Tools Used
The analysis was conducted using Python with key libraries such as pandas, scikit-learn, and matplotlib for data cleaning, visualization, and predictive modeling. The dataset was prepared by removing null values, rescaling variables for comparability, and eliminating outliers that could distort the results. Various machine learning models were implemented to predict crude death rates, including:

- Linear Regression: Used to predict death crude rates based on income and literacy levels.
- K-Nearest Neighbors (KNN) Regression: Applied to model relationships between suicide rates, income levels, and crude death rates.
- Bayesian Linear Regression: Used to forecast future death crude rates based on historical data from 2010 and 2020.
Each model was evaluated using Root Mean Squared Error (RMSE) and R-squared scores to determine prediction accuracy.

## Findings and Conclusion
The results indicate that income levels have a stronger correlation with crude death rates than literacy rates, though the overall predictive power of the models was limited. The Linear Regression model had a relatively high RMSE and a low R-squared score, suggesting weak predictive accuracy due to possible overfitting. Similarly, the KNN model showed high variance and struggled to generalize, indicating that the variables might not have strong direct correlations. The Bayesian Linear Regression model performed moderately well, showing that higher crude death rates in 2010 correlated with higher rates in 2020, but also confirming an overall downward trend in death rates over time.

Key Takeaways
Economic wealth does have some influence on public health outcomes, but other socio-economic factors may also play significant roles.
Crude death rates are difficult to predict solely based on economic and literacy data, as multiple unaccounted variables (e.g., healthcare quality, lifestyle factors) may be at play.
Future studies could incorporate additional data sources, such as healthcare spending, demographic trends, and government policies, to improve predictive accuracy.
