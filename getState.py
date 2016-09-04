#!/usr/bin/python

import os
import sys
import json
from pySwitcher import pySwitcher

def main(argv):
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    settingsPath = os.path.join(__location__, 'settings.json')

    with open(settingsPath) as settings_file:
        settings = json.load(settings_file)

    assert(settings['username'] != ''), 'missing Username in settings.json'
    assert(settings['password'] != ''), 'missing Password in settings.json'

    switch = pySwitcher()
    switch.login(settings['username'], settings['password'])

    state = switch.getState()
    print state

    if(state == 'on'):
        sys.exit(0)
    else:
        sys.exit(1)

if __name__ == "__main__":
   main(sys.argv[1:])