def on_button_pressed_a():
    global Speed, Rotation2
    Speed = 0
    Rotation2 = -100
input.on_button_pressed(Button.A, on_button_pressed_a)

def Brake():
    global Speed
    if Speed >= 10:
        Brakelights.set_brightness(20)
        Speed += -10
        Brakelights.set_brightness(10)
    else:
        Brakelights.set_brightness(20)
        Brakelights.set_brightness(10)

def on_button_pressed_ab():
    global Speed, Rotation2
    Speed = 0
    Rotation2 = 0
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global Speed, Rotation2
    Speed = 0
    Rotation2 = 100
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_mes_dpad_controller_id_microbit_evt():
    global Speed, Rotation2
    if control.event_value() == EventBusValue.MES_DPAD_BUTTON_D_DOWN:
        music.play_sound_effect(music.builtin_sound_effect(soundExpression.hello),
            SoundExpressionPlayMode.UNTIL_DONE)
    if control.event_value() == EventBusValue.MES_DPAD_BUTTON_1_DOWN:
        Speed += 10
    if control.event_value() == EventBusValue.MES_DPAD_BUTTON_2_DOWN:
        Brake()
    if control.event_value() == EventBusValue.MES_DPAD_BUTTON_3_DOWN:
        Rotation2 += -10
    if control.event_value() == EventBusValue.MES_DPAD_BUTTON_4_DOWN:
        Rotation2 += 10
    if control.event_value() == EventBusValue.MES_DPAD_BUTTON_A_DOWN:
        Headlights.set_brightness(20)
        Headlights.set_brightness(10)
control.on_event(EventBusSource.MES_DPAD_CONTROLLER_ID,
    EventBusValue.MICROBIT_EVT_ANY,
    on_mes_dpad_controller_id_microbit_evt)

Rotation2 = 0
Speed = 0
Brakelights: neopixel.Strip = None
Headlights: neopixel.Strip = None
strip = neopixel.create(DigitalPin.P0, 10, NeoPixelMode.RGB)
Headlights = strip.range(8, 2)
Brakelights = strip.range(3, 2)
Brakelights.set_brightness(10)
Headlights.set_brightness(10)
Headlights.show_color(neopixel.colors(NeoPixelColors.WHITE))
Brakelights.show_color(neopixel.colors(NeoPixelColors.RED))
Speed = 0
Rotation2 = 0

def on_forever():
    servos.P1.run(Rotation2 + Speed)
    servos.P2.run(Rotation2 - Speed)
basic.forever(on_forever)

def on_forever2():
    pass
basic.forever(on_forever2)
