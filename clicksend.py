import time
from interception import *
from consts import *

context = interception()

mouse = 0

for i in range(MAX_DEVICES):
    if interception.is_mouse(i):
        mouse = i
        break


class KeyboardDriver:
    def __init__(self):
        self.driver = interception()
        self.keyboard = self.keyboard_driver()

    def keyboard_driver(self):
        for i in range(MAX_DEVICES):
            if interception.is_keyboard(i):
                return i
        return None

    def tusbas(self, key, gecikme):
        interception_press = key_stroke(key, interception_key_state.INTERCEPTION_KEY_DOWN.value, 0)
        self.driver.send(self.keyboard, interception_press)
        time.sleep(gecikme)
        interception_press.state = interception_key_state.INTERCEPTION_KEY_UP.value
        self.driver.send(self.keyboard, interception_press)


class MouseDriver:
    def leftclick(self, sleep):
        # interception_mouse_flag.INTERCEPTION_MOUSE_MOVE_ABSOLUTE.value, ile mouse hareket ettirebilirsiniz.
        mstroke = mouse_stroke(
            interception_mouse_state.INTERCEPTION_MOUSE_LEFT_BUTTON_DOWN.value,
            interception_mouse_flag.INTERCEPTION_MOUSE_MOVE_ABSOLUTE.value,
            0,
            27306,
            48544,
            0,
        )
        context.send(mouse, mstroke)
        time.sleep(sleep)
        mstroke.state = interception_mouse_state.INTERCEPTION_MOUSE_LEFT_BUTTON_UP.value
        context.send(mouse, mstroke)

    def rightclick(self, sleep):
        mstroke = mouse_stroke(interception_mouse_state.INTERCEPTION_MOUSE_RIGHT_BUTTON_DOWN.value, 0, 0, 0, 0, 0)
        context.send(mouse, mstroke)
        time.sleep(sleep)
        mstroke.state = interception_mouse_state.INTERCEPTION_MOUSE_RIGHT_BUTTON_UP.value
        context.send(mouse, mstroke)

    def mouse_left_down(self):
        interception_press = mouse_stroke(
            interception_mouse_state.INTERCEPTION_MOUSE_LEFT_BUTTON_DOWN.value, 0, 0, 0, 0, 0
        )
        context.send(self.mouse, interception_press)

    def mouse_left_up(self):
        interception_up = mouse_stroke(interception_mouse_state.INTERCEPTION_MOUSE_LEFT_BUTTON_UP.value, 0, 0, 0, 0, 0)
        context.send(self.mouse, interception_up)

    def mouse_right_down(self):
        interception_press = mouse_stroke(
            interception_mouse_state.INTERCEPTION_MOUSE_RIGHT_BUTTON_DOWN.value, 0, 0, 0, 0, 0
        )
        context.send(mouse, interception_press)

    def mouse_right_up(self):
        interception_up = mouse_stroke(interception_mouse_state.INTERCEPTION_MOUSE_RIGHT_BUTTON_UP.value, 0, 0, 0, 0, 0)
        context.send(mouse, interception_up)
