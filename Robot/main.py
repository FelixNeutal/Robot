import time

from PS4Controller import MyController
from Robot import Robot

if __name__ == '__main__':
    controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
    controller.listen()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
