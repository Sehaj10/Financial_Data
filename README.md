The code fetches annual income statement data for a list of ticker symbols using the Alpha Vantage API. It saves the data as CSV files in a specified folder.​

Importing Required Libraries: The code begins by importing necessary libraries, including `TimeSeries` from `alpha_vantage.timeseries`, `time`, `requests`, `json`, `json_normalize` from `pandas`, and `pd` from `pandas`.

Reading Ticker Symbols from a CSV File: The script reads ticker symbols from a CSV file named 'TickerFile.csv' using the `pd.read_csv()` function. The ticker symbols are stored in a pandas DataFrame called `df1`.

Extracting Ticker Symbols: The code retrieves the ticker symbols from the 'Ticker' column of `df1` using `df1['Ticker'].to_numpy()`. The symbols are stored in a numpy array called `list_of_tickers`.

Setting API Key and Output Path: The user needs to provide their Alpha Vantage API key, which is stored in the variable `key`. The user also needs to specify the folder path where the output CSV files will be saved. The path is stored in the variable `pathway`.

Defining the 'earnings' Function: The script defines a function named `earnings` that takes the API key, list of tickers, and output path as inputs.

Initializing Variables: The function initializes a counter variable `i` to keep track of the ticker being processed. An empty DataFrame `df2` is created to store the combined data.

Fetching Data for Each Ticker: The function iterates over each ticker in the `list_of_tickers` using a `for` loop. It constructs the API URL for fetching income statement data by replacing the ticker symbol and API key in the URL template.

 Handling Rate Limiting: To avoid exceeding the API rate limit, the function checks if the counter `i` is a multiple of 4 (you may adjust this number as per your API's rate limits). If it is a multiple, the script prints "waiting ..." and sleeps for 60 seconds using `time.sleep(60)`.

 Processing the API Response: The function checks if the response dictionary contains the key 'annualReports' using `response_dict['annualReports']`. If the key is not found, the script prints "Didn't save data" for the ticker and continues to the next ticker using `continue`.

Converting Data to DataFrame: If 'annualReports' key exists, the function creates a DataFrame `df` from the 'annualReports' data extracted from the response dictionary.

 Saving Data as CSV:
    - The function saves the DataFrame as a CSV file in the specified output folder 

Executing the Function: The `earnings()` function is called with the API key, list of tickers, and output path provided as arguments.

The next step is to implement this code on the cloud and run it using Azure SQL and take user input for both ticker symbol and type of report instead to uploading a csv file. 
