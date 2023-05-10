function Reset () {
    Reverse = false
    Speed = 0
    Rotation2 = 0
    strip = neopixel.create(DigitalPin.P0, 10, NeoPixelMode.RGB)
    Brakelights = strip.range(5, 2)
    Headlights = strip.range(0, 2)
    strip.setBrightness(10)
    Headlights.showColor(neopixel.colors(NeoPixelColors.White))
    Brakelights.showColor(neopixel.colors(NeoPixelColors.Red))
}
control.onEvent(EventBusSource.MICROBIT_ID_BUTTON_A, EventBusValue.MICROBIT_EVT_ANY, function () {
    while (control.eventValue() == EventBusValue.MES_DPAD_BUTTON_1_DOWN && Speed < 100) {
        if (Reverse == true) {
            Speed += -10
        } else {
            Speed += 10
        }
        basic.pause(10)
    }
    while (control.eventValue() == EventBusValue.MES_DPAD_BUTTON_2_DOWN) {
        if (Speed != 0) {
            if (Reverse == true) {
                Speed += 10
            } else {
                Speed += -10
            }
        } else if (Reverse == false) {
            Reverse = true
            Brakelights.showColor(neopixel.colors(NeoPixelColors.White))
            break;
        } else {
            Reverse = false
            Brakelights.showColor(neopixel.colors(NeoPixelColors.Red))
            break;
        }
        basic.pause(10)
    }
    while (control.eventValue() == EventBusValue.MES_DPAD_BUTTON_3_DOWN && Rotation2 > -100) {
        Rotation2 += -10
        basic.pause(10)
    }
    while (control.eventValue() == EventBusValue.MES_DPAD_BUTTON_4_DOWN && Rotation2 < 100) {
        Rotation2 += 10
        basic.pause(10)
    }
    if (control.eventValue() == EventBusValue.MES_DPAD_BUTTON_A_DOWN) {
        Reset()
    } else if (control.eventValue() == EventBusValue.MES_DPAD_BUTTON_D_DOWN) {
        music.playSoundEffect(music.builtinSoundEffect(soundExpression.mysterious), SoundExpressionPlayMode.UntilDone)
        basic.pause(50)
    }
})
let Headlights: neopixel.Strip = null
let Brakelights: neopixel.Strip = null
let strip: neopixel.Strip = null
let Rotation2 = 0
let Speed = 0
let Reverse = false
Reset()
basic.forever(function () {
    let R_speed = 0
    let L_speed = 0
    servos.P1.run(L_speed)
    servos.P2.run(R_speed)
})
control.inBackground(function () {
    control.waitForEvent(EventBusSource.MES_DPAD_CONTROLLER_ID, EventBusValue.MES_DPAD_BUTTON_1_DOWN)
})
