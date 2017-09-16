from datetime import datetime
import requests


class OpenWeatherDataReq:
    def __init__(self):
        self.app_id = 'daeb7968eea4fbfcf0c44c073bb24a6d'
        self.request_url = "http://api.openweathermap.org/data/2.5/forecast?q=London,uk&APPID={}".format(self.app_id)
        self.response = requests.get(self.request_url)
        self.json_response = self.response.json()
        self.kelv_to_cels_adj = -273.15

    def get_date_data(self, yyyymmdd_date):
        """
        This function expects a date input in the YYYYMMDD format.
        It pulls the entire JSON weather forecast data for that date.
        """
        try:
            date = datetime.strptime(yyyymmdd_date, '%Y%m%d').strftime('%Y-%m-%d')
            return [{
                    key['dt_txt']:
                        {
                            'description': key['weather'][0]['description'],
                            'temperature': '{}C'.format(int(key['main']['temp'] + self.kelv_to_cels_adj)),
                            'pressure': key['main']['pressure'],
                            'humidity': '{}%'.format(key['main']['humidity'])
                        }
                    }
                    for key in self.json_response['list'] if date in key['dt_txt']]
        except:
            return {'status': 'error', 'message': 'No data for {}'.format(date)}

    def get_datetime_data(self, yyyymmdd_date, hhmm_time):
        """
        This function expects a date input in the YYYYMMDD format, and a time input in the HHMM format.
        It pulls the JSON weather forecast data for that date and time.
        """
        try:
            date = datetime.strptime(yyyymmdd_date, '%Y%m%d').strftime('%Y-%m-%d')
            time = datetime.strptime(hhmm_time, '%H%M').strftime('%H:%M:%S')
            return [{
                        'description': key['weather'][0]['description'],
                        'temperature': '{}C'.format(int(key['main']['temp'] + self.kelv_to_cels_adj)),
                        'pressure': key['main']['pressure'],
                        'humidity': '{}%'.format(key['main']['humidity'])
                    }
                    for key in self.json_response['list'] if all((date in key['dt_txt'], time in key['dt_txt']))][0]
        except:
            return {'status': 'error', 'message': 'No data for {} {}'.format(date, time)}
