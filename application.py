import bs4 
import flask
import requests
import schedule
import time


from datetime import date
from requests.exceptions import Timeout





url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports_us/08-01-2022.csv"


def update_url():
    today_date = date.today().strftime("%m-%d-%y")
    url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports_us/{date}.csv".format(date = today_date)

    return url

def get_request(url):
    # Today date not working, need to revisit
    today_date = date.today().strftime("%m-%d-%y")
    try:

        request = requests.get(url, timeout=10)
        open("{date}", "wb").write(request.content).format(date=today_date)

    except Timeout:
        print("Timeout raised")

get_request(url)
        

#schedule.every().day.at("21:30").do(get_request, url)


#while True:
    #schedule.run_pending()
    #time.sleep(1)
