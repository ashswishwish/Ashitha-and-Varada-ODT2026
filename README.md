# Open Design and Technology  
## Final Project README

> **Project Weight:** 70%  
> **Team Size:** 2 students  
> **Project Duration:** 4 weeks  
> **Class Time Available:** 6 hours per class  
> **Total Time Available:** 48 effort-hours per team  
> **Project Type:** Playful, interactive, technology-based experience

---

# Before you begin

## Fork and rename this repository
After forking this repository, rename it using the format:

`ODT-2026-TeamName`

### Example
`ODT-2026-PixelWizards`

Do not keep the default repository name.

---

# How to use this README

This file is your team’s **working project document**.

You must keep updating it throughout the 4-week build period.  
By the final review, this README should clearly show:
- your idea,
- your planning,
- your design decisions,
- your technical process,
- your build progress,
- your testing,
- your failures and changes,
- your final outcome.

## Rules
- Fill every section.
- Do not delete headings.
- If something does not apply, write `Not applicable` and explain why.
- Add images, screenshots, sketches, links, and videos wherever useful.
- Update task status and weekly logs regularly.
- Use this file as evidence of process, not only as a final report.

---

# 1. Team Identity

## 1.1 Studio / Group Name
`[ESP-EATERS]`

## 1.2 Team Members

| Name | Primary Role | Secondary Role | Strengths Brought to the Project |
|---|---|---|---|
| `Ashitha Ashok` | `[Coding / App]` | `[Electronics]` | `[Strong logic building, UI thinking, integration]` |
| `Varada Supanekar` | `[Electronics / Fabrication]` | `[Mechanics]` | `[Circuit design, physical prototyping]` |

## 1.3 Project Title
`[Batman Dodge]`

## 1.4 One-Line Pitch
`A fast-paced pixel-art Batman game controlled by a hand-built ESP32 dual-joystick console that transmits inputs wirelessly over BLE and lights up a NeoPixel in real time to mirror every in-game action.`

## 1.5 Expanded Project Idea
In 1–2 paragraphs, explain:
- what your project is,
- what kind of playful experience it creates,
- what makes it fun, curious, engaging, strange, satisfying, competitive, or delightful,
- what technologies are involved.

**Response:**  
`The project is a 2D pixel-art game (BATMANNER) where Batman navigates a city landscape, dodging obstacles and enemies. All player input comes from a custom physical console built around an ESP32 microcontroller with two HW-504 analogue joysticks. The console pairs to the game host over Bluetooth Low Energy, appearing as a standard HID keyboard so no special drivers are needed.
The experience combines embodied physical control with reactive lighting feedback. A single WS2812B NeoPixel breathes continuously and changes colour in real time based on which action is being performed — yellow for movement, orange for strafing, cyan for dash, green for fire, red for pause — creating an immediate sensory link between what the player does physically and what happens on screen. This makes the console feel alive, not just functional.`

---

# 2. Philosophy Fit

## 2.1 Experience, Not Social Problem
This module does **not** require your project to solve a large social problem.

You are allowed to build:
- toys,
- games,
- interactive objects,
- playful machines,
- kinetic artifacts,
- humorous devices,
- strange but delightful experiences,
- things that are entertaining to use or watch.

## 2.2 What kind of experience are you creating?
Answer the following:
- What is the experience?
- What do you want the player or participant to feel?
- Why would someone want to try it again?

**Response:**  
`[- Experience: A reflex-based arcade dodging game played through a hand-held physical console with live colour feedback on every action.
- Feeling: rgency and presence — the glowing controller makes it feel like the hardware itself is reacting, not just the screen.
- Replay value: Increasing difficulty, score competition, and the tactile satisfaction of the joystick + light response loop make each run feel immediate and replayable]`

## 2.3 Design Persona
Complete the sentence below:

> We are designing this project as if we are a small creative studio making a **[toy / game / playable object / interactive experience]** for **[children / teens / adults / classmates / exhibition visitors / mixed audience]**.

**Response:**  
`[We are designing this project as if we are a small creative studio making a game / interactive experience for teens and exhibition visitors.]`

---

# 3. Inspiration

## 3.1 References
List what inspired the project.

| Source Type | Title / Link | What Inspired You |
|---|---|---|
| `[Video Game]` | `[Flappy Bird]` | `[Simple but addictive loop]` |
| `[Video Game]` | `[Jetpack Joyride]` | `[Continuous motion gameplay]` |
| `[Visual Style]` | `[Pixel Art Games]` | `[Minimal but expressive visuals]` |
| `[Hardware Project]` | `[DIY Arduino gamepads]` | `[Joystick-to-BLE keyboard mapping concept]` |

## 3.2 Original Twist
What makes your project original?

**Response:**  
`[Most physical game controllers are generic. Here, the NeoPixel on the controller is wired directly into the game's action logic — it breathes white at rest, turns cyan on a dash, green on fire, red on ESC — so the controller itself narrates the game state. Combined with the one-way mirror installation, this creates a hybrid physical-digital experience that a phone or standard gamepad cannot replicate.]`

---

# 4. Project Intent

## 4.1 Core Interaction Loop
Describe the main loop of interaction.

