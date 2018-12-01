### How to Launch the Flask Application
1. Firstly, activate the virtualenv inside:
```
./flask_project/env/Scripts/activate
```
* Or on Linux:
```
source ./flask_project/env/Scripts/activate
```
2. Depending on your OS (Linux or Windows): 
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
3. Run the application using:
```
flask run
```
 
---
### REST API Syntax
For now, the rest API syntax is as follows:

```
http://<host:port>/api?city=<city_name>&app_id=<app_id>&date=<date>
```

Where:

| Syntax Element | Meaning |
| --- | --- |
| \<host:port> | The host's IP or domain name and Flask's listening port. |
| \<city_name> | The name of the city you want data for|
| \<app_id> | Your api.openweathermap.org ID, sign up to get one. |
| \<date> | A date in the YYYYMMDD format. ||

