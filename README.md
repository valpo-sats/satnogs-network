SatNOGS Network
==============================
SatNOGS Network is a Django based application, implementing a global scheduling and monitoring network for ground station operations. It features multiple observers to multiple intrumentation functionality and manages observation jobs and results.

## Installation

### Development

Requirements: You ‘ll need python, virtualenv, pip and git

1 - Clone our code
```
$ git clone https://github.com/satnogs/satnogs-network.git
```
2 - Set up the virtual environment
```
$ cd satnogs-network/
$ virtualenv --no-site-packages ../env/satnogs
```
3 - Activate your python virtual environment
```
$ source ../env/satnogs/bin/activate
```
4 - Install local development requirements
```
(satnogs)$ pip install -r requirements/local.txt
```
5 - Create and setup the database
```
(satnogs)$ touch satnogs.db
(satnogs)$ export DATABASE_URL='sqlite:///satnogs.db'
(satnogs)$ cd SatNOGS
(satnogs)$ ./manage.py syncdb && ./manage.py migrate
```
6 - Create a superuser
```
(satnogs)$ ./manage.py createsuperuser
```
7 - Run development server
```
(satnogs)$ ./manage.py runserver 0.0.0.0:8000
```
Your satnogs-network development instance is available in localhost:8000 . Go hack!

LICENSE: MPL-2.0
