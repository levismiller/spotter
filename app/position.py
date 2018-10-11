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

    async def moveto_angle(self, pan, tilt):
        pan_dc = await self.__calc_duty_cycle(self.camera.pan_range, pan)
        tilt_dc = await self.__calc_duty_cycle(self.camera.tilt_range, tilt)
        print(pan, tilt, 'pan_dc', pan_dc, 'tilt_dc', tilt_dc)
        await self.__move_servo(self.pan_servo_pin, pan_dc)
        await self.__move_servo(self.tilt_servo_pin, tilt_dc)

    async def moveto(self, lat, lng, alt):
        pass

    async def __move_servo(self, pin, duty_cycle):
        pwm = GPIO.PWM(pin, self.servo_hertz)
        pwm.start(0)
        pwm.ChangeDutyCycle(duty_cycle)
        sleep(0.3)
        pwm.stop()

        # pwm = GPIO.PWM(pin, self.servo_hertz)
        # pwm.start(8)
        # dutyCycle = angle / 18. + 3.
        # pwm.ChangeDutyCycle(dutyCycle)
        # sleep(0.3)
        # pwm.stop()

    async def __calc_horz_angle(self, lat, lng):
        pass

    async def __calc_vert_angle(self, distance, alt):
        pass

    async def __calc_distance(self, lat, lng, alt):
        pass

    async def __calc_duty_cycle(self, servo_range, angle):
        # dc = float(angle) / self.pulse + 2.5
        dc = float(angle) / 18. + 3.
        if dc < servo_range[0]:
            return servo_range[0]
        if dc > servo_range[-1]:
            return servo_range[-1]
        return dc