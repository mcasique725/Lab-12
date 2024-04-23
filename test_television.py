import pytest
from television import Television


# Test init method
def test_init():
    tv = Television()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"  # Check initial values


# Test power method
def test_power():
    tv = Television()
    tv.power()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"   # Check when TV is on
    tv.power()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"  # Check when TV is off


# Test mute method
def test_mute():
    tv = Television()
    tv.volume_up()  # Increase volume once
    tv.mute()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"  # Check when TV is off and muted
    tv.power()      # Turn on TV
    tv.mute()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"   # Check when TV is on and muted
    tv.mute()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"   # Check when TV is on and unmuted


# Test channel_up method
def test_channel_up():
    tv = Television()
    tv.channel_up()     # Increase channel from 0 to 1
    assert str(tv) == "Power = False, Channel = 1, Volume = 0"  # Check when TV is off
    tv.power()          # Turn on TV
    tv.channel_up()     # Increase channel from 0 to 1
    assert str(tv) == "Power = True, Channel = 1, Volume = 0"   # Check when TV is on
    for _ in range(3):  # Increase channel past max value (3)
        tv.channel_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"   # Check when channel loops to min value


# Test channel_down method
def test_channel_down():
    tv = Television()
    tv.channel_down()   # Decrease channel from 0 to 3
    assert str(tv) == "Power = False, Channel = 3, Volume = 0"  # Check when TV is off
    tv.power()          # Turn on TV
    tv.channel_down()   # Decrease channel from 0 to 3
    assert str(tv) == "Power = True, Channel = 3, Volume = 0"   # Check when TV is on
    for _ in range(4):  # Decrease channel past min value (0)
        tv.channel_down()
    assert str(tv) == "Power = True, Channel = 3, Volume = 0"   # Check when channel loops to max value


# Test volume_up method
def test_volume_up():
    tv = Television()
    tv.volume_up()      # Increase volume from 0 to 1
    assert str(tv) == "Power = False, Channel = 0, Volume = 1"  # Check when TV is off
    tv.power()          # Turn on TV
    tv.volume_up()      # Increase volume from 0 to 1
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"   # Check when TV is on
    tv.mute()           # Mute TV
    tv.volume_up()      # Try increasing volume when muted
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"   # Check volume remains 0 when muted
    tv.mute()           # Unmute TV
    for _ in range(3):  # Increase volume past max value (2)
        tv.volume_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 2"   # Check when volume reaches max value


# Test volume_down method
def test_volume_down():
    tv = Television()
    tv.volume_down()    # Decrease volume from 0 to 2
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"  # Check when TV is off
    tv.power()          # Turn on TV
    tv.volume_down()    # Decrease volume from 0 to 2
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"   # Check when TV is on
    tv.mute()           # Mute TV
    tv.volume_down()    # Try decreasing volume when muted
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"   # Check volume remains 0 when muted
    tv.mute()           # Unmute TV
    tv.volume_up()      # Increase volume to max (2)
    tv.volume_down()    # Decrease volume from 2 to 1
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"   # Check when volume is decreased
    for _ in range(2):  # Decrease volume past min value (0)
        tv.volume_down()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"   # Check when volume reaches min value
