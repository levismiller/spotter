class Camera(object):

    def __init__(self):
        self.lat = 0
        self.lng = 0
        self.alt = 0
        self.host = ''
        self.pan_range = []
        self.tilt_range = []
        self.zoom = 0
        self.active = False

    def configure(self, pan_range=None, tilt_range=None, lat=0, lng=0, alt=0, host=''):
        if not pan_range:
            pan_range = [4,11]
        if not tilt_range:
            tilt_range = [3,6]

        self.pan_range = pan_range
        self.tilt_range = tilt_range
        self.lat = lat
        self.lng = lng
        self.alt = alt
        self.host = host
        self.active = True

    def remove(self):
        self.lat = 0
        self.lng = 0
        self.alt = 0
        self.host = ''
        self.pan_range = []
        self.tilt_range = []
        self.zoom = 0
        self.active = False

    def config(self):
        return {
            'active': self.active,
            'lat': self.lat,
            'lng': self.lng,
            'alt': self.alt,
            'pan': self.pan_range,
            'tilt': self.tilt_range,
            'host': self.host,
            'zoom': self.zoom
        }
