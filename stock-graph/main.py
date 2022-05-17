# pip install streamlit fbprophet yfinance plotly
import streamlit as st
from datetime import date
from PIL import Image
import yfinance as yf
from plotly import graph_objs as go

START = "2018-01-01"
TODAY = date.today().strftime("%Y-%m-%d")

st.title('Pulse~Stock-graph')
image = Image.open('2.png')
st.image(image, width=200)
st.write("""
This app shows the stockmarket opening and closing prize using the yfinance API!
***
""")

stocks = ('GOOGL', 'AAPL', 'MSFT', 'SBI', 'RELI','ICBK','IDEA.NS','FB','IBM','YESBANK.NS')
selected_stock = st.selectbox('Select dataset for prediction', stocks)

@st.cache
def load_data(ticker):
    data = yf.download(ticker, START, TODAY)
    data.reset_index(inplace=True)
    return data


data_load_state = st.text('Loading data...')
data = load_data(selected_stock)
data_load_state.text('Loading data... done!')

st.subheader('Raw data')
st.write(data.tail())


# Plot raw data
def plot_raw_data():
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name="stock_open"))
    fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name="stock_close"))
    fig.layout.update(title_text='Time Series data with Rangeslider', xaxis_rangeslider_visible=True)
    st.plotly_chart(fig, width=2500, height=2000)


plot_raw_data()
