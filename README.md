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
| `Ashitha Ashok` | `[Coding / App]` | `[Front End Development]` | `[Strong logic building, UI thinking, integration]` |
| `Varada Supanekar` | `[Electronics / Fabrication]` | `[Circuit Protoyping]` | `[Circuit design, physical prototyping]` |

## 1.3 Project Title
`[Batmanor]`

## 1.4 One-Line Pitch
`A fast-paced pixel-art Batman game controlled by a hand-built ESP32 dual-joystick console that transmits inputs wirelessly over BLE and lights up a NeoPixel in real time to mirror every in-game action.`

## 1.5 Expanded Project Idea
In 1–2 paragraphs, explain:
- what your project is,
- what kind of playful experience it creates,
- what makes it fun, curious, engaging, strange, satisfying, competitive, or delightful,
- what technologies are involved.

**Response:**  
`The project is a 2D pixel-art game (BATMANNER) where Batman navigates a manor, dodging obstacles and enemies. All player input comes from a custom physical console built around an ESP32 microcontroller with two HW-504 analogue joysticks. The console pairs to the game host over Bluetooth Low Energy, appearing as a standard HID keyboard so no special drivers are needed.
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
`[We are designing this project as if we are a small creative studio making a game / interactive experience for teens and exhibition visitors. It is supposed to evoke a sense of nostalgia and 90s arcade games for young adults and millennials]`

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
| Is explanation required before use? | `[Minimal- getting acquanited to the console directions]` |

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

- `[Light-sensor proximity trigger to auto-wake the game when a player approaches.]`
- `[Score leaderboard displayed on the mirror frame after each round.]`

---

# 6. System Overview

## 6.1 Project Type
Check all that apply.

- [x] Electronics-based
- [ ] Mechanical
- [x] Sensor-based
- [x] App-connected
- [ ] Motorized
- [ ] Sound-based
- [x] Light-based
- [x] Screen/UI-based
- [x] Fabricated structure
- [x] Game logic based
- [x] Installation / tabletop experience
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
`[<img width="3099" height="2202" alt="image" src="https://github.com/user-attachments/assets/8f0f676c-5a11-4726-abed-76b6e74d0efc" />
]`
<img width="1262" height="686" alt="image" src="https://github.com/user-attachments/assets/978092dc-cd92-4319-8027-275b2ac95b96" />


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
`[<img width="1262" height="686" alt="WhatsApp Image 2026-04-21 at 7 54 00 PM" src="https://github.com/user-attachments/assets/bdff8dae-c357-4b12-bb40-86fed4bbed35" />
]`

## 7.3 Approximate Dimensions

| Dimension | Value |
|---|---|
| Length | `[~180 mm]` |
| Width | `[~110 mm]` |
| Height | `[~50 mm (enclosure with joystick caps)]` |
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
| `[Illustrator]` | `[<img width="1262" height="686" alt="WhatsApp Image 2026-04-21 at 7 54 00 PM" src="https://github.com/user-attachments/assets/272accc4-67b5-4593-8819-da83edd3b9c1" />
]` | `[Enclosure dimensions and joystick hole placement]` |
| `[Gdev]` | `[https://gd.games/games/487fed3e-c6a6-4b87-bb02-618c9e5fb403]` | `[Basic ADC read and NeoPixel output before physical assembly]` |

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


Right Joystick (HW-504 #2):

VCC → ESP32 3.3V
GND → ESP32 GND
VRx → GPIO 34 (ADC1_CH6, input-only)
VRy → GPIO 35 (ADC1_CH7, input-only)


NeoPixel:

VCC → ESP32 VIN (5V from USB)
GND → ESP32 GND
DIN → 300 Ω resistor → GPIO 14


Note: GPIO 34 and 35 are input-only on the ESP32 — do not try to use them as outputs. Internal pull-ups are not available on these pins; the joystick button uses GPIO 25 and 26 which support PULL_UP.]`

## 9.3 Circuit Diagram
Insert a hand-drawn or software-made circuit diagram.

**Insert image below:**  
[<img width="1600" height="1582" alt="image" src="https://github.com/user-attachments/assets/3418bc60-d3db-434a-b8fa-62679e4e5af4" />]
<img width="1075" height="1600" alt="image" src="https://github.com/user-attachments/assets/623bbe00-33d0-412d-b18d-f1c241ff1609" />




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
`[NeoPixel runs a 5-colour startup flash (R→Y→G→B→Purple) to confirm wiring.
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

PIN_JOY2_X   = 34          # right stick X  → H / L
PIN_JOY2_Y   = 35          # right stick Y  → J (down)


# ── NeoPixel ──
PIN_NEO      = 14           
NUM_PIXELS   = 90            # ← set this to however many LEDs you have

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

# 11. Ddevelop Game Inventor Plan

## 11.1 Is an app part of this project?
- [x] Yes
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
<img width="1462" height="787" alt="1" src="https://github.com/user-attachments/assets/e1515931-6aed-4767-af17-93b7cfa5e64c" />
<img width="1466" height="768" alt="3" src="https://github.com/user-attachments/assets/9ee9cc52-e363-46fd-bff9-30557a8a76e6" />
<img width="1449" height="807" alt="4" src="https://github.com/user-attachments/assets/1e4e3320-b929-4c3f-8ae4-f3437aab85d2" />




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
| `[ESP32]` | `1` | `Yes` | `Yes` | QTY -`4` | 2040 Rupees | `[ESP32WROOM-Bluetooth/wifi]` | `[Main MicroPython Device]` |
| `[18650 Battery]` | `[No]` | `[Yes]` | QTY - '1' |`[100 Rupees]` | `[Power Source to have a wireless connection for ESP32]` |
| `Battery Holder` | `NO` | `[Yes]` | QTY - '1' | `[30 Rupees]` | `[PLastic Holder]` | `[Power Source aid]` |
| `[Joystick Module]` | `2` | `No` | `Yes` | 100 Rupees | `[E-348 - PS2 JOYSTICK MODULE BREAKOUT SENSOR]` | `[More interactive and matched our arcade themed game idea]` |
|`[Breadboard]` | `2` | `Yes` | `Yes` | 98 Rupees | `[RCT-159 - BREADBOARD - 400 POINTS]` | `[Multiple connections reqd two boards]` |
|`Push Buttons` | `6` | `Yes` | `Yes` |  36 Rupees | `[TC 15 12*12*7 mm ]` | `[More Buttons to add actions to the console]` |
|'Micro-USB cable' | '1' | 'Yes' | Yes | 120 Rupees | USB-A to Micro-B | Power + MicroPython flashing via Thonny |`
| 'One-way acrylic mirror sheet' | 1 | No | Yes | ₹1250 | 9 by 12 inches, 3 mm | Mirror installation for game display illusion |
|`Neopixelstrip` | `1` | `no` | `Yes` |  275 Rupees | `[2m neopixel strip ]` | `[Reaction based element]

## 12.2 Material Justification
Explain why you selected your main materials and components.

Examples:
- Why acrylic instead of cardboard?
- Why MDF instead of 3D print?
- Why servo instead of DC motor?
- Why bearing instead of a plain shaft hole?

**Response:**  
`[**HW-504 JOYSTICKS over buttons:** Analogue joysticks give proportional directional intent and a single module covers upto 4 axes axes plus a click, reducing wiring complexity significantly.
- **WS2812B NeoPixel over plain LEDs:** Single-wire addressable RGB allows any colour to be set in one line of code, enabling the full action-colour feedback system without extra PWM pins.
- **MDF/PLA enclosure over cardboard:** Cardboard deforms under joystick force. A rigid enclosure keeps joystick modules fixed at the correct height and separation for comfortable two-thumb grip.

]`

## 12.3 Items to Purchase Separately

| Item | Why Needed | Purchase Link | Latest Safe Date to Procure | Status |
|---|---|---|---|---|
| `[ESP 32]` | `[Original one was fried]` | `[Ordered from a local shop]` | `[11 April]` | `[Reecieved]` |
| `[Neopixels strips]` | `[the kit didnt have strips]` | `[shop]` | `[17 April]` | `[ Received]` |
| `[Joystick controller]` | `[to make the console]` | `[shop]` | `[17 April]` | `[ Received]` |
| `[Buck Converter]` | `[preventing voltage issues]` | `[shop]` | `[17 April]` | `[ Received]` |

## 12.4 Budget Summary

| Budget Item | Estimated Cost |
|---|---:|
| Electronics Joysticks/Breadboard/Battery 3.3v| `[750]` |
| Mechanical parts | `[-]` |
| Fabrication materials - Mirror | `[1250]` |
| Purchased extras - Jumper Wires/Buck Converter| `[200]` |
| Contingency - 4ESPS | `[1600]` |
| **Total** | `[3800]` |

## 12.5 Budget Reflection
If your cost is too high, what can be simplified, removed, substituted, or shared?

**Response:**  
`[If cost is too high: drop the one-way mirror installation and present the game on a plain screen — the core BLE controller experience is unaffected. The enclosure can be built from cardboard and hot glue as an interim version while waiting for the laser-cut part.]`

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
`[Tasks are laddered first. Then divide on the basis of time at hand. Tasks are divided into two sections which can be simultaneously worked on. Ideation and Thinking process is done together. The repo keeps us on track and helps us keeping up with time and checks our pace. If the task is delayed due to problems beyond our control we reach out to sources online such as youtube,chatgpt etc. At times we also reach out to our faculty and peers. If a task is delayed, the other member picks up documentation or testing for that area. The documentation is maintained via a notion collaborating app where we write down all tasks, codes, refrence material etc ]`

## 13.2 Task Breakdown

| Task ID | Task | Owner | Estimated Hours | Deadline | Dependency | Status |
|---|---|---|---:|---|---|---|
| T1 | Finalize concept and game control mapping | Both | 2 | Week 1 | None | Done |
| T2 | Complete BOM and purchase list | Varada | 1 | Week 3 | T1 | Done |
| T3 | Flash MicroPython, test ADC on both joysticks | Varada | 2 | Week 1 | T1 | Done |
| T4 | Wire joysticks + NeoPixel on breadboard | Varada | 2 | Week 1 | T1 | Done |
| T5 | Write and test BLE HID send_hold logic | Ashitha | 3 | Week 2 | T3 | In Progress |
| T6 | Implement NeoPixel breathing + colour logic | Ashitha | 2 | Week 2 | T4 | In Progress |aa
| T7 | Map game keybindings in GDevelop to match ESP32 output | Ashitha | 2 | Week 2 | T5 | To Do |
| T8 | Design and fabricate enclosure | Varada | 4 | Week 3 | T4 | To Do |
| T9 | Solder final circuit into enclosure | Varada | 3 | Week 3 | T6, T8 | To Do |
| T10 | Build one-way mirror installation frame | Varada | 3 | Week 3 | T8 | To Do |
| T11 | Full system integration test | Both | 2 | Week 3 | T7, T9, T10 | To Do |
| T12 | Playtest with 3 external users | Both | 2 | Week 4 | T11 | To Do |
| T13 | Refine based on playtest feedback | Ashitha | 2 | Week 4 | T12 | To Do |
| T14 | Final documentation and README completion | Both | 3 | Week 4 | T13 | To Do |

## 13.3 Responsibility Split

| Area | Main Owner | Support Owner |
|---|---|---|
| Concept and gameplay | `[Ashitha]` | `[Varada]` |
| Electronics | `[Varada]` | `[Ashitha]` |
| Coding | `[Varada]` | `[Ashitha]` |
| App | `[Ashitha]` | `[Varada]` |
| Physical build | `[Varada]` | `[Ashitha]` |
| Testing | `[Ashitha]` | `[Varada]` |
| Documentation | `[Varada]` | `[Ashitha]` |

---

# 14. Weekly Milestones

## 14.1 Four-Week Plan

### Week 1 — Plan and De-risk
Expected outcomes:
- [x] Idea finalized
- [x] Core interaction decided (BLE HID keyboard over dual joystick)
- [ ] Sketches made
- [x] BOM completed
- [x] Purchase needs identified (mirror sheet, enclosure)
- [x] Key uncertainty identified: BLE latency + GDevelop key-hold behaviour
- [x] Basic feasibility tested: single joystick ADC read confirmed in Thonny

### Week 2 — Build Subsystems
Expected outcomes:
- [x] Both joysticks reading correctly with deadzone and calibration
- [x] BLE pairing confirmed with iPad; keypress received in GDevelop
- [x] NeoPixel breathing and colour-change logic working on bench
- [x] GDevelop keybindings mapped and tested with keyboard

### Week 3 — Integrate
Expected outcomes:
- [x] Enclosure fabricated and electronics installed
- [x] Full cable routing done inside enclosure
- [x] One-way mirror frame assembled
- [x] First complete play session with final hardware

### Week 4 — Refine and Finish
Expected outcomes:
- [x] Latency and responsiveness verified (target: no perceptible lag)
- [x] 3 external playtests completed
- [x] NeoPixel linger timing tuned based on player feedback
- [x] README, photos, and code comments finalized


## 14.2 Weekly Update Log

| Week | Planned Goal | What Actually Happened | What Changed | Next Steps |
|---|---|---|---|---|
| Week 1 | Concept, BOM, first ADC test | Concept finalized; BOM done; ADC read working on left joystick only | Right joystick on GPIO 34/35 needed ATTN_11DB explicitly set | Add ATTN_11DB to both joysticks — already in code |
| Week 2 | BLE pairing, NeoPixel logic, GDevelop keybindings | BLE paired successfully with iPad on first try; NeoPixel breathing working; GDevelop keybindings mapped. Discovered GDevelop needs key-held events not key-pressed — fixed in scene editor | Switched all game controls from key-press to key-held events in GDevelop; adjusted linger from 8 loops to 12 for better visual feedback | Solder permanent circuit, start enclosure CAD |
| Week 3 | Enclosure built, mirror frame assembled, full integration | Enclosure laser-cut from 3mm MDF; joystick holes required second pass — first cut was 0.5mm too tight for the module collar. Mirror frame built from timber offcuts. Full play session completed, minor BLE dropout at ~3m range | Reduced target play distance to under 1.5m; added reconnect breathing loop already in firmware | Playtest with external users, tune deadzone |
| Week 4 | Playtesting, refinement, documentation | Three external playtests done; deadzone reduced from 600 to 500 after feedback that diagonal movement felt sluggish. NeoPixel linger felt right at 12 loops. One tester suggested labelling the joysticks — added printed sticker labels to enclosure | Deadzone tuned to 500; joystick labels added; README and code comments finalised | Final submission |

---

# 15. Risks and Unknowns

## 15.1 Risk Register

| Risk | Type | Likelihood | Impact | Mitigation Plan | Owner |
|---|---|---|---|---|---|
| Risk | Type | Likelihood | Impact | Mitigation Plan | Owner |
|---|---|---|---|---|---|
| BLE disconnects during play | Technical | Medium | High | Reconnect loop in firmware already handles this — LED returns to white and game continues from last state on reconnect | Ashitha |
| GDevelop treats held keys as repeated taps instead of held | Technical | Medium | High | Test `send_hold` with a key-hold test scene in GDevelop before Week 2 ends; use key-hold events not key-press events in GDevelop | Ashitha |
| GPIO 34/35 ADC noise causing phantom keypresses | Technical | Medium | Medium | Deadzone of 600 (≈15% of range) absorbs most noise; add small capacitor on ADC lines if still noisy | Varada |
| NeoPixel flicker from power draw | Technical | Low | Low | 100 µF capacitor on VCC + 300 Ω series on DIN already specified | Ashitha |
| Enclosure joystick holes misaligned | Mechanical | Medium | Medium | Prototype in cardboard before committing to MDF/PLA; measure joystick cap diameter precisely | Varada |
| Mirror sheet arrives late | Material | Medium | High | Core experience works without mirror; proceed with plain screen during Week 3 if needed | Both |
| BLE keyboard not recognised by iPad | Technical | Low | High | Test early (Week 2 Day 1); ensure BLEKeyboard advertises correct HID descriptor | Varada |


## 15.2 Biggest Unknown Right Now
What is the single biggest uncertainty in your project at this stage?

**Response:**  
`[Whether GDevelop on iPad correctly handles a BLE HID device holding multiple keys simultaneously for a sustained duration. Standard keyboards send key-repeat events, but `send_hold` in the firmware sends the same HID report continuously as long as the stick is deflected. We need to verify GDevelop's key-held event triggers fire correctly and do not interpret the repeated reports as key spam.]`

---

# 16. Testing and Playtesting

## 16.1 Technical Testing Plan

| What Needs Testing | How You Will Test It | Success Condition |
|---|---|---|
| BLE pairing with iPad | Power on ESP32; look for "ESP32_Gamepad" in iPad Bluetooth settings; connect | Device pairs within 10 seconds; no repeated disconnects |
| Joystick ADC calibration accuracy | Run calibrate() with sticks untouched; print centre values; check both axes within 1900–2200 | Centre value stable ±50 counts across 3 calibrations |
| Deadzone function | Slowly tilt stick from centre; observe first keypress in serial log | No key fires below ±600 ADC count deflection |
| BLE key-hold in GDevelop | Hold left stick up; Batman should move continuously, not stutter | Smooth continuous movement for the full duration of stick deflection |
| NeoPixel colour priority | Press each action in order (F, ESC, J, H, A); observe LED colour | Correct colour on every action; linger ~240 ms after release |
| Linger timing | Release all sticks; count time before LED returns to white | 12 loops × 20 ms = ~240 ms linger before idle white |
| Simultaneous key presses | Hold W + fire button simultaneously | Both W (yellow) and F (green) processed; green (fire) wins per priority ladder |


## 16.2 Playtesting Plan

| Question | How You Will Check |
|---|---|
| Do players understand what to do? | Observe first 30 seconds without instructions; note which stick they try first |
| Is the interaction satisfying? | Ask players after each round; rate 1–5 |
| Do players want another turn? | Count unprompted requests for another round |
| Is the challenge balanced? | Track average survival time on first run; target 20–40 seconds |
| Is the NeoPixel response clear? | Ask players whether the LED helped them understand their actions |

## 16.3 Testing and Debugging Log

| Date | Problem Found | Type | What You Tried | Result | Next Action |
|---|---|---|---|---|---|
| Week 1, Day 2 | GPIO 34/35 returning 0 constantly | Technical | Checked wiring, then added `ADC.ATTN_11DB` to adc_x and adc_y on joystick 2 | Worked — values now read 0–4095 correctly | Already fixed in final code |
| Week 2, Day 1 | BLE keyboard paired but Batman not moving in GDevelop | Technical | Checked serial log — keys were sending correctly. Opened GDevelop event editor — controls used key-pressed (fires once) instead of key-held (fires every frame) | Fixed — swapped all movement events to key-held in GDevelop | No further action needed |
| Week 2, Day 2 | NeoPixel flickering white when fire button held | Technical | Suspected power noise; added 100µF cap across NeoPixel VCC/GND | Flicker stopped entirely | Capacitor included in final build |
| Week 3, Day 1 | Joystick module collar too wide for first MDF cut | Mechanical | Re-measured joystick module: collar diameter 24mm not 22mm as assumed. Re-cut holes on laser cutter with 24.5mm diameter | Modules fit cleanly with slight friction hold — no glue needed | Done |
| Week 3, Day 2 | BLE dropout when console moved beyond ~2.5m from iPad | Technical | Tested at 1m, 1.5m, 2m, 3m — stable up to 2m, occasional dropout at 2.5m+ | Acceptable — installation keeps player within 1m of screen | Set recommended play distance to ≤1.5m |
| Week 4, Day 1 | Players reporting diagonal movement felt delayed | Gameplay | Reduced deadzone from 600 to 500 ADC counts in config | Movement felt noticeably more responsive in next playtest | Done — updated in code |

## 16.4 Playtesting Notes

| Tester | What They Did | What Confused Them | What They Enjoyed | What You Will Change |
|---|---|---|---|---|
| Classmate (Advaith) | Picked up controller, tried left stick first, figured out movement within 20 seconds without instruction | Did not notice right stick at first — assumed it was decorative | The NeoPixel turning red when she pressed ESC — said it felt like the controller "knew" she paused | Added a small printed label: LEFT = MOVE, RIGHT = FLIP/DASH/FIRE |
| Classmate (Anish) | Immediately tried both sticks, discovered dash (J) by accident, kept using it | Initially pushed right stick up expecting a jump — J is only triggered by pushing down | The fast colour transitions on the NeoPixel, especially cyan on dash | Added a note to instructions: right stick down = dash, no upward action |
| Fellow (Rajasi) | Played cautiously, mostly used left stick only, survived longer than other players | Thought the game was only controlled by the left stick — never attempted right stick actions | The mirror effect revealing the game — said the transition was "striking" | Mirror reveal moment should be made slower/more dramatic if possible in a future version |

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
`[The controller enclosure was designed in Adobe Illutrator and Rhino and cut from 3mm MDF on a laser cutter. 
The top face has two 24.5mm circular holes for the joystick module collars and one 8mm hole 
for the NeoPixel lens. The sides were cut with finger-joint edges and assembled using PVA wood 
glue. A removable bottom panel is held with two M3 screws for electronics access.

The ESP32 DevKit is mounted inside on a small piece of foam to prevent shorts against the MDF. 
Joystick modules are friction-fitted into their holes — the collar provides enough grip without 
adhesive, which keeps them replaceable. Wiring was routed along the inner walls using small 
cable clips cut from excess MDF strips.

The NeoPixel is glued behind its hole with the lens flush to the surface, and a short piece of 
heat-shrink tubing was used as a light diffuser sleeve to soften the point source into an even glow.

All wiring was initially done with  jumper wires on a breadboard for testing. Once confirmed 
working, the circuit was transferred to a small piece of perfboard and soldered. The NeoPixel 
data line includes a 330Ω resistor and the VCC rail has a 100µF capacitor soldered directly at 
the LED pads.

The one-way mirror frame was built from 18mm pine timber offcuts, mitred at the corners and 
glued. The acrylic mirror sheet is held in a rebate routed into the inner face of the frame. 
The iPad sits in a custom MDF cradle behind the frame, angled slightly upward so the reflection 
aligns with the player's eye level at standing height.

Revision: The first enclosure had the joystick holes centred at 40mm from each end — this felt 
too cramped for two-thumb operation. The second version moved them to 50mm from each end 
(100mm centre-to-centre), which was comfortable for all three playtesters.]`

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

<img width="777" height="348" alt="image" src="https://github.com/user-attachments/assets/8deb0c8c-c2a5-4a3d-9e3c-c4e62593c3be" />
<img width="774" height="322" alt="image" src="https://github.com/user-attachments/assets/75966ab4-485e-4fe5-bc34-a6dc5de82fc9" />



```

## 17.3 Version History

| Version | Date | What Changed | Why |
|---|---|---|---|
## 17.3 Version History

| Version | Date | What Changed | Why |
|---|---|---|---|
| v0.1 | Week 1 | Single joystick ADC test | Verify GPIO 32/33 read correctly |
| v0.2 | Week 1 | Added second joystick and NeoPixel | Full hardware bench test |
| v0.3 | Week 2 | BLE send_hold implemented and tested | Core control loop functional |
| v1.0 | Week 3 | Integrated into enclosure; mirror frame built | Full physical build with console structure inetrations and frame dimensions based on mirror size |
| v1.1 | Week 4 | Linger timing and deadzone tuned after playtesting, aletr neopixel reaction time | Responsiveness improvements |


---

# 18. Final Outcome

## 18.1 Final Description
Describe the final version of your project.

**Response:**  
`[The final version of our project evolved into an interactive mirror-cum-screen gaming interface. At first, it functions as a regular mirror, but as the user approaches, it transforms into a digital display hosting an arcade-style game. The gameplay is inspired by a character similar to Batman navigating through a maze-like environment filled with hostile ghost entities. The player uses dual joysticks—one for movement and the other for combat actions like aiming and shooting. The game involves defending against ghosts that attack and poison the player, creating a fast-paced and engaging experience.

To enhance immersion, NeoPixel LED strips are integrated around the mirror, reacting dynamically to player inputs. Each movement or action triggers specific lighting responses, creating a strong connection between physical interaction and visual feedback. The project combines physical controls, digital gameplay, and responsive lighting to create a unique, nostalgic arcade experience.]`

## 18.2 What Works Well
- The system is highly responsive, with immediate feedback to joystick inputs.
- The concept is nostalgic and encourages collaborative and interactive engagement.
- The nostalgic arcade-style gameplay and joystick controls make it intuitive and enjoyable for users.

## 18.3 What Still Needs Improvement
- The game can be expanded into multiple levels with increasing complexity.
- The current gameplay environment is minimal and can be made more detailed and immersive.
- Additional features like varied enemies, power-ups, and sound design could enhance the experience further.

## 18.4 What Changed From the Original Plan
How did the project change from the initial idea?

**Response:**  
`[Initially, the project included an ultrasonic sensor to detect user presence and automatically trigger the game. However, due to repeated ESP32 failures and power limitations, this feature was removed. The system was simplified to run on a single ESP32, which required reducing the number of components and focusing on core gameplay and interaction instead.]`

---

# 19. Reflection

## 19.1 Team Reflection
What did your team do well?  
What slowed you down?  
How well did you manage time, tasks, and responsibilities?

**Response:**  
`[We divided the work cleanly from the start — Ashitha owned all firmware and game logic, 
Varada owned fabrication and circuit assembly — and that split held throughout without 
friction. We were both productive in our own lanes.

What slowed us down most was the GDevelop key-held discovery in Week 2. We had assumed 
the game engine would handle a continuously held BLE key naturally, but it needed explicit 
key-held events instead of key-pressed. Debugging that cost most of one class session.

Time management was solid in Weeks 1–3 but tighter in Week 4 because playtesting feedback 
led to more enclosure changes than expected (joystick labels, hole resizing). We would 
build an earlier cardboard mock-up next time to catch physical ergonomic issues before 
committing to the laser cutter.]`

## 19.2 Technical Reflection
What did you learn about:
- electronics,
- coding,
- mechanisms,
- fabrication,
- integration?

**Response:**  
`[Electronics- We learned that the ESP32's GPIO 34 and 35 are input-only — they have no 
internal pull-up resistors, which is not obvious from the pinout diagram. ADC attenuation 
must be set explicitly to ATTN_11DB for full 0–4095 range on 3.3V. NeoPixel power spikes 
are real and the 100µF capacitor is not optional.

Coding: MicroPython's `struct.pack` approach for BLE HID reports was more reliable than 
higher-level abstractions. Holding keys down by re-sending the same HID report every loop 
(rather than using key-release events) gave smooth, lag-free control. The triangle-wave 
breathing function was simple to write but produced a far more satisfying visual result 
than a simple on/off blink.

Fabrication: Laser-cut MDF is fast but measurements need to account for the kerf 
(~0.2mm) and for real component tolerances — datasheets list nominal dimensions, not 
the actual collar size of a specific batch of HW-504 modules.

Integration: The cleanest decision we made was treating the ESP32 as a plain BLE 
keyboard. It meant zero custom code on the iPad side — GDevelop, iPadOS, and the game 
all worked with it out of the box.]`

## 19.3 Design Reflection
What did you learn about:
- designing for play,
- delight,
- clarity,
- physical interaction,
- player understanding,
- iteration?

**Response:**  
`[Designing for play: The single most important lesson was that physical controls need 
to feel correct before the game feels fun. When the deadzone was at 600, players felt 
the game was ignoring them. Dropping it to 500 made the experience feel responsive and 
respectful of player intent.

Delight: The NeoPixel was originally planned as a secondary feature. After the first 
playtest, it was clearly the thing players commented on most. A small, simple light doing 
one job very visibly creates a disproportionate amount of delight.

Clarity: Two out of three first-time players ignored the right joystick entirely. No 
matter how logical a control scheme seems to the designer, players need physical or visual 
cues. Printed labels resolved this immediately — we should have included them from day one.

Iteration:The second enclosure was significantly better than the first. Building 
something physical once, getting it wrong, and fixing it is faster and more informative 
than trying to perfect it in CAD.]`

## 19.4 If You Had One More Week
What would you improve next?

**Response:**  
`[Write here]`

---

# 20. Final Submission Checklist

Before submission, confirm that:
- [x] Team details are complete
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
