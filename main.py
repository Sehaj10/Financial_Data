from alpha_vantage.timeseries import TimeSeries 
import time
import requests
import json 
from pandas import json_normalize
import pandas as pd

# Enter the csv file name which contains your ticker symbols
df1 = pd.read_csv('TickerFile.csv')
print(df1)
list_of_tickers = df1['Ticker'].to_numpy()

#Enter your API Key
key = 'API_Key'

#Enter the path of the folder where you want to save the file (include a '/' at the end)
pathway = r'/Users/sehaj/Downloads/F1/Output/' 

def earnings(key, list_of_tickers, output_path): 
    
    # counter
    i = 0
    # empty datafraame
    df2 = pd.DataFrame()

    
    for ticker in list_of_tickers:
        i = i + 1 
        url = 'https://www.alphavantage.co/query?function=INCOME_STATEMENT&symbol={}&apikey={}'.format(ticker, key)

        # request fn our URL string is passed here 
        response = requests.get(url)
        
        # dumping all data into python object 
        response_dict = response.json()

        
        if i % 4 == 0:
            print("waiting ...")
            time.sleep(60)
        
        # type check make sure its a dict 
        print(type(response_dict))

        try:
            # you take headers of dictionary and state its header'
            # extracting list object
            selected_json = response_dict['annualReports']
        except:
            print("Didnt data save", ticker)
            continue
        
        if isinstance(selected_json, list):
            pass
        try:
            selected_json = response_dict['annualReports']
        except:
            # _, header= response.json()
            # print(_)
            # print(header)
            print("Didnt data save", ticker)
            continue

        # python list selected json into pandas dataframe insert database do dynamic serverless function 
        df = pd.DataFrame(selected_json)
        print(df.head)
        df.to_csv(output_path + 'file_annualReports_{}.csv'.format(str(ticker)))
    
    return print("succesful query from API alpha vantage")

earnings(key, list_of_tickers, pathway)
