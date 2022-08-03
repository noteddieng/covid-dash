import requests
import schedule
import time
import pandas as pd

from datetime import date
from datetime import datetime
from datetime import timedelta
from requests.exceptions import Timeout



# Set global variables
global today_date
global yesterday

today_date = date.today().strftime("%m-%d-%Y")
yesterday = datetime.today() - timedelta(days=1)
yesterday = yesterday.strftime("%m-%d-%Y")

def create_df():
    try:
        url =  "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports_us/{date}.csv".format(date = today_date)

        request = requests.get(url, timeout = 10)

        try:
            req_status = request.raise_for_status()
            df = pd.read_csv(url)

            return df

        except requests.exceptions.HTTPError:
            reupdated_url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports_us/{yesterday}.csv".format(yesterday = yesterday)
            df = pd.read_csv(reupdated_url)

            return df
    except Timeout:
        print('Timeout Raised')

print(create_df())

schedule.every().day.at("21:30").do(create_df)


while True:
    schedule.run_pending()
    time.sleep(1)
