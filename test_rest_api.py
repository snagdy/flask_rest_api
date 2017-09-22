from flask import Flask, jsonify, abort
from open_weather_data import OpenWeatherDataReq as owdr

app = Flask(__name__)


@app.route('/weather/london/<app_id>/<date>/<kelvin>/')
@app.route('/weather/london/<app_id>/<date>/<hour_minute>/<kelvin>/')
@app.route('/weather/london/<app_id>/<date>/<hour_minute>/<attribute>/<kelvin>/')
def request_weather_data(app_id, date, hour_minute=None, attribute=None, kelvin=None):
    new_req = owdr(app_id)
    if not date:
        abort(404)
    if not kelvin:
        if not hour_minute:
            return jsonify(new_req.get_date_data(date))
        if not attribute:
            return jsonify(new_req.get_datetime_data(date, hour_minute))
        return jsonify({attribute: new_req.get_datetime_data(date, hour_minute)[attribute]})
    if kelvin == 'kelvin':
        if not hour_minute:
            return jsonify(new_req.get_date_data(date, kelvin=True))
        if not attribute:
            return jsonify(new_req.get_datetime_data(date, hour_minute, kelvin=True))
        return jsonify({attribute: new_req.get_datetime_data(date, hour_minute, kelvin=True)[attribute]})