Examples:
- press → launch → score → reset
- connect → control → observe → repeat
- turn → trigger → react → repeat
- move object → sensor detects → sound/light response → player reacts

**Response:**  
`[move joystick → ESP32 reads ADC → BLE keyboard report sent → game character responds → NeoPixel colour changes → player reacts → repeat]`

## 4.2 Intended Player / Audience

| Question | Response |
|---|---|
| Who is this for? | `[Students / exhibition visitors]` |
| Age range | `[10–25]` |
| Solo or multiplayer | `[Solo]` |
| Expected duration of one round | `[30–60 seconds per round]` |
| What should the player feel? | `[Tension and excitement]` |
| Is explanation required before use? | `[Minimal]` |

## 4.3 Player Journey
Describe exactly how a player will use the project.

1. **Approach:** `[Player walks up to what appears to be a normal mirror in a dark frame.]`
2. **Start:** `[Light sensor detects presence; game activates and becomes visible through the one-way mirror. Player picks up the ESP32 console]`
3. **First Action:** `[Batman begins moving automatically. Player pushes the left joystick to steer, NeoPixel turns yellow (W/S) or orange (A/D) instantly.]`
4. **Main Interaction:** `[Player steers Batman with the left stick (WASD), uses the right stick to flip direction (H/L), dash downward (J), and fires with the right button (F). The NeoPixel cycles through cyan, green, purple, orange in direct response.]`
5. **System Response:** `[All 4 lives lost → game over screen visible through the mirror..]`
6. **Win / Lose / End Condition:** `[How does one round end?]`
7. **Reset:** `[Game resets automatically or on player input; mirror returns to idle reflection state.]`

## 4.4 Rules of Play
If your project is a game, list the rules clearly.

- `[Batman moves continuously; the player must steer and dodge.]`
- `[Left joystick controls directional movement (W=up, S=down, A=left, D=right).]`
- `[Right joystick left/right triggers a directional flip (H / L keys).]`
- `[Right joystick pushed down triggers a dash (J key).]`
- `[Right joystick button fires (F key) , Left joystick button pauses / opens menu (ESC key).]`
- `[Player has 4 lives; losing all lives ends the round.]`
- `[Difficulty increases progressively with each level.]`



---

# 5. Definition of Success

## 5.1 Definition of “Playable”
Your project will be considered complete only if these conditions are met.

- [ ] `[he mirror convincingly appears as a normal reflective surface when idle and transitions clearly into a game display when activated.]`
- [ ] `[Players are able to understand and start interacting with the system with minimal instructions.]`
- [ ] `[Joystick controls feel responsive and allow smooth movement, attack, and dash actions (BLE loop runs at 50 Hz / 20 ms per cycle; deadzone set to 600/4095 ADC units).]`
- [ ] `[The game provides a progressively challenging and replayable experience across multiple lives and levels.]`
- [ ] `[NeoPixel lighting responds instantly and meaningfully to in-game actions — colour changes occur within the same 20 ms loop tick as the keypress.]`

## 5.2 Minimum Viable Version
What is the smallest version of this project that still delivers the core experience?

**Response:**  
`[A hand-held ESP32 console with both joysticks, and BLE keyboard pairing, running the BATMANNER game on an iPad. Core loop is: move, dodge, fire, lose a life — with NeoPixel confirming each action in colour.]`

## 5.3 Stretch Features
What features are nice to have but not essential?

- `[One-way mirror installation frame with internal LED ambient lighting.]`
- `[Light-sensor proximity trigger to auto-wake the game when a player approaches.]`
- `[Score leaderboard displayed on the mirror frame after each round.]`

---

# 6. System Overview

## 6.1 Project Type
Check all that apply.

- [0] Electronics-based
- [ ] Mechanical
- [0] Sensor-based
- [0] App-connected
- [ ] Motorized
- [ ] Sound-based
- [0] Light-based
- [0] Screen/UI-based
- [0] Fabricated structure
- [0] Game logic based
- [0] Installation / tabletop experience
- [ ] Other: `[Write here]`

## 6.2 High-Level System Description
Explain how the system works in simple terms.

Include:
- input,
- processing,
- output,
- physical structure,
- app interaction if any.

**Response:**  
`[The ESP32 reads two analogue HW-504 joysticks (4 ADC channels + 2 digital button pins) at 50 Hz. On each loop, it compares the deflection against a calibrated centre value and a deadzone of 600 ADC units (out of 4095). If a direction is active, it assembles a 6-key HID keyboard report and sends it over BLE using the BLEKbdHold class, which holds keys down for as long as the stick is deflected — matching how a keyboard game expects input. Simultaneously, the NeoPixel breathes using a triangle-wave brightness function and changes colour based on which keys are active, with a 12-loop (~240 ms) linger so colours do not snap off the moment a stick returns to centre. The game (BATMANNER, built in GDevelop) runs on an iPad and receives keyboard events from the ESP32 as if they came from a standard Bluetooth keyboard.]`

## 6.3 Input / Output Map

