from datetime import date

def update_url():
    today_date = date.today().strftime("%m-%d-%y")
    url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports_us/{date}.csv".format(date = today_date)

    return url

def print_url():

    print(update_url())

print_url()