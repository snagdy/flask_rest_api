from pprint import pprint
from datetime import datetime
import requests


app_id = 'daeb7968eea4fbfcf0c44c073bb24a6d'
request_url = "http://api.openweathermap.org/data/2.5/forecast?q=London,uk&APPID={}".format(app_id)
response = requests.get(request_url)
json_response = response.json()
# pprint(json_response)
dates_list = [key['dt_txt'][:10] for key in json_response['list']]
kelv_to_cels_adj = -273.15


# def get_date(date):

def get_date_data(yyyymmdd_date):
    """
    This function expects a date input in the YYYYMMDD format.
    It pulls the entire JSON weather forecast data for that date.
    """
    try:
        date = datetime.strptime(yyyymmdd_date, '%Y%m%d').strftime('%Y-%m-%d')
        return [{'date_time': key['dt_txt'],
                 'description': key['weather'][0]['description'],
                 'temperature': '{}C'.format(int(['main']['temp']+kelv_to_cels_adj)),
                 'pressure': key['main']['pressure'],
                 'humidity': '{}%'.format(key['main']['humidity'])} for key in json_response['list'] if date in key['dt_txt']]
    except:
        return {'status': 'error', 'message': 'No data for {}.'.format(yyyymmdd_date)}


def get_datetime_data(yyyymmdd_date, hhmm_time):
    """
    This function expects a date input in the YYYYMMDD format, and a time input in the HHMM format.
    It pulls the JSON weather forecast data for that date and time.
    """
    try:
        date = datetime.strptime(yyyymmdd_date, '%Y%m%d').strftime('%Y-%m-%d')
        time = datetime.strptime(hhmm_time, '%H%M').strftime('%H:%M:%S')
        return [{'date_time': key['dt_txt'],
                 'description': key['weather'][0]['description'],
                 'temperature': '{}C'.format(int(key['main']['temp']+kelv_to_cels_adj)),
                 'pressure': key['main']['pressure'],
                 'humidity': '{}%'.format(key['main']['humidity'])} for key in json_response['list'] if
                all((date in key['dt_txt'], time in key['dt_txt']))][0]
    except:
        return {'status': 'error', 'message': 'No data for {} {}'.format(date, time)}