| System Part | Type | What It Does |
|---|---|---|
| `[Joystick #1 and #2]` | Input | `[Left stick: W/A/S/D movement + ESC on click and Right stick: H/L flip, J dash, F fire on click ]` |
| `[ESP32 / Controller]` | Processing | `[Samples analog input via ADC, applies deadzone filtering and calibration, and packages the processed data into BLE HID reports for transmission.]` |
| `[WS2812B NeoPixel]` | Output | `[Breathing colour feedback: white=idle, yellow=W/S, orange=A/D, cyan=J, green=F, purple=H/L, red=ESC]` |
| `[iPad running GDevelop game]` | Processing | `[Receives BLE keyboard events, runs all game logic and rendering]` |

---

# 7. Sketches and Visual Planning

## 7.1 Concept Sketch
Add an early sketch of the full idea.

**Insert image below:**  
`[Upload image and link here]`

Example:
```md

```

## 7.2 Labeled Build Sketch
Add a sketch with labels showing:
- structure,
- electronics placement,
- user touch points,
- moving parts,
- output elements.

**Insert image below:**  
`[Upload image and link here]`

## 7.3 Approximate Dimensions

| Dimension | Value |
|---|---|
| Length | `[~160 mm]` |
| Width | `[~90 mm]` |
| Height | `[~35 mm (enclosure with joystick caps)]` |
| Estimated weight | `[~180 g (with enclosure)]` |

---

# 8. Mechanical Planning

## 8.1 Mechanical Features
Check all that apply.

- [ ] Gears
- [ ] Pulleys
- [ ] Belt drives
- [ ] Linkages
- [ ] Hinges
- [ ] Shafts
- [ ] Springs
- [ ] Bearings
- [ ] Wheels
- [ ] Sliders
- [ ] Levers
- [x] Not applicable

## 8.2 Mechanical Description
Describe the mechanism and what it is meant to do.

**Response:**  
`[The controller enclosure houses the ESP32, two HW-504 joystick modules, a NeoPixel LED, and wiring. The joystick shafts protrude through cut holes on the top face. The enclosure uses a hinged or snap-fit lid for access to electronics during development. The one-way mirror frame is a separate standing structure that holds the iPad behind an acrylic one-way mirror panel.]`

## 8.3 Motion Planning
If something moves, explain:
- what moves,
- what causes the movement,
- how far it moves,
- how fast it moves,
- what could go wrong.

**Response:**  
`[What moves: The joystick thumbsticks move mechanically on X and Y axes; the potentiometer inside the module converts this to a variable resistance read by the ESP32 ADC.
Cause: Thumb pressure from the player.
Range: Each axis sweeps 0–4095 ADC counts; the centre is calibrated at startup (30-sample average, typically ~1900–2100). The deadzone of 600 counts means deflection must exceed ~15% of full range before a keypress registers.
Speed: ADC is sampled every 20 ms (50 Hz loop).
What could go wrong: Joystick drift if the module is bumped during calibration; ADC noise on GPIO 34/35 (input-only pins on ESP32, no internal pull-up — ensure 3.3V supply is stable).]`

## 8.4 Simulation / CAD / Animation Before Making
If your project includes mechanical motion, document the digital planning before fabrication.

| Tool Used | File / Link | What Was Tested |
|---|---|---|
| `[Illustrator]` | `[Link or screenshot]` | `[Enclosure dimensions and joystick hole placement]` |
| `[Gdev]` | `[Link or screenshot]` | `[Basic ADC read and NeoPixel output before physical assembly]` |

## 8.5 Changes After Digital Testing
What changed after the CAD, animation, or simulation stage?

**Response:**  
`[Joystick hole spacing was adjusted after the first mdf mock-up — the original spacing made two-thumb operation uncomfortable. Final spacing: 80 mm centre-to-centre.]`

---

# 9. Electronics Planning

## 9.1 Electronics Used

| Component | Quantity | Purpose |
|---|---:|---|
| `[ESP32]` | `1` | `[Main controller]` |
| `[ Dual-Axis Joystick Module]` | `[2]` | `[Analogue X/Y input + digital push-button]` |
| `[WS2812B NeoPixel LED]` | `[1]` | `[RGB action-colour breathing feedback]` |
| `[Dupont jumper wires (M-M, M-F)]` | `[1]` | `[connecting wires]` |
| `[Micro-USB cable]` | `[1]` | `[Power and MicroPython flashing]` |
| `[Breadboard / PCB]` | `[1]` | `[Prototyping connections]` |



## 9.2 Wiring Plan
Describe the main electrical connections.

**Response:**  
`[Left Joystick (HW-504 #1):

VCC → ESP32 3.3V
GND → ESP32 GND
VRx → GPIO 32 (ADC1_CH4)
VRy → GPIO 33 (ADC1_CH5)
SW  → GPIO 25 (PULL_UP enabled in code)

Right Joystick (HW-504 #2):

VCC → ESP32 3.3V
GND → ESP32 GND
VRx → GPIO 34 (ADC1_CH6, input-only)
VRy → GPIO 35 (ADC1_CH7, input-only)
SW  → GPIO 26 (PULL_UP enabled in code)

NeoPixel:

VCC → ESP32 VIN (5V from USB)
GND → ESP32 GND
DIN → 300 Ω resistor → GPIO 2


Note: GPIO 34 and 35 are input-only on the ESP32 — do not try to use them as outputs. Internal pull-ups are not available on these pins; the joystick button uses GPIO 25 and 26 which support PULL_UP.]`

