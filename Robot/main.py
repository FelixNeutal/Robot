import time

from Robot import Robot

if __name__ == '__main__':
    robot = Robot()
    robot.drive_forward()
    time.sleep(10)
    robot.stop_driving()
    time.sleep(2)
    robot.drive_backward()
    time.sleep(10)
    robot.stop_driving()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
