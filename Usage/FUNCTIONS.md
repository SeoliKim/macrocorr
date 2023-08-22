#Functions

### Table of Contents
1. [macrocorr.Correlator](##macrocorr.Correlator)
2. [macrocorr.Correlator.analyze_Correlation](##**macrocorr.Correlator.analyze_Correlation**)
3. [macrocorr.Correlator.get_Correlation](##**macrocorr.Correlator.get_Correlation**)

<br/>

## **macrocorr.Correlator**

**macrocorr.Correlator(data_x, date, start_date=None, end_date=None)**

&emsp;  Create a correlator with input time-series data and respective date index

**Parameter:**

- **data_x: 1D array_like**
    
    One time-series array containing the numerical value of a single variable.
    
    Tips: When the data is a [pandas dataframe](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html).
    
    ```python
    data_x=my_dataframe['Variable'].values
    ```
    
- **date: array of Datetimeindex**
    
    the format of the date should be able to understand by **[pandas.to_datetime](https://pandas.pydata.org/docs/reference/api/pandas.to_datetime.html).**
    
    Make sure number of values in the date matches number of values in data_x. 
    
- **start_date, end_date: Datetimeindex, optional**
    
    Specify a start_date or an end_date for data_x
    
    start_date, end_date should be within the range of date and at the same time frequency

**Return:**

Correlator that be used for other functions of analyzing and comparing. See below. 

**Example:** 

```python
import macrocorr as mcrr
my_correlator= mcrr.Correlator(date=my_dataset['Date'].values, data_x=my_dataset['Current_price'].values, start_date="2000-09-01", end_date="2022-12-01")
```
<br/>

## **macrocorr.Correlator.analyze_Correlation**

**macrocorr.Correlator.analyze_Correlation(category='population’, country='USA', top_num=3)**

Analyze and compare the input data with the macroeconomic indicators from the indicated category. 

The correlation is dependent on [SciPy](https://scipy.org/)’s built function to get the Pearson coefficient. For details, please check out ****[scipy.stats.pearsonr](**https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.pearsonr.html**).****

**Parameter:**

- **category: string (one category), optional (default= ’population’)**
    
    One category of macroeconomic indicators
    
    There are currently six categories: 
    
    - **commodity**
    - **development**
    - **economics**
    - **finance**
    - **international**
    - **population**
    
    To view more details, visit [CATALOG](https://github.com/SeoliKim/macrocorr/blob/main/Usage/CATALOG.md).
    
- **country: string (one nation), optional (default= 'USA')**
    
    The dedicated nation for national-scale macroeconomic indicators
    
    To view details about country name, visit [World Bank Country and regions](https://datahelpdesk.worldbank.org/knowledgebase/articles/906519-world-bank-country-and-lending-groups). 
    
- **top_num: int, optional (default= 3)**
    
    the number should be smaller than the total number of indicators in respective category, make sure to enter a valid value. Recommended from 1-5

**Result Printed:**

Massage of the most correlated macro-indicators of the top_num
” Name_of_indicator: Pearson coefficient of XXXX with p-value of XXXX”
The graph of the input data with the most correlated macro-indicator from the category

**Example:** 

```python
my_correlator.analyze_Correlation(category="finance", country='japan', top_num=5)
```

<br/>

## **macrocorr.Correlator.get_Correlation**

**macrocorr.Correlator.get_Correlation(y_name, country='USA', graph=True)**

Analyze and compare the input data with the indicated macroeconomic indicator

The correlation is dependent on [SciPy](https://scipy.org/)’s built function to get the Pearson coefficient. For details, please check out ****[scipy.stats.pearsonr](**https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.pearsonr.html**).****

**Parameter:**

- **y_name: string (one macroeconomic indicator ),**
    
    One specific macroeconomic indicators
    
    To view a complete list of provided macroeconomic indicator , visit [CATALOG](https://github.com/SeoliKim/macrocorr/blob/main/Usage/CATALOG.md).
    
- **country: string (one nation), optional (default= 'USA')**
    
    The dedicated nation for national-scale macroeconomic indicators
    
    To view details about country name, visit [World Bank Country and regions](https://datahelpdesk.worldbank.org/knowledgebase/articles/906519-world-bank-country-and-lending-groups). 
    
- **graph: boolean, optional (default= true)**
    
    if you want the graph of the input data with the correlated macro-indicator
**Result Printed:**

” Name_of_indicator: Pearson coefficient of XXXX with p-value of XXXX”
The graph of the input data with the macro-indicator

**Example:** 

```python
my_correlator.get_Correlation(y-name="Export volume index", country='france', graph=False)
```