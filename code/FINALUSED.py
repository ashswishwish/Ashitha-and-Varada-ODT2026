# =================================================================
#  ESP32 BLE GAMEPAD — Dual Joystick + STABLE NeoPixel (NO BLINK)
#  Buttons removed | F mapped to right joystick UP
# =================================================================

from machine import Pin, ADC
import neopixel, time, struct
from ble_keyboard import BLEKeyboard


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  CONFIGURATION
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PIN_JOY_X    = 32
PIN_JOY_Y    = 33
PIN_JOY2_X   = 34
PIN_JOY2_Y   = 35

PIN_NEO      = 14
NUM_PIXELS   = 90

DEADZONE     = 600
LOOP_MS      = 20
CAL_SAMPLES  = 30
INVERT_X     = False
INVERT_Y     = True

DEVICE_NAME  = "ESP32_Gamepad"

# ── HID keycodes ──
KEY_W = 26
KEY_A = 4
KEY_S = 22
KEY_D = 7
KEY_H = 11
KEY_L = 15
KEY_J = 13
KEY_F = 9

# ── Colours ──
COL_OFF     = (0, 0, 0)
COL_IDLE    = (255, 255, 255)
COL_WAITING = (255, 255, 255)
COL_WS      = (255, 210, 0)
COL_AD      = (255, 80,  0)
COL_FLIP    = (160, 0,   255)
COL_DASH    = (0,   255, 255)
COL_FIRE    = (0,   255, 0)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  BLE KEYBOARD
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

class BLEKbdHold(BLEKeyboard):
    def send_hold(self, keycodes, modifier=0):
        ks = list(keycodes)[:6]
        while len(ks) < 6:
            ks.append(0)
        self._send(struct.pack("8B", modifier, 0, *ks))


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  NEOPIXEL — SOLID (NO BLINK)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

class NeoController:
    def __init__(self, pin, n):
        self.np     = neopixel.NeoPixel(Pin(pin), n)
        self.n      = n
        self.colour = None   # track last state

    def set(self, colour):
        # Only update LEDs if colour actually changed
        if colour != self.colour:
            self.colour = colour
            self.show()

    def show(self):
        for i in range(self.n):
            self.np[i] = self.colour
        self.np.write()

    def startup_flash(self):
        for col in [(255,0,0),(255,140,0),(0,255,0),(0,0,255),(160,0,255)]:
            for i in range(self.n):
                self.np[i] = col
            self.np.write()
            time.sleep_ms(120)
        self.set(COL_OFF)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  JOYSTICK (NO BUTTON)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

class Joystick:
    def __init__(self, pin_x, pin_y, deadzone,
                 invert_x=False, invert_y=False):
        self.adc_x = ADC(Pin(pin_x))
        self.adc_y = ADC(Pin(pin_y))
        self.adc_x.atten(ADC.ATTN_11DB)
        self.adc_y.atten(ADC.ATTN_11DB)
        self.deadzone = deadzone
        self.invert_x = invert_x
        self.invert_y = invert_y
        self.center_x = 2048
        self.center_y = 2048

    def calibrate(self):
        sx, sy = 0, 0
        for _ in range(CAL_SAMPLES):
            sx += self.adc_x.read()
            sy += self.adc_y.read()
            time.sleep_ms(10)
        self.center_x = sx // CAL_SAMPLES
        self.center_y = sy // CAL_SAMPLES

    def read(self):
        dx = self.adc_x.read() - self.center_x
        dy = self.adc_y.read() - self.center_y
        if self.invert_x: dx = -dx
        if self.invert_y: dy = -dy
        x_dir = 1 if dx > self.deadzone else (-1 if dx < -self.deadzone else 0)
        y_dir = 1 if dy > self.deadzone else (-1 if dy < -self.deadzone else 0)
        return (x_dir, y_dir)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  GAMEPAD
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

class Gamepad:
    def __init__(self, js1, js2, keyboard, neo):
        self.js1 = js1
        self.js2 = js2
        self.kbd = keyboard
        self.neo = neo
        self.last_keys = frozenset()

    def update(self):
        x1, y1 = self.js1.read()
        x2, y2 = self.js2.read()

        keys = set()

        # ── Left stick: WASD ──────────────────────
        if   x1 > 0: keys.add(KEY_D)
        elif x1 < 0: keys.add(KEY_A)
        if   y1 > 0: keys.add(KEY_W)
        elif y1 < 0: keys.add(KEY_S)

        # ── Right stick: H/L/J + F ────────────────
        if   x2 < 0: keys.add(KEY_H)
        elif x2 > 0: keys.add(KEY_L)
        if   y2 < 0: keys.add(KEY_J)
        elif y2 > 0: keys.add(KEY_F)

        current = frozenset(keys)

        if current != self.last_keys:
            self.kbd.send_hold(current)
            self.last_keys = current
            self._pick_colour(keys)
            self._log(current)

    def _pick_colour(self, keys):
        if   KEY_F in keys:                    self.neo.set(COL_FIRE)
        elif KEY_J in keys:                    self.neo.set(COL_DASH)
        elif KEY_H in keys or KEY_L in keys:   self.neo.set(COL_FLIP)
        elif KEY_W in keys or KEY_S in keys:   self.neo.set(COL_WS)
        elif KEY_A in keys or KEY_D in keys:   self.neo.set(COL_AD)
        else:                                  self.neo.set(COL_IDLE)

    def _log(self, keys):
        names = {
            KEY_W:"W", KEY_A:"A", KEY_S:"S", KEY_D:"D",
            KEY_H:"H", KEY_L:"L", KEY_J:"J", KEY_F:"F",
        }
        held = [names.get(k, "?") for k in keys]
        print("keys:", "+".join(held) if held else "(released)")


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  MAIN
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def main():
    print("ESP32 BLE Gamepad (Stable LEDs)")

    neo = NeoController(PIN_NEO, NUM_PIXELS)
    neo.startup_flash()

    kbd = BLEKbdHold(DEVICE_NAME)

    time.sleep_ms(500)

    js  = Joystick(PIN_JOY_X,  PIN_JOY_Y,  DEADZONE, INVERT_X, INVERT_Y)
    js2 = Joystick(PIN_JOY2_X, PIN_JOY2_Y, DEADZONE, INVERT_X, INVERT_Y)
    js.calibrate()
    js2.calibrate()

    # ── Waiting for BLE connection (NO BLINK) ──
    while not kbd.is_connected():
        neo.set(COL_WAITING)
        time.sleep_ms(LOOP_MS)

    neo.set(COL_IDLE)

    gamepad = Gamepad(js, js2, kbd, neo)

    while True:
        if kbd.is_connected():
            gamepad.update()
        else:
            neo.set(COL_WAITING)

        time.sleep_ms(LOOP_MS)


main()