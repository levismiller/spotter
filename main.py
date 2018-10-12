from sanic import Sanic
from sanic.response import json
from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

pan_servo = {
    'pin': 11,
    'range': [4, 11]
}

tilt_servo = {
    'pin': 11,
    'range': [3, 6]
}

GPIO.setup(tilt_servo['pin'], GPIO.OUT)
GPIO.setup(pan_servo['pin'], GPIO.OUT)

app = Sanic()
app.static('/static', './static')


def set_servo_angle(servo, angle):
    print(int(servo['pin']))
    # pwm = GPIO.PWM(servo['pin'], 50)
    # pwm.start(8)
    # dc = angle / 18. + 3.
    # if dc < servo['range'][0]:
    #     return servo['range'][0]
    # if dc > servo['range'][-1]:
    #     return servo['range'][-1]
    # pwm.ChangeDutyCycle(dc)
    # sleep(0.3)
    # pwm.stop()


def move_to(lat, lng, alt):
    pass


def __calc_pan_angle(lat, lng):
    pass


def __calc_tilt_angle(distance, alt):
    pass


def __calc_distance(lat, lng, alt):
    pass


@app.route('/gotoangle/<pan>/<tilt>', methods=['GET'])
async def goto_angle(req, pan, tilt):
    set_servo_angle(pan_servo, int(pan))
    set_servo_angle(tilt_servo, int(tilt))

    return json({
        'success': True,
        'lat': 0,
        'lng': 0,
        'alt': 0,
        'pan': 0,
        'tilt': 0,
        'range': 0,
        'zoom': 0
    })


@app.route('/goto/<lat>/<lng>/<alt>', methods=['GET'])
async def goto(req, lat, lng, alt):
    move_to(lat, lng, alt)
    return json({
        'success': True,
        'lat': 0,
        'lng': 0,
        'alt': 0,
        'pan': 0,
        'tilt': 0,
        'range': 0,
        'zoom': 0
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
