
import requests
import schedule
import time
import csv


from datetime import date
from requests.exceptions import Timeout


# Token - DELETE: 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



def update_url():
    today_date = date.today().strftime("%m-%d-%y")
    url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports_us/{date}.csv".format(date = today_date)

    

def get_request():
    update_url()
    

    today_date = date.today().strftime("%m-%d-%y")
    try:
        
        request = requests.get(update_url(), timeout=10)
        open("%s.csv" % today_date, "wb").write(request.content)

    except Timeout:
        print("Timeout raised")

get_request()

schedule.every().day.at("21:30").do(get_request, update_url)


while True:
    schedule.run_pending()
    time.sleep(1)
