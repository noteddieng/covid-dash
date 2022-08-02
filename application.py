
import requests
import schedule
import time
import csv


from datetime import date
from requests.exceptions import Timeout


# Token - DELETE: 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

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
            print('URL Error')
            
    
    except Timeout:
        print("Timeout raised")

get_request()

schedule.every().day.at("21:30").do(get_request, update_url)


while True:
    schedule.run_pending()
    time.sleep(1)
