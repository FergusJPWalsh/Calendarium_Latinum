import tweepy
import datetime
from datetime import date
import calendar
import csv

consumer_key = "XXXX"
consumer_secret = "XXXX" 
access_token = "XXXX" 
access_token_secret = "XXXX"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

current_year = datetime.datetime.now()
auc = current_year.replace(year=(current_year.year+753))
auc = auc.year
current_year = current_year.year

start = date(current_year, 1, 1)
end = date(current_year, 12, 31)
dates = (start + datetime.timedelta(days=x) for x in range(0, (end-start).days))
text = []
with open("Calendarium Latinum.csv") as f:
    reader = csv.reader(f)
    for rows in reader:
        if calendar.isleap(current_year):
            text.append(rows[1])
        else:
            text.append(rows[0])

calendarium = dict(zip(dates, text))
today = date.today()
wkdays = ["dies Lunae, ","dies Martis, ","dies Mercurii, ","dies Iovis, ","dies Veneris, ","dies Saturni, ","dies Solis sive dies Dominicus, "]
wkday = wkdays[today.weekday()]
if today in calendarium:
    hodie = "Est hodie " + wkday + calendarium[today] + ", ab urbe condita " + str(auc)
str(hodie)
api.update_status(hodie)
