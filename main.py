from sanic import Sanic
from sanic.response import json

from time import sleep
import RPi.GPIO as GPIO

app = Sanic()
app.static('/static', './static')

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

servos = {
    'pan': {
        'pin': 13,
        'range': [4, 11]
    },
    'tilt': {
        'pin': 11,
        'range': [3, 6]
    }
}

GPIO.setup(servos['tilt']['pin'], GPIO.OUT)
GPIO.setup(servos['pan']['pin'], GPIO.OUT)


def set_servo_angle(GPIO, servo, angle):
    pwm = GPIO.PWM(servo['pin'], 50)
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
    set_servo_angle(GPIO, servos['pan'], float(pan))
    set_servo_angle(GPIO, servos['tilt'], float(tilt))
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
