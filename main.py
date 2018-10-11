from sanic import Sanic
from sanic.response import json

from app.camera import Camera
from app.position import CameraPosition

app = Sanic()
app.static('/static', './static')

cameraPosition = CameraPosition()


@app.route('/', methods=['GET'])
async def home(req):
    if cameraPosition.camera:
        return json(cameraPosition.camera.config())
    else:
        return json({'msg': 'No camera configured'})


@app.route('/setup/', methods=['POST'])
async def setup(req):
    if not cameraPosition.camera:
        body = await req.json()
        pan = body.get('pan_range', [4, 11])
        tilt = body.get('tilt_range', [3, 6])
        lat = body.get('lat', 0)
        lng = body.get('lng', 0)
        alt = body.get('alt', 0)
        host = body.get('host', None)

        if host:
            cam = Camera()
            cam.configure(pan, tilt, lat, lng, alt, host)
            cameraPosition.camera = cam

    if cameraPosition.camera:
        return json(cameraPosition.camera.config())
    else:
        return json({'msg': 'No camera configured'})


@app.route('/goto/<lat>/<lng>/<alt>', methods=['GET'])
async def goto(req, lat, lng, alt):
    if cameraPosition.camera and cameraPosition.camera.active:
        body = await req.json()
        lat = body.get('lat', 0)
        lng = body.get('lng', 0)
        alt = body.get('alt', 0)
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
