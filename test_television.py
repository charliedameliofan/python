import pytest
from television import Television


def test_init_state():
    my_tv = Television()
    # default is powered off (False), channel 0, volume 0
    expected = "Power = False, Channel = 0, Volume = 0"
    assert str(my_tv) == expected


def test_power_toggle():
    my_tv = Television()
    my_tv.power()  # turn on
    assert "Power = True" in str(my_tv)
    my_tv.power()  # turn off
    assert "Power = False" in str(my_tv)


def test_channel_operations_only_when_on():
    my_tv = Television()
    my_tv.channel_up()
    assert "Channel = 0" in str(my_tv)

    my_tv.power()
    my_tv.channel_up()  # 0 -> 1
    assert "Channel = 1" in str(my_tv)
    my_tv.channel_up()  # 1 -> 2
    my_tv.channel_up()  # 2 -> 3
    assert "Channel = 3" in str(my_tv)
    my_tv.channel_up()  # 3 -> 0
    assert "Channel = 0" in str(my_tv)

    my_tv.channel_down() #0 - 3
    assert "Channel = 3" in str(my_tv)


def test_volume_up_down_and_mute_behavior():
    my_tv = Television()
    my_tv.volume_up()
    assert "Volume = 0" in str(my_tv)

    # turn on and increase volume step by step
    my_tv.power()
    my_tv.volume_up()
    assert "Volume = 1" in str(my_tv)
    my_tv.volume_up()
    assert "Volume = 2" in str(my_tv)
    # at max volume, should stay the same
    my_tv.volume_up()
    assert "Volume = 2" in str(my_tv)

    # muting should display volume as 0 but internal volume is kept
    my_tv.mute()
    assert "Volume = 0" in str(my_tv)

    # lowering volume when muted should unmute and decrease
    my_tv.volume_down()
    assert "Volume = 1" in str(my_tv)

    # keep decreasing until we hit the minimum
    my_tv.volume_down()
    assert "Volume = 0" in str(my_tv)
    my_tv.volume_down()
    assert "Volume = 0" in str(my_tv)


def test_mute_only_works_when_on():
    # mute = nothing when tv off
    my_tv = Television()
    my_tv.mute()
    assert "Volume = 0" in str(my_tv)

    # when the TV is on, mute works
    my_tv.power()
    my_tv.mute()
    assert "Volume = 0" in str(my_tv)
    my_tv.mute()  # unmute
    assert "Volume = 0" in str(my_tv)
