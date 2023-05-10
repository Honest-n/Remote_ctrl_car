def Reset():
    global Reverse, Speed, Rotation2, strip, Brakelights, Headlights
    Reverse = False
    Speed = 0
    Rotation2 = 0
    strip = neopixel.create(DigitalPin.P0, 10, NeoPixelMode.RGB)
    Brakelights = strip.range(5, 2)
    Headlights = strip.range(0, 2)
    strip.set_brightness(10)
    Headlights.show_color(neopixel.colors(NeoPixelColors.WHITE))
    Brakelights.show_color(neopixel.colors(NeoPixelColors.RED))

def on_mes_dpad_controller_id_microbit_evt():
    global Speed, Reverse, Rotation2
    if control.event_value() == EventBusValue.MES_DPAD_BUTTON_1_DOWN:
        if Reverse == True:
            Speed += -10
        else:
            Speed += 10
    else:
        if control.event_value() == EventBusValue.MES_DPAD_BUTTON_2_DOWN:
            if Speed != 0:
                if Reverse == True:
                    Speed += 10
                else:
                    Speed += 0 - 10
            elif Reverse == False:
                Reverse = True
                Brakelights.show_color(neopixel.colors(NeoPixelColors.WHITE))
            else:
                Reverse = False
                Brakelights.show_color(neopixel.colors(NeoPixelColors.RED))
        else:
            if control.event_value() == EventBusValue.MES_DPAD_BUTTON_3_DOWN:
                Rotation2 += -10
            else:
                if control.event_value() == EventBusValue.MES_DPAD_BUTTON_4_DOWN:
                    Rotation2 += 10
                else:
                    if control.event_value() == EventBusValue.MES_DPAD_BUTTON_A_DOWN:
                        pass
                    else:
                        if control.event_value() == EventBusValue.MES_DPAD_BUTTON_D_DOWN:
                            Reset()
    servos.P2.run(Rotation2 - Speed)
    servos.P1.run(Rotation2 + Speed)
control.on_event(EventBusSource.MES_DPAD_CONTROLLER_ID,
    EventBusValue.MICROBIT_EVT_ANY,
    on_mes_dpad_controller_id_microbit_evt)

Headlights: neopixel.Strip = None
Brakelights: neopixel.Strip = None
strip: neopixel.Strip = None
Rotation2 = 0
Speed = 0
Reverse = False
Reset()