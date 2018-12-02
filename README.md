### How to Launch the Flask Application
1. Firstly, create and activate a virtualenv using your favourite shell (CMD shell recommended on Windows OS) and 
virtualenv utility, I recommend *mkvirtualenv* from the *virtualenvwrapper-win* package; for example:
```
mkvirtualenv flask_rest_api
setprojectdir .                         # from inside the directory you cloned to.
```
2. Install the requirements from inside your virtualenv's pip package manager, using the requirements.txt, as follows:
```
pip install -r requirements.txt
```

3. Depending on your OS (Linux or Windows): 
```
export FLASK_APP=test_rest_api.py       # Linux
$env:FLASK_APP='.\test_rest_api.py'     # Windows (PowerShell)
set FLASK_APP=test_rest_api.py          # Windows (cmd)
```
For additional debugging (never do this on a production machine / in production):
```
export FLASK_ENV=development            # Linux
$env:FLASK_ENV=development              # Windows (PowerShell)
set FLASK_ENV=development               # Windows (cmd)
```
4. Run the application using:
```
flask run
```
 
---
### RESTful API Syntax
The API syntax is as follows:

```
http://<host:port>/api?city=<city_name>&app_id=<app_id>&date=<date>
```

Where the required arguments specified are as explained below:

| Syntax Element | Meaning |
| --- | --- |
| \<host:port> | The host's IP or domain name and Flask's listening port. |
| \<city_name> | The name of the city you want data for.|
| \<app_id> | Your api.openweathermap.org ID, sign up to get one. |
| \<date> | A date in the YYYYMMDD format. Do not request a historical date, you will get an empty list back.||

### Expected RESTful API Output
You can expect the output to be a dictionary containing dictionaries like this snippet below:
```
"2018-12-05": [
    {
      "00:00:00": {
        "clouds": {
          "all": 92
        }, 
        "description": "light rain", 
        "main": {
          "grnd_level": 1016.76, 
          "humidity": 99, 
          "pressure": 1016.76, 
          "sea_level": 1024.37, 
          "temp": 283.335, 
          "temp_kf": 0, 
          "temp_max": 283.335, 
          "temp_min": 283.335
        }, 
        "wind": {
          "deg": 189.501, 
          "speed": 5.56
        }
      }
    }, 
```