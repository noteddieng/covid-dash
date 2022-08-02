from abc import update_abstractmethods
from urllib.error import HTTPError
import requests

from requests import Timeout
from datetime import datetime
from datetime import date
from datetime import timedelta

global today_date

today_date = date.today().strftime("%m-%d-%y")


def update_url():

    url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports_us/{date}.csv".format(date = today_date)

    return url


def get_request():

    try:
        
        #https://google.com
    
        request = requests.get(update_url(), timeout=10)
        
        try:
            req_status = request.raise_for_status()
            open("%s.csv" % today_date, "wb").write(request.content)

        except requests.exceptions.HTTPError:

            print(requests.exceptions.HTTPError)
            
    
    except Timeout:
        print("Timeout raised")

def reupdate_url():
    
    yesterday = datetime.today() - timedelta(days=1)

    yesterday = yesterday.strftime("%m-%d-%Y")
    
    url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports_us/{yesterday}.csv".format(yesterday = yesterday)
    print(url)



reupdate_url()