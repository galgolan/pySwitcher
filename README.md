# pySwitcher
(Unofficial) Python API for Switcher - Dud boiler home automation switch http://www.switcher.co.il/

Required Packages
-----------------
* requests - http://docs.python-requests.org/en/master/user/install/#install

Usage
----------------

```python
from pySwitcher import pySwitcher
switch = pySwitcher()
switch.login('USERNAME', 'PASSWORD')
switch.getState()   # returns 'on' or 'off'
switch.turnOn()     # returns True/False to indicate success/failure
switch.turnOff()    # returns True/False to indicate success/failure
```

Command Line Usage
------------------
Provided for easy integration with some home automation servers, such as: https://home-assistant.io/

Edit **settings.json** with your username & password. The following scripts are available:

Print the current state of the switch (Exit code is 0 when switch is on, non-zero when off):
```
$ getState.py
```

Turns the switch on:
```
$ turnOn.py
```

Turns the switch off:
```
$ turnOff.py
```
