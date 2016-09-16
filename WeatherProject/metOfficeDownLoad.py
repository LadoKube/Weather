import requests
import re
import datetime
import time
import os


# function to build form data given date and time
def get_form_data(date, time):
   return {'Type': 'Forecast',
           'PredictionSiteID': '352409',
           'ObservationSiteID': '352409',
           'Date': date,
           'PredictionTime': time}


# function to generate dates
def daterange(start_date, end_date):
   for n in range(int((end_date - start_date).days)):
       yield start_date + datetime.timedelta(n)


# Settings

start_date = datetime.date(2016, datetime.datetime.now().month, datetime.datetime.now().day )
end_date = datetime.date(2016, datetime.datetime.now().month, datetime.datetime.now().day + 1) # Add one more day than you want.
start_hour = 10
end_hour = 23
save_location = r'C:\Projects\WeatherData\output_{0}_{1}.csv'
timer_delay = 0.1

# A list to hold errored dates
missing_dates = []
count = 0
# iterate through each date

for single_date in daterange(start_date, end_date):

  request_date = time.strftime("%d/%m/%Y", single_date.timetuple())  # get the date string for use in the post request
  file_date = time.strftime("%Y%m%d", single_date.timetuple())  # get the date string for use in the file name

  # iterate through each hour

  for x in xrange(start_hour, end_hour + 1):  # have to use end_hour + 1 as range is exclusive on upper side
      while count == 0:
           request_time = str(x).zfill(2) + '00'  # get the hour string
           # get the form data
           form_data = get_form_data(request_date, request_time)
           # send the request, and then search the response for https addresses
           try:
               r = requests.post("http://datagovuk.cloudapp.net/query", data=form_data)
           except:
               missing_dates.append(['Post request failed.', request_date, request_time])
               continue
           if not r.ok:
               missing_dates.append(['Bad get response.', request_date, request_time])
               continue
               # search the response for the csv url
           urls = re.findall('https://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', r.text)
           if len(urls) == 0:
               print("No Urls Found for {0}:{1}".format(request_date, request_time))
               if "No matching records were found." in r.text:
                   missing_dates.append(['No Url. Missing Data.', request_date, request_time])
               else:
                   missing_dates.append(['No Url. Other.', request_date, request_time])
               continue
           # visit the csv url, streaming the file to disk
           with open(save_location.format(file_date, request_time), 'wb') as handle:
               try:
                   r = requests.get(urls[0], stream=True)
               except:
                   missing_dates.append(['Get request failed.', request_date, request_time])
                   continue
               if not r.ok:
                   missing_dates.append(['Bad get response.', request_date, request_time])
                   continue
               for block in r.iter_content(1024):
                   if not block:
                       break

                   handle.write(block)
                   count = 1


           time.sleep(timer_delay)

