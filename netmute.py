#!/usr/bin/env python

import subprocess as sp
import time

current_ssid = None


def get_wlan0_network_ssid() -> str:
    command = "nmcli c show --active | grep \"wlan0\" | awk '{print $1}'"
    result = sp.run(command, shell=True, capture_output=True)
    return bytes.decode(result.stdout).replace("\n", "")


def mute_audio():
    command = "amixer set Master mute"
    sp.run(command, shell=True)


def unmute_audio():
    command = "amixer set Master unmute"
    sp.run(command, shell=True)


def poll_network_and_set_audio():
    global current_ssid

    muted_networks = [
        "eduroam",
        "MUW-NET",
        "OnePluz 6",
    ]

    ssid = get_wlan0_network_ssid()

    if current_ssid == ssid:
        return  # We don't wanna set it over and over again.

    current_ssid = ssid

    if not ssid:
        return  # we don't change anything.

    if ssid in muted_networks:
        mute_audio()
    else:
        unmute_audio()


if __name__ == "__main__":
    print("==Netmute==")
    while True:
        time.sleep(5.0)
        poll_network_and_set_audio()
