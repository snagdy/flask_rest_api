from flask import Flask, jsonify, abort
from open_weather_data import OpenWeatherDataReq as owdr

app = Flask(__name__)


@app.route('/weather/london/<app_id>/<date>/<temp_unit>/')
@app.route('/weather/london/<app_id>/<date>/<hour_minute>/<temp_unit>/')
@app.route('/weather/london/<app_id>/<date>/<hour_minute>/<attribute>/<temp_unit>/')
def request_weather_data(app_id, date, hour_minute=None, attribute=None, temp_unit=None):
    new_req = owdr(app_id)
    if new_req.validate_app_id() is not True:
        response = {'status': '401',
                    'message': 'Unauthorised. See http://openweathermap.org/faq#error401 for more info.'}
        return jsonify(response)
    else:
        if not date:
            abort(404)
        if not hour_minute:
            return jsonify(new_req.get_date_data(date, temp_unit))
        if not attribute:
            return jsonify(new_req.get_datetime_data(date, hour_minute, temp_unit))
        return jsonify({attribute: new_req.get_datetime_data(date, hour_minute, temp_unit)[attribute]})
