Servos8 Hat
===========

.. include:: ../refs/hat.servo8.ref

8Servos HAT v1.1 is an 8-channel servo driver module that works with the
M5StickC/C Plus series. Adopt STM32F030F4 as main controller to drive servos
with PWM (Pulse Width Modulation) signal. I2C communication. Embedded power
management circuit to control servo ON/OFF with programming. With the
rechargeable 16340 lithium battery (with the capacity of 700mAh),It also
supports 18350 lithium batteries, it can support Maximum 1.3A load. Applied for
robotic and DIY projects.


Support the following products:

    |Servo8|


Micropython Example::

    import os, sys, io
    import M5
    from M5 import *
    from hardware import *
    from hat import Servos8Hat
    i2c0 = I2C(0, scl=Pin(26), sda=Pin(0), freq=100000)
    servo = Servos8Hat(i2c0, 0x36)
    servo.power_on()
    for i in range(1, 9):
    servo.write_servo_angle(i, 90)
    servo.power_off()


.. only:: builder_html


class Servos8Hat
----------------

Constructors
-------------

.. method:: Servos8Hat(i2c: I2C, address: int | list | tuple = 0x36)

    Initialize the Servos8Hat.

    - ``i2c``: I2C port to use.
    - ``address``: I2C address of the servo8.

    UIFLOW2:

        |init.png|


Methods
-------

.. method:: Servos8Hat.write_servo_angle(ch, angle)

    Set the angle of the servo.

    - ``ch``: The channel (1 to 8) of the servo.
    - ``angle``: The angle (0 to 180) of the servo.

    UIFLOW2:

        |write_servo_angle.png|


.. method:: Servos8Hat.read_servo_angle(ch)

    Read the angle of the servo.

    - ``ch``: The channel (1 to 8) of the servo.

    UIFLOW2:

        |read_servo_angle.png|


.. method:: Servos8Hat.write_servo_pulse(ch, pulse)

    Set the pulse of the servo.

    - ``ch``: The channel (1 to 8) of the servo.
    - ``pulse``: The pulse (500 to 2500) of the servo.

    UIFLOW2:

        |write_servo_pulse.png|


.. method:: Servos8Hat.read_servo_pulse(ch)

    Read the pulse of the servo.

    - ``ch``: The channel (1 to 8) of the servo.

    UIFLOW2:

        |read_servo_pulse.png|


.. method:: Servos8Hat.power_ctrl(state)

    Control the power of the servo.

    - ``state``: The state of the power, 0 for OFF and 1 for ON.

    UIFLOW2:

        |power_ctrl.png|


.. method:: Servos8Hat.power_on()

    Turn on the power of the servo.

    UIFLOW2:

        |power_on.png|


.. method:: Servos8Hat.power_off()

    Turn off the power of the servo.

    UIFLOW2:

        |power_off.png|


.. method:: Servos8Hat.get_power_state()

    Get the state of the power of the servo.

    UIFLOW2:

        |get_power_state.png|
