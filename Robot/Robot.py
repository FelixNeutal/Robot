from adafruit_motorkit import MotorKit


class Robot:
    def __init__(self):
        self.kit = MotorKit()
        self.left_motor = self.kit.motor1
        self.right_motor = self.kit.motor4

    def drive_left_motor(self, direction="FORWARD"):
        if direction == "FORWARD":
            self.left_motor.throttle = 1
        else:
            self.left_motor.throttle = -1

    def drive_right_motor(self, direction="FORWARD"):
        if direction == "FORWARD":
            self.right_motor.throttle = 1
        else:
            self.right_motor.throttle = -1

    def drive_forward(self):
        self.drive_left_motor("FORWARD")
        self.drive_right_motor("FORWARD")

    def drive_backward(self):
        self.drive_left_motor("BACKWARD")
        self.drive_right_motor("BACKWARD")

    def stop_driving(self):
        self.left_motor.throttle = 0
        self.right_motor.throttle = 0