import requests
import argparse



class OpenWeatherDataReq(object):
    def __init__(self, city, app_id):
        # 'daeb7968eea4fbfcf0c44c073bb24a6d' is our default app_id for testing.
        self.app_id = app_id
        self.city = city
        self.request_url = "http://api.openweathermap.org/data/2.5/forecast?q={}&APPID={}".format(self.city, self.app_id)
        self.response = requests.get(self.request_url)
        self.json_response = self.response.json()
        self.kelv_to_cels_adj = -273.15
        self.args = argparse.ArgumentParser()

    def validate_app_id(self):
        if self.json_response['cod'] == 401:
            return False
        else:
            return True
