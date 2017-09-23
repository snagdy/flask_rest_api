from datetime import datetime
import requests


class OpenWeatherDataReq(object):
    def __init__(self, app_id):
        # 'daeb7968eea4fbfcf0c44c073bb24a6d' is our default app_id for testing.
        self.app_id = app_id
        self.request_url = "http://api.openweathermap.org/data/2.5/forecast?q=London,uk&APPID={}".format(self.app_id)
        self.response = requests.get(self.request_url)
        self.json_response = self.response.json()
        self.kelv_to_cels_adj = -273.15

    def validate_app_id(self):
        if self.json_response['cod'] == 401:
            print 'invalid api key'
            return False
        else:
            print 'valid api key'
            return True

    def get_date_data(self, yyyymmdd_date, temp_unit):
        """
        This function expects a date input in the YYYYMMDD format.
        It pulls the entire JSON weather forecast data for that date.
        """
        try:
            date = datetime.strptime(yyyymmdd_date, '%Y%m%d').strftime('%Y-%m-%d')
            if temp_unit == 'celsius':
                return \
                    {
                        key['dt_txt']:
                        {
                            'description': key['weather'][0]['description'],
                            'temperature': '{}C'.format(int(key['main']['temp'] + self.kelv_to_cels_adj)),
                            'pressure': key['main']['pressure'],
                            'humidity': '{}%'.format(key['main']['humidity'])
                        }
                        for key in self.json_response['list'] if date in key['dt_txt']
                    }
            elif temp_unit == 'kelvin':
                return \
                    {
                        key['dt_txt']:
                        {
                            'description': key['weather'][0]['description'],
                            'temperature': '{}K'.format(int(key['main']['temp'])),
                            'pressure': key['main']['pressure'],
                            'humidity': '{}%'.format(key['main']['humidity'])
                        }
                        for key in self.json_response['list'] if date in key['dt_txt']
                    }
            else:
                return {'status': '400',
                        'message': 'Bad Request. {} is an invalid temperature unit.'.format(temp_unit)}
        except:
            try:
                return {'status': '404',
                        'message': 'Not Found. No data for {}'.format(date)}
            except UnboundLocalError:
                return {'status': '400',
                        'message': 'Bad Request. {} is an invalid date input'.format(yyyymmdd_date)}

    def get_datetime_data(self, yyyymmdd_date, hhmm_time, temp_unit):
        """
        This function expects a date input in the YYYYMMDD format, and a time input in the HHMM format.
        It pulls the JSON weather forecast data for that date and time.
        """
        try:
            date = datetime.strptime(yyyymmdd_date, '%Y%m%d').strftime('%Y-%m-%d')
            time = datetime.strptime(hhmm_time, '%H%M').strftime('%H:%M:%S')
            if temp_unit == 'celsius':
                return [{
                    'description': key['weather'][0]['description'],
                    'temperature': '{}C'.format(int(key['main']['temp'] + self.kelv_to_cels_adj)),
                    'pressure': key['main']['pressure'],
                    'humidity': '{}%'.format(key['main']['humidity'])
                }
                    for key in self.json_response['list'] if all((date in key['dt_txt'], time in key['dt_txt']))][0]
            elif temp_unit == 'kelvin':
                return [{
                    'description': key['weather'][0]['description'],
                    'temperature': '{}K'.format(int(key['main']['temp'])),
                    'pressure': key['main']['pressure'],
                    'humidity': '{}%'.format(key['main']['humidity'])
                }
                    for key in self.json_response['list'] if all((date in key['dt_txt'], time in key['dt_txt']))][0]
            else:
                return {'status': '400',
                        'message': 'Bad Request. {} is an invalid temperature unit.'.format(temp_unit)}
        except:
            try:
                return {'status': '404',
                        'message': 'Not Found. No data for {} {}'.format(date, time)}
            except UnboundLocalError:
                return {'status': '400',
                        'message': 'Bad Request. {} {} is an invalid date time input'.format(yyyymmdd_date, hhmm_time)}
