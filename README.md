# sensors-monitor
Application for monitoring sensors readings, currently with light, temperature and humidity measurements.

## Modules
### API
A python application that constantly acquires sensors data and store them in a MongoDB database and then provide these data via a RESTful API.
#### Requirements
* [Python](https://www.python.org/)
  * [Flask](http://flask.pocoo.org/)
  * [Flask-Cors](http://flask-cors.readthedocs.org/en/latest/)
  * [Flask-PyMongo](http://flask-pymongo.readthedocs.org/en/latest/)
  * [pymongo](http://api.mongodb.org/python/current/)
  * [pyserial](https://pyserial.readthedocs.org/en/latest/)
* [MongoDB](https://www.mongodb.org/)

#### Setup and Run
* Install the requirements (Tip: use [pip](https://pip.pypa.io/en/stable/) to install the python packages)
* Execute:
  ```
  $ python api/sensors_api.py
  ```
  
### Sensors Module AVR
Uses an AVR microcontroller to interact with the sensors and provide the measured values via serial communication.
#### Requirements
* [avr-gcc](https://gcc.gnu.org/)
* [avrdude](http://savannah.nongnu.org/projects/avrdude)
* [AVR Libc](http://www.nongnu.org/avr-libc/)
* [AVR-Util](https://github.com/CELTAB/AVR-Util)

### WEB Interface
A WEB interface for plotting the datas as graphics and print them in PDF format.