## 9.3 Circuit Diagram
Insert a hand-drawn or software-made circuit diagram.

**Insert image below:**  
`[Upload image and link here]`

## 9.4 Power Plan

| Question | Response |
|---|---|
| Power source | `[ 3.7V battery]` |
| Voltage required | `[5V for NeoPixel VCC; 3.3V (regulated on board) for ESP32 logic and joysticks]` |
| Current concerns | `[NeoPixel at full white draws ~60 mA; ESP32 + BLE ~240 mA peak; total under 400 mA — safe for USB]` |
| Safety concerns | `[NeoPixel power spike on startup; mitigated by 100 µF capacitor across VCC/GND. GPIO 34/35 are 3.3V-max — do not connect 5V signals.]` |

---

# 10. Software Planning

## 10.1 Software Tools

| Tool / Platform | Purpose |
|---|---|
| `[MicroPython]` | `[Main controller firmware — ADC reading, BLE HID, NeoPixel control]` |
| `[Gdevelop]` | `[Game devloper for BATMANOR — handles all gameplay logic, collision, lives, levels]` |
| `[ble_keyboard.py library]` | `[BLE HID keyboard abstraction used by the ESP32 firmware]` |
| `[Thonny IDE]` | `[Flash and run MicroPython scripts on the ESP32]` |


## 10.2 Software Logic
Describe what the code must do.

Include:
- startup behavior,
- input handling,
- sensor reading,
- decision logic,
- output behavior,
- communication logic,
- reset behavior.

**Response:**  
`[Startup:

NeoPixel runs a 5-colour startup flash (R→Y→G→B→Purple) to confirm wiring.
BLE advertising begins; NeoPixel breathes white (COL_WAITING) until paired.
Both joysticks are calibrated: 30 ADC samples are averaged to find the resting centre on each axis. No sticks should be touched during this phase.

Main loop (20 ms / 50 Hz):

Read left joystick: ADC on GPIO 32 (X) and GPIO 33 (Y), subtract calibrated centre, apply deadzone (±600 counts). Map result to KEY_W/A/S/D. Read button on GPIO 25 → KEY_ESC.
Read right joystick: ADC on GPIO 34 (X) and GPIO 35 (Y), subtract calibrated centre, apply deadzone. Map X-left → KEY_H, X-right → KEY_L, Y-down → KEY_J. Read button on GPIO 26 → KEY_F.
Compare current key set to previous. If changed, send a new 8-byte BLE HID report (modifier + 0 + 6 keycodes, packed with struct.pack("8B")).
Pick NeoPixel colour by priority: F (green) > ESC (red) > J (cyan) > H/L (purple) > W/S (yellow) > A/D (orange) > idle (white). After release, linger colour holds for 12 loops (~240 ms) before fading to white.
Advance the breathing triangle wave one step (±1/40 per loop, reversing at min/max brightness 0.10–1.00).
If BLE disconnects mid-session, NeoPixel returns to COL_WAITING and the loop continues waiting for reconnection.

Reset: No explicit reset needed — releasing all inputs sends a zero-key HID report; game handles its own round reset on life loss.]`

## 10.3 Code Flowchart


Suggested sequence:
- start,
- initialize,
- wait for input,
- read input,
- decision,
- trigger output,
- repeat or reset,
- error handling.

**Insert image below:**  
`[<img width="447" height="728" alt="image" src="https://github.com/user-attachments/assets/43b8e711-de0a-493b-915b-2396dcb2e5db" />
]`

## 10.4 Pseudocode

