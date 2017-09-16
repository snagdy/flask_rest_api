from flask import Flask, jsonify
import open_weather_data as owd


app = Flask(__name__)


@app.route('/weather/london/<date>/')
@app.route('/weather/london/<date>/<hour_minute>/')
@app.route('/weather/london/<date>/<hour_minute>/<attribute>/')
def request_weather_data(date, hour_minute=None, attribute=None):
    if not hour_minute:
        return jsonify(owd.get_date_data(date))
    if not attribute:
        return jsonify(owd.get_datetime_data(date, hour_minute))
    return jsonify({attribute: owd.get_datetime_data(date, hour_minute)[attribute]})
