from alpha_vantage.timeseries import TimeSeries
import time
import requests
import json
from pandas import json_normalize
import pandas as pd
import streamlit as st
import base64 
from streamlit_option_menu import option_menu


st.markdown("<h1 style='text-align: center;'>Financial Information</h1>", unsafe_allow_html=True)
#st.title('Financial Information')

interval_dict = {
    'annualReports': 'Annual',
    'quaterlyReports': 'Quarterly'
}


#info = st.selectbox('Select Type of Information', ('INCOME_STATEMENT', 'BALANCE_SHEET', 'CASH_FLOW'))
#st.markdown("<h3 style='text-align: center; color: #31333F;'>-------------------------------------------------------------------------------</h3>", unsafe_allow_html=True)
info = option_menu(
            menu_title=None,  
            options=["INCOME_STATEMENT", "BALANCE_SHEET", "CASH_FLOW"],  
            icons=["archive-fill", "activity", "cash-coin"],  
            menu_icon=None,  
            default_index=0,  
            orientation="horizontal",
            styles={
                "nav-link": {
                    "font-size": "14px",
                    "font-weight": "bold",
                    "text-align": "Center",
                }

            },
        )

interval = st.selectbox('Select Interval', list(interval_dict.values()))
selected_interval = [key for key, value in interval_dict.items() if value == interval][0]
interval_label = interval_dict.get(selected_interval, '')

user_input = st.text_input('Enter Stock Ticker (Enter multiple stocks up to 5 at a time sperated by ,)')
ticker = user_input.split(',')

key = 'IYS8IX32IVQT3XKB'

def earnings(api_key, ticker_list):
    for ticker in ticker_list:
        url = 'https://www.alphavantage.co/query?function={}&outputsize=full&symbol={}&apikey={}'.format(info, ticker.strip(), api_key)

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
        st.dataframe(df.head())
        csv_file_path = '{}_{}.csv'.format(ticker.strip(), interval_label)
        df.to_csv(csv_file_path, index=False)
        st.write("CSV file saved:", csv_file_path)
        download_button = get_csv_download_button(csv_file_path, ticker.strip(), interval_label)
        st.markdown(download_button, unsafe_allow_html=True)


def get_csv_download_button(file_path, ticker, interval_label):
    with open(file_path, 'rb') as file:
        csv_data = file.read()
    base64_encoded = base64.b64encode(csv_data).decode()
    file_name = '{}_{}'.format(ticker.strip(), interval_label)
    download_button = f'<a href="data:file/csv;base64,{base64_encoded}" download="{file_name}.csv"><button>Download CSV</button></a>'
    return download_button

earnings(key, ticker)

footer = "MADE WITH  \u2764\ufe0f  BY SEHAJ "

# Apply CSS styling to position the footer at the bottom
footer_style = """
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100%;
    text-align: center;
    padding: 10px;
    font-weight: bold;
    letter-spacing: 1.25px;
    font-size: 13px;
    color: #FC6600;
"""
st.markdown('<p style="{}">{}</p>'.format(footer_style, footer), unsafe_allow_html=True)
