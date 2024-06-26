# macrocorr

Macrocorr (’macroeconomic correlation’) is a Python package for analyzing the correlation between macroeconomic indicators and time-series data. 

*Pearson's correlation* is used to analyze the correlation. This package uses [SciPy](https://scipy.org/)’s built function to get the Pearson coefficient. For details, please check out **[scipy.stats.pearsonr](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.pearsonr.html).** 

This package is designed to provide the easy process of analyzing and comparing the correlations with multiple macroeconomic indicators at a single time. The result is intended to provide an overview of macroeconomic relationships. It should not be used for profitable purposes.

The data of the macroeconomic indicators are extracted from [WorldBank](https://databank.worldbank.org/) and [YahooFinance](https://finance.yahoo.com/lookup?s=DATA) historical database. This package doesn’t guarantee the accuracy of the correlated data.

## Installation

The latest stable release (and required dependencies) can be installed from [pip](https://pypi.org/project/macrocorr/).

```bash
pip install macrocorr
```

## Usage
- For all macroeconomic indicators and all major categories, check out [CATALOG](https://github.com/SeoliKim/macrocorr/blob/main/Usage/CATALOG.md).
- For more detailed uses of the functions, check out [FUNCTIONS](https://github.com/SeoliKim/macrocorr/blob/main/Usage/FUNCTIONS.md).
- For a step-by-step example use-case, check out [example_basic.ipynb](https://github.com/SeoliKim/macrocorr/blob/main/Usage/example/example_basic.ipynb).

#### Quick Start

1. Import package Macrocorr

```python
import macrocorr as mcrr
```

2. Create a correlator with the data you want to analyze

```python
my_correlator= mcrr.Correlator(date=my_data['Date'].values, data_x=my_data['Price'].values)
# data_x should be an one-dimensional array of numerical value
# make sure the values from date and data_x are matched
```

3. Analyze and compare the correlation with the macroeconomic indicators from a category

```python
my_correlator.analyze_Correlation(category='population', country='USA', top_num=3)
# print the top 3 most correlated indicators from the category (='population') 
# with their respective Pearson's coefficient and p-value
# plot the graph with both the input data and data of the most correlated indicator
```

4. Analyze the correlation with one specific indicator

```python
my_correlator.get_Correlation(y_name="Population, total", graph=True)
# print the Pearson's coefficient and p-value of the indicator (='Population, total') 
# plot the graph with both the input data and data of the indicator
```
</br>

## Contributing

Development takes place on [Github](https://github.com/SeoliKim/macrocorr)

Pull requests are welcome. Feel free to add more macroeconomic indicators or analysis methods.

For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
</br>

## License

[MIT](https://choosealicense.com/licenses/mit/)
