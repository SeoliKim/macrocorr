import pandas as pd
import macrocorr as mc


apple_stock_dataset=pd.read_csv(r'C:/Users/seoli/Project/macrocorr.git/macrocorr/Usage/example/AAPL.csv')
print(apple_stock_dataset['Date'].values[-1])

apple_stock_correlator= mc.correlator(date=apple_stock_dataset['Date'].values, data_x=apple_stock_dataset['Close'].values)

# apple_stock_correlator.analyze_Correlation(ctegory='population')

apple_stock_correlator.get_Correlation(y_name="Net Financial Account", graph=True)