```text
[# =================================================================
#  ESP32 BLE GAMEPAD — Dual Joystick + Breathing NeoPixel
#
#  File: gamepad_test.py
#  Run from Thonny with F5. Stop with Ctrl+C.
#  Requires: ble_keyboard.py in same directory (unchanged)
#
#  Wiring (HW-504 #1 — left, WASD + ESC):
#    VCC -> 3.3V, GND -> GND
#    VRx -> GPIO 32, VRy -> GPIO 33, SW -> GPIO 25
#
#  Wiring (HW-504 #2 — right, H/L/J + F):
#    VCC -> 3.3V, GND -> GND
#    VRx -> GPIO 34, VRy -> GPIO 35, SW -> GPIO 26
#
#  Wiring (NeoPixel):
#    VCC -> 5V (VIN pin), GND -> GND, DIN -> GPIO 2
# =================================================================

from machine import Pin, ADC
import neopixel, time, struct
from ble_keyboard import BLEKeyboard


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  CONFIGURATION
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# ── Joystick pins ──
PIN_JOY_X    = 32          # left stick X
PIN_JOY_Y    = 33          # left stick Y
PIN_JOY_BTN  = 25          # left click  → ESC
PIN_JOY2_X   = 34          # right stick X  → H / L
PIN_JOY2_Y   = 35          # right stick Y  → J (down)
PIN_JOY2_BTN = 26          # right click → F (fire)

# ── NeoPixel ──
PIN_NEO      = 2            # try GPIO2 if GPIO4 didn't work
NUM_PIXELS   = 1            # ← set this to however many LEDs you have

# ── Joystick behaviour ──
DEADZONE     = 600
LOOP_MS      = 20
CAL_SAMPLES  = 30
INVERT_X     = False
INVERT_Y     = True

DEVICE_NAME  = "ESP32_Gamepad"

# ── HID keycodes ──
KEY_W        = 26
KEY_A        = 4
KEY_S        = 22
KEY_D        = 7
KEY_ESC      = 41           # left click
KEY_H        = 11           # right stick left  — flip left
KEY_L        = 15           # right stick right — flip right
KEY_J        = 13           # right stick down  — dash
KEY_F        = 9            # right click       — fire

# ── Colours (R, G, B) at full brightness ──
COL_WAITING  = (80,  80,  80)   # white  — not yet paired
COL_IDLE     = (80,  80,  80)   # white  — connected, no input
COL_WS       = (120, 100, 0)    # yellow — W or S
COL_AD       = (150, 40,  0)    # orange — A or D
COL_FLIP     = (80,  0,   120)  # purple — H or L (flip)
COL_DASH     = (0,   120, 120)  # cyan   — J (dash)
COL_FIRE     = (0,   120, 0)    # green  — F (fire)
COL_ESC      = (120, 0,   0)    # red    — ESC

# ── Breathing ──
BREATH_MIN    = 0.10
BREATH_MAX    = 1.00
BREATH_STEPS  = 40          # steps per half-cycle (40×20ms = 0.8s per half)

# ── Linger — how many loops a colour holds after button releases ──
LINGER_LOOPS  = 12          # ~240ms


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  BLE KEYBOARD WRAPPER
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

class BLEKbdHold(BLEKeyboard):
    def send_hold(self, keycodes, modifier=0):
        ks = list(keycodes)[:6]
        while len(ks) < 6:
            ks.append(0)
        self._send(struct.pack("8B", modifier, 0, *ks))


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  NEOPIXEL CONTROLLER — continuous breathing
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  Triangle wave runs every loop regardless of colour changes.
#  set_colour() swaps the hue without resetting the wave, so
#  transitions feel smooth instead of snapping.

class NeoController:
    def __init__(self, pin, n):
        self.np         = neopixel.NeoPixel(Pin(pin), n)
        self.n          = n
        self.target     = COL_IDLE
        self._step      = 0
        self._direction = 1

    def set_colour(self, colour):
        self.target = colour

    def breathe(self):
        t = self._step / BREATH_STEPS
        b = BREATH_MIN + (BREATH_MAX - BREATH_MIN) * t
        col = (
            int(self.target[0] * b),
            int(self.target[1] * b),
            int(self.target[2] * b),
        )
        for i in range(self.n):
            self.np[i] = col
        self.np.write()

        self._step += self._direction
        if self._step >= BREATH_STEPS:
            self._direction = -1
        elif self._step <= 0:
            self._direction = 1

    def startup_flash(self):
        """Rapid colour cycle on boot — confirms wiring immediately."""
        for col in [(120,0,0),(120,80,0),(0,120,0),(0,0,120),(80,0,120)]:
            for i in range(self.n):
                self.np[i] = col
            self.np.write()
            time.sleep_ms(120)
        for i in range(self.n):
            self.np[i] = (0, 0, 0)
        self.np.write()


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  JOYSTICK
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

class Joystick:
    def __init__(self, pin_x, pin_y, pin_btn, deadzone,
                 invert_x=False, invert_y=False):
        self.adc_x    = ADC(Pin(pin_x))
        self.adc_y    = ADC(Pin(pin_y))
        self.adc_x.atten(ADC.ATTN_11DB)
        self.adc_y.atten(ADC.ATTN_11DB)
        self.btn      = Pin(pin_btn, Pin.IN, Pin.PULL_UP)
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
        x_dir   = 1 if dx > self.deadzone else (-1 if dx < -self.deadzone else 0)
        y_dir   = 1 if dy > self.deadzone else (-1 if dy < -self.deadzone else 0)
        pressed = self.btn.value() == 0
        return (x_dir, y_dir, pressed)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  GAMEPAD
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

class Gamepad:
    def __init__(self, js1, js2, keyboard, neo):
        self.js1       = js1
        self.js2       = js2
        self.kbd       = keyboard
        self.neo       = neo
        self.last_keys = frozenset()
        self.linger    = 0
        self.linger_col = COL_IDLE

    def update(self):
        x1, y1, btn1 = self.js1.read()
        x2, y2, btn2 = self.js2.read()

        keys = set()

        # ── Left stick: WASD + ESC click ──────────────────────
        if   x1 > 0: keys.add(KEY_D)
        elif x1 < 0: keys.add(KEY_A)
        if   y1 > 0: keys.add(KEY_W)
        elif y1 < 0: keys.add(KEY_S)
        if btn1:     keys.add(KEY_ESC)

        # ── Right stick: H/L/J + F click ──────────────────────
        if   x2 < 0: keys.add(KEY_H)   # lean left  → flip left
        elif x2 > 0: keys.add(KEY_L)   # lean right → flip right
        if   y2 < 0: keys.add(KEY_J)   # push down  → dash
        if btn2:     keys.add(KEY_F)   # click      → fire

        current = frozenset(keys)
        if current != self.last_keys:
            self.kbd.send_hold(current)
            self.last_keys = current
            self._log(current)

        self._pick_colour(keys)
        self.neo.breathe()

    def _pick_colour(self, keys):
        """
        Priority (high → low):
          fire > esc > dash > flip > W/S > A/D > idle
        Linger keeps the colour alive briefly after release.
        """
        if KEY_F in keys:
            self._set_linger(COL_FIRE)
        elif KEY_ESC in keys:
            self._set_linger(COL_ESC)
        elif KEY_J in keys:
            self._set_linger(COL_DASH)
        elif KEY_H in keys or KEY_L in keys:
            self._set_linger(COL_FLIP)
        elif KEY_W in keys or KEY_S in keys:
            self._set_linger(COL_WS)
        elif KEY_A in keys or KEY_D in keys:
            self._set_linger(COL_AD)
        else:
            if self.linger > 0:
                self.linger -= 1
                self.neo.set_colour(self.linger_col)
            else:
                self.neo.set_colour(COL_IDLE)

    def _set_linger(self, colour):
        self.linger     = LINGER_LOOPS
        self.linger_col = colour
        self.neo.set_colour(colour)

    def _log(self, keys):
        names = {
            KEY_W:"W", KEY_A:"A", KEY_S:"S", KEY_D:"D",
            KEY_ESC:"ESC", KEY_H:"H", KEY_L:"L",
            KEY_J:"J", KEY_F:"F",
        }
        held = [names.get(k, "?") for k in keys]
        print("  keys:", "+".join(held) if held else "(released)")


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  MAIN
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def main():
    print("=" * 40)
    print("  ESP32 BLE Gamepad")
    print("  L:WASD+ESC  R:H/L/J+F")
    print("=" * 40)

    neo = NeoController(PIN_NEO, NUM_PIXELS)
    neo.startup_flash()                    # colour cycle = neopixel alive

    print("Starting BLE...")
    kbd = BLEKbdHold(DEVICE_NAME)
    neo.set_colour(COL_WAITING)            # white breathing while pairing

    print("Calibrating — DO NOT touch the sticks!")
    time.sleep_ms(500)
    js  = Joystick(PIN_JOY_X,  PIN_JOY_Y,  PIN_JOY_BTN,
                   DEADZONE, INVERT_X, INVERT_Y)
    js2 = Joystick(PIN_JOY2_X, PIN_JOY2_Y, PIN_JOY2_BTN,
                   DEADZONE, INVERT_X, INVERT_Y)
    js.calibrate()
    js2.calibrate()
    print("  stick1 center: X={}  Y={}".format(js.center_x,  js.center_y))
    print("  stick2 center: X={}  Y={}".format(js2.center_x, js2.center_y))

    print("\nPair with '{}' in Bluetooth settings.".format(DEVICE_NAME))
    while not kbd.is_connected():
        neo.breathe()
        time.sleep_ms(LOOP_MS)
    print("Connected!\n")
    neo.set_colour(COL_IDLE)

    gamepad = Gamepad(js, js2, kbd, neo)
    while True:
        if kbd.is_connected():
            gamepad.update()
        else:
            neo.set_colour(COL_WAITING)
            neo.breathe()
        time.sleep_ms(LOOP_MS)


main()]
```

