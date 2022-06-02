    # Created by Bischofberger David

from random import random
from time import sleep
# DEBUG, can be removed from fetchSensorValue() when shipping

def getParameters( intern_Tu, intern_Tg ):
    """returns the PI system parameters of the current system as a tuple: '( Kp, Ti )'."""

    # changeable parameters:
    intern_Kp  =   (   0.6 * intern_Tg    )   /  (   intern_Tu * intern_Tg    )
    intern_Ti  =   (   4   * intern_Tu    )   /   intern_Kp

    return (intern_Kp, intern_Ti)

def getResponse( error, error_before, sysParam ):
    """returns the PI system reaction of the current system as tuple."""


    ( intern_Kp, intern_Ti )   =   sysParam     #: unpacking sysParam

    internPResponse =   intern_Kp * error
    internIResponse =   intern_Ti * (error + error_before)

    return ( internPResponse + internIResponse )

def fetchSensorValue(channel):
    """expects channel as integer argument, fetches sensor value over SPI from ADC."""
    return random()

"""main code:"""
sysParam    = getParameters(1, 5)
e_b         = 0
targetValue = 20
Ks          = 2.2

while True:
    e = targetValue/fetchSensorValue(channel = 0)

    print(
        str(
            Ks * getResponse(e, e_b, sysParam)
        )
    )

    e_b = e
    sleep(.05)