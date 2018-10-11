from asyncio import sleep
import RPi.GPIO as GPIO

class CameraPosition(object):

    def __init__(self):
        self.pan_servo_pin = 13
        self.tilt_servo_pin = 11
        self.servo_hertz = 50
        self.pulse = 20
        self.camera = None
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.pan_servo_pin, GPIO.OUT)
        GPIO.setup(self.tilt_servo_pin, GPIO.OUT)

    def moveto_angle(self, pan, tilt):
        pan_dc = self.__calc_duty_cycle(self.camera.pan_range, pan)
        tilt_dc = self.__calc_duty_cycle(self.camera.tilt_range, tilt)
        print(pan, tilt, 'pan_dc', pan_dc, 'tilt_dc', tilt_dc)
        self.__move_servo(self.pan_servo_pin, pan_dc)
        self.__move_servo(self.tilt_servo_pin, tilt_dc)

    def moveto(self, lat, lng, alt):
        pass

    def __move_servo(self, pin, duty_cycle):
        pwm = GPIO.PWM(pin, self.servo_hertz)
        pwm.start(0)
        pwm.ChangeDutyCycle(duty_cycle)
        sleep(0.3)
        pwm.stop()

    def __calc_horz_angle(self, lat, lng):
        pass

    def __calc_vert_angle(self, distance, alt):
        pass

    def __calc_distance(self, lat, lng, alt):
        pass

    def __calc_duty_cycle(self, servo_range, angle):
        dc = float(angle) / self.pulse + 2.5
        if dc < servo_range[0]:
            return servo_range[0]
        if dc > servo_range[-1]:
            return servo_range[-1]
        return dc