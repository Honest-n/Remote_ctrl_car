input.onButtonPressed(Button.A, function () {
    Speed = 0
    Rotation2 = -100
})
function Brake () {
    if (Speed >= 10) {
        Speed += -10
    } else {
    	
    }
}
input.onButtonPressed(Button.AB, function () {
    Speed = 0
    Rotation2 = 0
})
input.onButtonPressed(Button.B, function () {
    Speed = 0
    Rotation2 = 100
})
control.onEvent(EventBusSource.MES_DPAD_CONTROLLER_ID, EventBusValue.MICROBIT_EVT_ANY, function () {
    if (control.eventValue() == EventBusValue.MES_DPAD_BUTTON_D_DOWN) {
        Speed = 0
    }
    if (control.eventValue() == EventBusValue.MES_DPAD_BUTTON_1_DOWN) {
        Speed += 10
    }
    if (control.eventValue() == EventBusValue.MES_DPAD_BUTTON_2_DOWN) {
        Brake()
    }
    if (control.eventValue() == EventBusValue.MES_DPAD_BUTTON_3_DOWN) {
        Rotation2 += -10
    }
    if (control.eventValue() == EventBusValue.MES_DPAD_BUTTON_4_DOWN) {
        Rotation2 += 10
    }
    if (control.eventValue() == EventBusValue.MES_DPAD_BUTTON_A_DOWN) {
        Headlights.setBrightness(20)
        music.playSoundEffect(music.builtinSoundEffect(soundExpression.hello), SoundExpressionPlayMode.InBackground)
        basic.pause(100)
        Headlights.setBrightness(10)
    }
})
let Rotation2 = 0
let Speed = 0
let Headlights: neopixel.Strip = null
let strip = neopixel.create(DigitalPin.P0, 10, NeoPixelMode.RGB)
let Brakelights = strip.range(5, 2)
Headlights = strip.range(0, 2)
Brakelights.setBrightness(10)
Headlights.setBrightness(10)
Headlights.showColor(neopixel.colors(NeoPixelColors.White))
Brakelights.showColor(neopixel.colors(NeoPixelColors.Red))
Speed = 0
Rotation2 = 0
basic.forever(function () {
	
})
basic.forever(function () {
    servos.P1.run(Rotation2 + Speed)
    servos.P2.run(Rotation2 - Speed)
})
