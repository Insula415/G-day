#!/usr/bin/python3
import os
import sys
import requests
import time
import pytz
from bs4 import BeautifulSoup
from datetime import datetime

print("Good morning!!")
print("--------------------")
time = time.strftime("%H:%M", time.localtime())
print ("Current time:",time)


a = requests.get('https://www.daysoftheyear.com/')
soup = BeautifulSoup(a.text,features="html.parser")

##getting date
date = soup.find('div', {'class':'card__date subheading'}).text
print("Date:",date)
print("--------------------")
##getting international day
print("INTERNATIONAL DAY:")
day = soup.find('h3', {'class':'card__title heading'}).text
print("Today is",day)
print("--------------------")

#world time zones
print("WORLD TIMES:")
London = pytz.timezone('Europe/London')
datetime_London=datetime.now(London)
print("London time:",datetime_London.strftime("%H:%M"))

NewYork = pytz.timezone('America/New_york')
datetime_NewYork=datetime.now(NewYork)
print("New York time:",datetime_NewYork.strftime("%H:%M"))

LA = pytz.timezone('America/Los_Angeles')
datetime_LA=datetime.now(LA)
print("Los Angeles time:",datetime_LA.strftime("%H:%M"))

Tokyo = pytz.timezone('Asia/Tokyo')
datetime_Tokyo=datetime.now(Tokyo)
print("Tokyo time:",datetime_Tokyo.strftime("%H:%M"))

Amsterdam = pytz.timezone('Europe/Amsterdam')
datetime_Amsterdam=datetime.now(Amsterdam)
print("Amsterdam time:",datetime_Amsterdam.strftime("%H:%M"))

Melbourne = pytz.timezone('Australia/Melbourne')
datetime_Melbourne=datetime.now(Melbourne)
print("Melbourne time:",datetime_Melbourne.strftime("%H:%M"))

print("--------------------")
print("DAILY QUOTE")
#daily quote
b = requests.get('https://www.azquotes.com/quote_of_the_day.html')
soup = BeautifulSoup(b.text,features="html.parser")

quote = soup.find('a', {'class':'title'}).text
print(quote)

print("--------------------")
print("Let's make today productive!!")