---

# 11. MIT App Inventor Plan

## 11.1 Is an app part of this project?
- [ ] Yes
- [ ] No

If yes, complete this section.

## 11.2 Why is the app needed?
Explain what the app adds to the experience.

Examples:
- remote control,
- score tracking,
- mode selection,
- personalization,
- triggering effects,
- displaying data.

**Response:**  
`[Write here]`

## 11.3 App Features

| Feature | Purpose |
|---|---|
| `[Bluetooth connect button]` | `[Purpose]` |
| `[Score display]` | `[Purpose]` |
| `[Control button / slider / label]` | `[Purpose]` |

## 11.4 UI Mockup
Insert a sketch or screenshot of the app interface.

**Insert image below:**  
`[Upload image and link here]`

## 11.5 App Screen Flow

1. `[Step 1]`
2. `[Step 2]`
3. `[Step 3]`
4. `[Step 4]`

---

# 12. Bill of Materials

## 12.1 Full BOM

| Item | Quantity | In Kit? | Need to Buy? | Estimated Cost | Material / Spec | Why This Choice? |
|---|---:|---|---|---:|---|---|
| `[ESP32]` | `1` | `Yes` | `No` | `0` | `[Spec]` | `[Reason]` |
| `[Item]` | `[Qty]` | `[Yes/No]` | `[Yes/No]` | `[Cost]` | `[Spec]` | `[Reason]` |
| `[Item]` | `[Qty]` | `[Yes/No]` | `[Yes/No]` | `[Cost]` | `[Spec]` | `[Reason]` |

## 12.2 Material Justification
Explain why you selected your main materials and components.

Examples:
- Why acrylic instead of cardboard?
- Why MDF instead of 3D print?
- Why servo instead of DC motor?
- Why bearing instead of a plain shaft hole?

**Response:**  
`[Write here]`

