from flask import Flask, jsonify, abort
# import open_weather_data as owd
from open_weather_data import OpenWeatherDataReq as owdr

app = Flask(__name__)


@app.route('/weather/london/<date>/')
@app.route('/weather/london/<date>/<hour_minute>/')
@app.route('/weather/london/<date>/<hour_minute>/<attribute>/')
def request_weather_data(date, hour_minute=None, attribute=None):
    new_req = owdr()
    if not date:
        abort(404)
    if not hour_minute:
        return jsonify(new_req.get_date_data(date))
    if not attribute:
        return jsonify(new_req.get_datetime_data(date, hour_minute))
    return jsonify({attribute: new_req.get_datetime_data(date, hour_minute)[attribute]})
