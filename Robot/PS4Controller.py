from pyPS4Controller.controller import Controller

from Robot import Robot


class MyController(Controller):

    def __init__(self, **kwargs):
        self.robot = Robot()
        Controller.__init__(self, **kwargs)

    def on_up_arrow_press(self):
        self.robot.drive_forward()

    def on_down_arrow_press(self):
        self.robot.drive_backward()

    def on_up_down_arrow_release(self):
        self.robot.stop_driving()

    def on_left_arrow_press(self):
        self.robot.turn_left()

    def on_right_arrow_press(self):
        self.robot.turn_right()

    def on_left_right_arrow_release(self):
        self.robot.stop_driving()

    def on_x_press(self):
        self.robot.increase_speed()

    def on_x_release(self):
        pass

    def on_circle_press(self):
        self.robot.decrease_speed()

    def on_circle_release(self):
        pass