## 12.3 Items to Purchase Separately

| Item | Why Needed | Purchase Link | Latest Safe Date to Procure | Status |
|---|---|---|---|---|
| `[Item]` | `[Reason]` | `[Link]` | `[Date]` | `[Pending / Ordered / Received]` |
| `[Item]` | `[Reason]` | `[Link]` | `[Date]` | `[Pending / Ordered / Received]` |

## 12.4 Budget Summary

| Budget Item | Estimated Cost |
|---|---:|
| Electronics | `[Cost]` |
| Mechanical parts | `[Cost]` |
| Fabrication materials | `[Cost]` |
| Purchased extras | `[Cost]` |
| Contingency | `[Cost]` |
| **Total** | `[Cost]` |

## 12.5 Budget Reflection
If your cost is too high, what can be simplified, removed, substituted, or shared?

**Response:**  
`[Write here]`

---

# 13. Planning the Work

## 13.1 Team Working Agreement
Write how your team will work together.

Include:
- how tasks are divided,
- how decisions are made,
- how progress will be checked,
- what happens if a task is delayed,
- how documentation will be maintained.

**Response:**  
`[Write here]`

## 13.2 Task Breakdown

| Task ID | Task | Owner | Estimated Hours | Deadline | Dependency | Status |
|---|---|---|---:|---|---|---|
| T1 | `[Finalize concept]` | `[Name]` | `2` | `[Date]` | `None` | `To Do` |
| T2 | `[Complete BOM]` | `[Name]` | `1` | `[Date]` | `T1` | `To Do` |
| T3 | `[Test electronics]` | `[Name]` | `2` | `[Date]` | `T1` | `To Do` |
| T4 | `[Build structure]` | `[Name]` | `4` | `[Date]` | `T1` | `To Do` |
| T5 | `[Write control code]` | `[Name]` | `4` | `[Date]` | `T3` | `To Do` |
| T6 | `[Integrate system]` | `[Name]` | `4` | `[Date]` | `T4, T5` | `To Do` |
| T7 | `[Playtest]` | `[Name]` | `2` | `[Date]` | `T6` | `To Do` |
| T8 | `[Refine and document]` | `[Name]` | `3` | `[Date]` | `T7` | `To Do` |

## 13.3 Responsibility Split

| Area | Main Owner | Support Owner |
|---|---|---|
| Concept and gameplay | `[Name]` | `[Name]` |
| Electronics | `[Name]` | `[Name]` |
| Coding | `[Name]` | `[Name]` |
| App | `[Name]` | `[Name]` |
| Mechanical build | `[Name]` | `[Name]` |
| Testing | `[Name]` | `[Name]` |
| Documentation | `[Name]` | `[Name]` |

---

# 14. Weekly Milestones

## 14.1 Four-Week Plan

### Week 1 — Plan and De-risk
Expected outcomes:
- [O] Idea finalized
- [0] Core interaction decided
- [ ] Sketches made
- [ ] BOM completed
- [0] Purchase needs identified
- [ ] Key uncertainty identified
- [ ] Basic feasibility tested

### Week 2 — Build Subsystems
Expected outcomes:
- [ ] Electronics tests completed
- [ ] CAD / structure planning completed
- [ ] App UI started if needed
- [ ] Mechanical concept tested
- [ ] Main subsystems partially working

### Week 3 — Integrate
Expected outcomes:
- [ ] Physical body built
- [ ] Electronics integrated
- [ ] Code connected to hardware
- [ ] App connected if required
- [ ] First playable version exists

### Week 4 — Refine and Finish
Expected outcomes:
- [ ] Technical bugs reduced
- [ ] Playtesting completed
- [ ] Improvements made
- [ ] Documentation completed
- [ ] Final build ready

## 14.2 Weekly Update Log

| Week | Planned Goal | What Actually Happened | What Changed | Next Steps |
|---|---|---|---|---|
| Week 1 | `[Write here]` | `[Write here]` | `[Write here]` | `[Write here]` |
| Week 2 | `[Write here]` | `[Write here]` | `[Write here]` | `[Write here]` |
| Week 3 | `[Write here]` | `[Write here]` | `[Write here]` | `[Write here]` |
| Week 4 | `[Write here]` | `[Write here]` | `[Write here]` | `[Write here]` |

---

# 15. Risks and Unknowns

## 15.1 Risk Register

| Risk | Type | Likelihood | Impact | Mitigation Plan | Owner |
|---|---|---|---|---|---|
| `[Example: Bluetooth disconnects]` | `Technical` | `Medium` | `High` | `[Fallback interaction / simplify connection flow]` | `[Name]` |
| `[Example: Structure breaks during play]` | `Mechanical` | `Medium` | `High` | `[Reinforce joints / change material]` | `[Name]` |
| `[Risk]` | `[Technical / Material / Time / Gameplay]` | `[Low/Medium/High]` | `[Low/Medium/High]` | `[Plan]` | `[Name]` |
| `[Risk]` | `[Type]` | `[Low/Medium/High]` | `[Low/Medium/High]` | `[Plan]` | `[Name]` |

## 15.2 Biggest Unknown Right Now
What is the single biggest uncertainty in your project at this stage?

