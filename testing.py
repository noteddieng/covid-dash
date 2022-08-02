from abc import update_abstractmethods
from urllib.error import HTTPError
import requests

from requests import Timeout
from datetime import date

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
            print('Success')

        except requests.exceptions.HTTPError:

            print(requests.exceptions.HTTPError)
    
    except Timeout:
        print("Timeout raised")

get_request()