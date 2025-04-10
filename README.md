
# 📈 S&P 500 Prediction using Machine Learning and Sentiment Analysis

This project combines financial, macroeconomic, and sentiment data to predict S&P 500 price movements using various machine learning models.

## Repository Structure

```
publication_sp500_pred-main/
├── data/                         # Raw and processed data files
├── results/                      # Model results and evaluation metrics
├── data_extraction.ipynb        # Pulls financial and macroeconomic data
├── data_extraction_2.ipynb      # Additional data fetching
├── data_processing.ipynb        # Cleans and prepares the dataset
├── news_sentiment_analysis.ipynb# Analyzes financial news using NLP
├── arimax.ipynb                 # ARIMAX time-series forecasting
├── random_forest.ipynb          # Random Forest model
├── lstm.ipynb                   # LSTM deep learning model
├── cnn.ipynb                    # Convolutional Neural Network model
├── xgboost.ipynb                # XGBoost implementation
```

## Key Features

-  **Time Series Forecasting** using ARIMAX and LSTM
-  **Machine Learning Models**: XGBoost, Random Forest, CNN
-  **News Sentiment Analysis** News sentiment analysis extraction from Google News using FinBERT
-  **Automated Data Extraction & Preprocessing**
-  **Model Comparison & Evaluation**


## Getting Started

1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/publication_sp500_pred.git
   cd publication_sp500_pred
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the notebooks in the following order:
   - `data_extraction.ipynb`
   - `data_processing.ipynb`
   - `news_sentiment_analysis.ipynb`
   - Choose a model notebook (e.g., `lstm.ipynb`, `xgboost.ipynb`)

## Results

Final evaluation metrics and prediction plots are saved in the `results/` directory. Each model includes performance metrics such as RMSE and directional accuracy.

## Contact

For questions or contributions, open an issue or reach out to the project maintainers.
