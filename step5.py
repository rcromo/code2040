import requests;
import datetime;

api_token = "98167604da0984648f3b69b863562265"
grab = "http://challenge.code2040.org/api/dating"
post_to = "http://challenge.code2040.org/api/dating/validate"

r_1 = requests.post(grab, data = {'token': api_token})

dictionary = r_1.json()
datestamp = dictionary['datestamp']
interval = dictionary['interval']

### parse the datetime which has format year-month-day T hour-minutes-seconds Z

date_time = datestamp.split('T')
date = date_time[0]
time = date_time[1].split('Z')[0]


date_form = date + ' ' + time
format_date_form = datetime.datetime.strptime(date_form,'%Y-%m-%d %H:%M:%S') ##stringify 


## Now want to add the seconds to our time

new_datestamp = format_date_form + datetime.timedelta(seconds = interval)
new_datestamp = new_datestamp.strftime('%Y-%m-%d %H:%M:%S') ## convert from string to datetime 
format_new_datestamp = new_datestamp.split(' ')[0] + "T" + new_datestamp.split(' ')[1] + "Z"


r_2 = requests.post(post_to, data = {'token': api_token, 'datestamp':format_new_datestamp})
print(r_2.text)