**Response:**  
`[Write here]`

---

# 16. Testing and Playtesting

## 16.1 Technical Testing Plan

| What Needs Testing | How You Will Test It | Success Condition |
|---|---|---|
| `[Bluetooth connection]` | `[Method]` | `[What counts as success?]` |
| `[Mechanism movement]` | `[Method]` | `[What counts as success?]` |
| `[Sensor behavior]` | `[Method]` | `[What counts as success?]` |
| `[App communication]` | `[Method]` | `[What counts as success?]` |

## 16.2 Playtesting Plan

| Question | How You Will Check |
|---|---|
| Do players understand what to do? | `[Method]` |
| Is the interaction satisfying? | `YES` |
| Do players want another turn? | `YES` |
| Is the challenge balanced? | `YES` |
| Is the response clear and immediate? | `[Method]` |

## 16.3 Testing and Debugging Log

| Date | Problem Found | Type | What You Tried | Result | Next Action |
|---|---|---|---|---|---|
| `[Date]` | `[Describe issue]` | `[Technical / Mechanical / UI / Gameplay]` | `[What you did]` | `[Worked / Partly / Failed]` | `[Next step]` |
| `[Date]` | `[Describe issue]` | `[Type]` | `[What you did]` | `[Result]` | `[Next step]` |

## 16.4 Playtesting Notes

| Tester | What They Did | What Confused Them | What They Enjoyed | What You Will Change |
|---|---|---|---|---|
| `[Peer / friend / classmate]` | `[Observation]` | `[Observation]` | `[Observation]` | `[Action]` |
| `[Peer / friend / classmate]` | `[Observation]` | `[Observation]` | `[Observation]` | `[Action]` |

---

# 17. Build Documentation

## 17.1 Fabrication Process
Describe how the project was physically made.

Include:
- cutting,
- 3D printing,
- assembly,
- fastening,
- wiring,
- finishing,
- revisions.

**Response:**  
`[Write here]`

## 17.2 Build Photos
Add photos throughout the project.

Suggested images:
- early sketch,
- prototype,
- electronics testing,
- mechanism test,
- app screenshot,
- final build.

Example:
```md



```

## 17.3 Version History

| Version | Date | What Changed | Why |
|---|---|---|---|
| `v1` | `[Date]` | `[Describe]` | `[Reason]` |
| `v2` | `[Date]` | `[Describe]` | `[Reason]` |
| `v3` | `[Date]` | `[Describe]` | `[Reason]` |

---

# 18. Final Outcome

## 18.1 Final Description
Describe the final version of your project.

**Response:**  
`[Write here]`

## 18.2 What Works Well
- `[Point 1]`
- `[Point 2]`
- `[Point 3]`

## 18.3 What Still Needs Improvement
- `[Point 1]`
- `[Point 2]`
- `[Point 3]`

## 18.4 What Changed From the Original Plan
How did the project change from the initial idea?

**Response:**  
`[Write here]`

---

# 19. Reflection

## 19.1 Team Reflection
What did your team do well?  
What slowed you down?  
How well did you manage time, tasks, and responsibilities?

**Response:**  
`[Write here]`

## 19.2 Technical Reflection
What did you learn about:
- electronics,
- coding,
- mechanisms,
- fabrication,
- integration?

**Response:**  
`[Write here]`

## 19.3 Design Reflection
What did you learn about:
- designing for play,
- delight,
- clarity,
- physical interaction,
- player understanding,
- iteration?

**Response:**  
`[Write here]`

## 19.4 If You Had One More Week
What would you improve next?

**Response:**  
`[Write here]`

---

# 20. Final Submission Checklist

Before submission, confirm that:
- [ ] Team details are complete
- [ ] Project description is complete
- [ ] Inspiration sources are included
- [ ] Player journey is written
- [ ] Sketches are added
- [ ] BOM is complete
- [ ] Purchase list is complete
- [ ] Budget summary is complete
- [ ] Mechanical planning is documented if applicable
- [ ] App planning is documented if applicable
- [ ] Code flowchart is added
- [ ] Task breakdown is complete
- [ ] Weekly logs are updated
- [ ] Risk register is complete
- [ ] Testing log is updated
- [ ] Playtesting notes are included
- [ ] Build photos are included
- [ ] Final reflection is written

---

# 21. Suggested Repository Structure

```text
project-repo/
├── README.md
├── images/
│   ├── concept-sketch.jpg
│   ├── labeled-sketch.jpg
│   ├── circuit-diagram.jpg
│   ├── ui-mockup.jpg
│   ├── prototype-1.jpg
│   └── final-build.jpg
├── code/
│   ├── main.py
│   ├── test_code.py
│   └── notes.md
├── cad/
│   ├── models/
│   └── screenshots/
└── docs/
    ├── references.md
    └── extra-notes.md
```

---

# 22. Instructor Review

## 22.1 Proposal Approval
- [ ] Approved to proceed
- [ ] Approved with changes
- [ ] Rework required before proceeding

**Instructor comments:**  
`[Instructor fills this section]`

## 22.2 Midpoint Review
`[Instructor fills this section]`

## 22.3 Final Review Notes
`[Instructor fills this section]`
