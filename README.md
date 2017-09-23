### How to Launch the Flask Application
1. Firstly, activate the virtualenv inside:
```
./flask_project/flask_project/Scripts/activate
```
* Or on Linux:
```
source ./flask_project/flask_project/Scripts/activate
```
2. Depending on your OS (Windows or Linux): 
```
[export|set] FLASK_APP=test_rest_api.py
```
3. Run the application using:
```
flask run
```
 
---
### REST API Syntax
For now, the rest API syntax is as follows:

```
http://<host:port>/weather/london/<app_id>/<date>/<hour minute>/<attribute>/<temp_unit>/
```

Where:

| Syntax Element | Meaning |
| --- | --- |
| \<host:port> | The host's IP or domain name and Flask's listening port. |
| \<app_id> | Your api.openweathermap.org ID, sign up to get one. |
| \<date> | A date in the YYYYMMDD format. |
| \<hour minute> | A time in the HHMM format. |
| \<attribute> | An attribute from the attribute list below. |
| \<temp_unit> | Specify if your desired temperature unit, either as in 'kelvin' or 'celsius'. |

#### Attributes
The following attributes can be queried for a given date and time.

- description
- temperature
- humidity
- pressure
