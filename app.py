from alpha_vantage.timeseries import TimeSeries
import time
import requests
import json
from pandas import json_normalize
import pandas as pd
import streamlit as st
import base64 

st.title('Financial Information')

interval = st.selectbox('Select Interval', ('annualReports', 'quaterlyReports'))

user_input = st.text_input('Enter Stock Ticker (Enter multiple stocks sperated by ,'')')
ticker = user_input.split(',')

key = 'IYS8IX32IVQT3XKB'
#pathway = r'/Users/sehaj/Downloads/F1/Output/'

def earnings(api_key, ticker_list):
    for ticker in ticker_list:
        url = 'https://www.alphavantage.co/query?function=INCOME_STATEMENT&symbol={}&apikey={}'.format(ticker.strip(), api_key)

        response = requests.get(url)
        response_dict = response.json()
        
        if 'quarterlyReports' in response_dict:
            data = response_dict['quarterlyReports']
        elif 'annualReports' in response_dict:
            data = response_dict['annualReports']
        else:
            st.write("Ticker:", ticker)
            continue
        
        df = pd.DataFrame(data)
        st.write(df.head())
        csv_file_path = 'file_{}_{}.csv'.format(interval, ticker.strip())
        df.to_csv(csv_file_path, index=False)
        st.write("CSV file saved:", csv_file_path)
        download_button = get_csv_download_button(csv_file_path, ticker.strip())
        st.markdown(download_button, unsafe_allow_html=True)


def get_csv_download_button(file_path, ticker):
    with open(file_path, 'rb') as file:
        csv_data = file.read()
    base64_encoded = base64.b64encode(csv_data).decode()
    download_button = f'<a href="data:file/csv;base64,{base64_encoded}" download="{ticker}.csv"><button>Download CSV</button></a>'
    return download_button

earnings(key, ticker)

footer = "MADE WITH  \u2764\ufe0f  BY SEHAJ  \U0001F618"

# Apply CSS styling to position the footer at the bottom
footer_style = """
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100%;
    text-align: center;
    background-color: lightgray;
    padding: 10px;
    font-weight: bold;
"""
st.markdown('<p style="{}">{}</p>'.format(footer_style, footer), unsafe_allow_html=True)

