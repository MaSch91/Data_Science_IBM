import yfinance as yf
import pandas as pd
import requests
from bs4 import BeautifulSoup
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.io as pio
pio.renderers.default = "iframe"

import warnings
# Ignore all warnings
warnings.filterwarnings("ignore", category=FutureWarning)

def make_graph(stock_data, revenue_data, stock):
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, subplot_titles=("Historical Share Price", "Historical Revenue"), vertical_spacing = .3)
    stock_data_specific = stock_data[stock_data.Date <= '2021-06-14']
    revenue_data_specific = revenue_data[revenue_data.Date <= '2021-04-30']
    fig.add_trace(go.Scatter(x=pd.to_datetime(stock_data_specific.Date, infer_datetime_format=True), y=stock_data_specific.Close.astype("float"), name="Share Price"), row=1, col=1)
    fig.add_trace(go.Scatter(x=pd.to_datetime(revenue_data_specific.Date, infer_datetime_format=True), y=revenue_data_specific.Revenue.astype("float"), name="Revenue"), row=2, col=1)
    fig.update_xaxes(title_text="Date", row=1, col=1)
    fig.update_xaxes(title_text="Date", row=2, col=1)
    fig.update_yaxes(title_text="Price ($US)", row=1, col=1)
    fig.update_yaxes(title_text="Revenue ($US Millions)", row=2, col=1)
    fig.update_layout(showlegend=False,
    height=900,
    title=stock,
    xaxis_rangeslider_visible=True)
    fig.show()
    from IPython.display import display, HTML
    fig_html = fig.to_html()
    display(HTML(fig_html))

tsla = yf.Ticker("TSLA")
tsla = tsla.history(period = "max")
tsla.reset_index(inplace=True)

html_data = pd.read_html(url)

tesla_revenue = html_data[1]

tesla_revenue.columns = ['Date', 'Revenue']

tesla_revenue.head()

tesla_revenue['Revenue'] = tesla_revenue['Revenue'].str.replace(',', '', regex=True)
tesla_revenue['Revenue'] = tesla_revenue['Revenue'].str.replace(r'\$', '', regex=True)

# Convert the 'Revenue' column to numeric
tesla_revenue['Revenue'] = pd.to_numeric(tesla_revenue['Revenue'])

tesla_revenue.dropna(inplace=True)

tesla_revenue = tesla_revenue[tesla_revenue['Revenue'] != ""]

tesla_revenue.tail()

gme = yf.Ticker("GME")

gme_data = gme.history(period = "max")

gme_data.reset_index(inplace=True)

gme_data.head()

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html"

html_data_2 = pd.read_html(url)

gme_revenue = html_data_2[1]

gme_revenue.columns = ['Date', 'Revenue']

gme_revenue['Revenue'] = gme_revenue['Revenue'].str.replace(',', '', regex=True)
gme_revenue['Revenue'] = gme_revenue['Revenue'].str.replace(r'\$', '', regex=True)

gme_revenue.tail()

make_graph(tsla, tesla_revenue, 'Tesla')
make_graph(gme_data,gme_revenue, 'GameStop')
