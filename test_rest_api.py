import logging

from os import getpid
from sys import stdout
from logging import StreamHandler
from logging.handlers import RotatingFileHandler
from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse
from datetime import datetime
from open_weather_data import OpenWeatherDataReq

app = Flask(__name__)
api = Api(app)
pid = getpid()


# Default web query:
# http://127.0.0.1:5000/api?city=London&app_id=daeb7968eea4fbfcf0c44c073bb24a6d&date=20181201
def weather_data_query(city, app_id, date, **kwargs):
    print 'PID: {}'.format(pid)
    app.logger.info("The process id is: %s", pid)
    print locals()
    new_req = OpenWeatherDataReq(city, app_id)
    if new_req.validate_app_id() is not True:
        app.logger.error('ERROR 401 - Unauthorised request using app_id %s', app_id)
        response = {
                        'status': '401',
                        'message': 'Unauthorised. See http://openweathermap.org/faq#error401 for more info.'
                    }
        return jsonify(response)
    else:
        return jsonify(
            {
                'status': new_req.json_response['cod'],
                'name': new_req.json_response['city']['name'],
                'country': new_req.json_response['city']['country'],
                'population': new_req.json_response['city']['population'],
                '{}'.format(date):
                    # TODO: Create a data-structure class to represent these API responses.
                    [
                    {
                        datetime.strptime(date_dict['dt_txt'].replace('-', ''), '%Y%m%d %H:%M:%S').strftime('%H:%M:%S'):
                        {
                            'clouds': date_dict['clouds'],
                            'main': date_dict['main'],
                            'description': date_dict['weather'][0]['description'],
                            'wind': date_dict['wind']
                         }
                    }
                    for date_dict in new_req.json_response['list'] if date in date_dict['dt_txt']
                    ]
            }
        )


class WeatherAPI(Resource):
    def get(self):
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument('city',
                            type=str,
                            required=True,
                            location='args',
                            help='Please provide a valid city name.')
        parser.add_argument('app_id',
                            type=str,
                            required=True,
                            location='args',
                            help='Missing an app_id. Get one by registering here: http://openweathermap.org')
        parser.add_argument('date',
                            type=str,
                            required=True,
                            location='args',
                            help='Please provide YYYYMMDD date string')

        query_dict = parser.parse_args()

        city = query_dict['city']
        app_id = query_dict['app_id']
        date = datetime.strptime(query_dict['date'], '%Y%m%d').strftime('%Y-%m-%d')

        return weather_data_query(city, app_id, date)


api.add_resource(WeatherAPI, '/api', endpoint='api')

if __name__ == '__main__':
    handler = RotatingFileHandler(filename='test_rest_api.log', maxBytes=10000, backupCount=1)
    stream_handler = StreamHandler(stdout)
    handler.setLevel(logging.DEBUG)
    app.logger.addHandler(handler) #To log to a rotating file.
    app.logger.addHandler(stream_handler) # To log to stdout.
    app.run(debug=True, host='0.0.0.0', port='8888')
