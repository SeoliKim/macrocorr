from macrocorr import correlator
import pandas as pd


apple_stock_dataset=pd.read_csv(r'C:/Users/seoli/Project/Macroecon/example/AAPL.csv')
print(apple_stock_dataset['Date'].values[-1])

apple_stock_correlator= correlator(date=apple_stock_dataset['Date'].values, data_x=apple_stock_dataset['Close'].values)

# apple_stock_correlator.analyze_Correlation(category='population')

apple_stock_correlator.get_Correlation(y_name="Net Financial Account", graph=True)


