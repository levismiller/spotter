class Camera(object):

    def __init__(self):
        self.lat = 0
        self.lng = 0
        self.alt = 0
        self.host = ''
        self.pan = 0
        self.tilt = 0
        self.zoom = 0
        self.active = False

    def configure(self, lat=0, lng=0, alt=0, host=''):
        self.lat = lat
        self.lng = lng
        self.alt = alt
        self.host = host
        self.active = True

    def remove(self):
        self.active = False
        self.host = None
        self.pan = None
        self.tilt = None

    def config(self):
        return {
            'active': self.active,
            'lat': self.lat,
            'lng': self.lng,
            'alt': self.alt,
            'pan': self.pan,
            'tilt': self.tilt,
            'host': self.host,
            'zoom': self.zoom
        }
