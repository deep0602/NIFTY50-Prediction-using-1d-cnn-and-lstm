This project presents an Artificial Neural Network (ANN) approach to predict the Nifty 50 index, the most popular stock market index in india. 
Comparison was done on  deep learning models like 1-D Convolutional Neural Network (CNN) and Long Short-Term Memory (LSTM) recurrent neural network 
in modeling the complex relationships present in historical stock price data. Additionally, 
Investigation was done of  the impact of incorporating the Put call  Ratio (PCR) as an additional feature alongside stock prices.
PCR is numerical value derived from derivatives data ,which indicates market participant’s view.Four different scenarios was considered, CNN model with price only, 
CNN model with price and PCR, LSTM model with price only, and LSTM model with price and PCR.
The LSTM model performed better than CNN model. Through empirical evaluation,  assessment of the predictive performance of each model and analysis the impact of incorporating PCR as an additional feature was done. 
The output of the best performing scenario's prediction was fed to a rule based trading strategy and was backtested for the test data. 
A comparative analysis of profit made by this strategy and profit made by nifty 50 index was done. 
2019 to 2022 year's nifty50 data was considered as train data while 2023 year's data was considered as test data.
