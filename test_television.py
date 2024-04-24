import pytest
from television import *


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
    tv.power()          # Turn on TV
    tv.volume_up()      # Increase volume once
    tv.mute()           # Mute TV
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"
    # Test when TV is on and unmuted
    tv.mute()           # Unmute TV
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"  # Check unmuted state and volume retained
    # Test when TV is off and muted
    tv.power()          # Turn off TV
    tv.mute()           # Mute TV
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"  # Check muted state when TV is off

    # Test when TV is off and unmuted
    tv.mute()           # Unmute TV
    assert str(tv) == "Power = False, Channel = 0, Volume = 1"  # Check unmuted state when TV is off


def test_channel_up():
    tv = Television()
    tv.channel_up()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"
    tv.power()
    tv.channel_up()
    assert str(tv) == "Power = True, Channel = 1, Volume = 0"
    tv.channel_up()
    tv.channel_up()
    tv.channel_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"


def test_channel_down():
    tv = Television()
    tv.channel_down()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"
    tv.power()
    tv.channel_down()
    assert str(tv) == "Power = True, Channel = 3, Volume = 0"


def test_volume_up():
    tv = Television()
    tv.volume_up()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"
    tv.power()
    tv.volume_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"
    tv.mute()
    tv.volume_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 2"
    tv.volume_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 2"


def test_volume_down():
    tv = Television()
    tv.volume_down()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"
    tv.power()
    tv.volume_up()
    tv.volume_up()
    tv.volume_down()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"
    tv.mute()
    tv.volume_down()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"
    tv.volume_down()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"


if __name__ == "__main__":
    pytest.main()
