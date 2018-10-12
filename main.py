from sanic import Sanic
from sanic.response import json

from app.camera import Camera
# from app.position import CameraPosition

from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

pan = 13
tilt = 11

GPIO.setup(tilt, GPIO.OUT)  # white => TILT
GPIO.setup(pan, GPIO.OUT)  # gray ==> PAN

app = Sanic()
app.static('/static', './static')


class CameraPosition(object):

    def __init__(self, GPIO):
        self.GPIO = GPIO
        self.camera = None

    def set_servo_angle(self, servo, angle):
        pwm = self.GPIO.PWM(servo, 50)
        pwm.start(8)
        dc = angle / 18. + 3.
        if dc < self.camera.servo_range[0]:
            return self.camera.servo_range[0]
        if dc > self.camera.servo_range[-1]:
            return self.camera.servo_range[-1]
        pwm.ChangeDutyCycle(dc)
        sleep(0.3)
        pwm.stop()

    async def moveto_angle(self, pan, tilt):
        pass

    async def moveto(self, lat, lng, alt):
        pass

    async def __move_servo(self, pin, duty_cycle):
        pass

    async def __calc_horz_angle(self, lat, lng):
        pass

    async def __calc_vert_angle(self, distance, alt):
        pass

    async def __calc_distance(self, lat, lng, alt):
        pass

    async def __calc_duty_cycle(self, servo_range, angle):
        pass


cameraPosition = CameraPosition(GPIO)


@app.route('/', methods=['GET'])
async def home(req):
    if cameraPosition.camera:
        return json(cameraPosition.camera.config())
    else:
        return json({'msg': 'No camera configured'})


@app.route('/setup/', methods=['GET'])
async def setup(req):
    if not cameraPosition.camera:
        #     body = await req.json()
        #     pan = body.get('pan_range', [4, 11])
        #     tilt = body.get('tilt_range', [3, 6])
        #     lat = body.get('lat', 0)
        #     lng = body.get('lng', 0)
        #     alt = body.get('alt', 0)
        #     host = body.get('host', None)
        #
        #     if host:
        cam = Camera()
        cam.configure()
        cameraPosition.camera = cam

    if cameraPosition.camera:
        return json(cameraPosition.camera.config())
    else:
        return json({'msg': 'No camera configured'})

@app.route('/gotoangle/<pan>/<tilt>', methods=['GET'])
async def goto_angle(req, pan, tilt):
    cam = Camera()
    cam.configure()
    cameraPosition.camera = cam
    
    if cameraPosition.camera and cameraPosition.camera.active:
        cameraPosition.set_servo_angle(13, int(pan))
        cameraPosition.set_servo_angle(11, int(tilt))

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
    else:
        return json({'msg': 'No camera configured'})


@app.route('/goto/<lat>/<lng>/<alt>', methods=['GET'])
async def goto(req, lat, lng, alt):
    if cameraPosition.camera and cameraPosition.camera.active:
        cameraPosition.moveto(lat, lng, alt)
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
    else:
        return json({'msg': 'No camera configured'})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)



