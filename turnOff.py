#!/usr/bin/python

import sys
import json
from pySwitcher import pySwitcher

def main(argv):
    with open('settings.json') as settings_file:
        settings = json.load(settings_file)

    assert(settings['username'] != ''), 'missing Username in settings.json'
    assert(settings['password'] != ''), 'missing Password in settings.json'

    switch = pySwitcher()
    switch.login(settings['username'], settings['password'])

    result = switch.turnOff()

    if(result == True):
        sys.exit(0)
    else:
        sys.exit(1)

if __name__ == "__main__":
   main(sys.argv[1:])