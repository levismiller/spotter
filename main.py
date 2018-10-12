from sanic import Sanic
from sanic.response import json

from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

pan = 13
tilt = 11

GPIO.setup(tilt, GPIO.OUT)
GPIO.setup(pan, GPIO.OUT)

app = Sanic()
app.static('/static', './static')


def set_servo_angle(GPIO, servo, angle):
    pwm = GPIO.PWM(servo, 50)
    pwm.start(8)
    dc = angle / 18. + 3.
    pwm.ChangeDutyCycle(dc)
    sleep(0.3)
    pwm.stop()


def calc_pan(self, lat, lng):
    pass


def calc_tilt(self, distance, alt):
    pass


def calc_zoom(self, lat, lng, alt):
    pass


@app.route('/', methods=['GET'])
async def home(req):
    return json({'msg': 'Default'})


@app.route('/ptz/<pan>/<tilt>/<zoom>', methods=['GET'])
async def ptz(req, pan, tilt, zoom):
    set_servo_angle(GPIO, 13, int(pan))
    set_servo_angle(GPIO, 11, int(tilt))
    return json({
        'success': True,
        'pan': pan,
        'tilt': tilt,
        'zoom': zoom
    })


@app.route('/lla/<lat>/<lng>/<alt>', methods=['GET'])
async def lla(req, lat, lng, alt):
    return json({
        'success': True,
        'lat': lat,
        'lng': lng,
        'alt': alt
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
