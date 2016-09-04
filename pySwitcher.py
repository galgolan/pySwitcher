import requests
import json

class pySwitcher(object):

    def __init__(self):        
        self.token = ''
        self.baseUri = 'http://server.switcher.co.il/Switcher/'
        self.userAgent = 'Switcher/1.0 CFNetwork/758.5.3 Darwin/15.6.0'
        self.headers = {'user-agent': self.userAgent}
        self.postHeaders = {'user-agent': self.userAgent, 'Content-Type': 'application/x-www-form-urlencoded'}
        self.switchId = ''

    def getSwitch(self):
        assert(self.token != ''), 'Not logged in!'

        req = requests.get(self.baseUri + 'appServiceGetSwitches', params={'token':self.token}, headers=self.headers)
        res = json.loads(req.text)
        if(res['errorCode'] == 0):
            switchId = res['switches'][0]
        else:
            switchId = ''

        return switchId

    def login(self, username, password):
        assert(username != ''), 'Invalid Username!'
        assert(password != ''), 'Invalid Password!'

        payload = {'password': password, 'account_pid': username, 'item_id': 'iPhone_app_id', 'device_info': {'duid':'4B7299E2-2677-43AC-BE40-A3CC5E5F700B','versions':{'software':'iphone_app'}}}
        req = requests.post(self.baseUri + 'loginApp', data=json.dumps(payload), headers = self.postHeaders)
        res = json.loads(req.text)
        if(res['errorCode'] == 0):
            self.token = res['token']
        else:
            self.token = ''

        self.switchId = self.getSwitch()

    def getState(self):
        assert(self.token != ''), 'Not logged in!'
        assert(self.switchId != ''), 'Cant get switch associated with the user!'

        serviceParams = {'token':self.token,'switchId':self.switchId}
        req = requests.get(self.baseUri + 'appServiceGetSwitchState', params=serviceParams, headers=self.headers)
        res = json.loads(req.text)
        if(res['errorCode'] == 0):
            state = res['state']
        else:
            state = ''
        
        return state

    def turnOn(self):
        assert(self.token != ''), 'Not logged in!'
        assert(self.switchId != ''), 'Cant get switch associated with the user!'

        serviceParams = {'token':self.token,'switchId':self.switchId, 'state':'on'}
        req = requests.get(self.baseUri + 'appServiceSetSwitchState', params=serviceParams, headers=self.headers)
        res = json.loads(req.text)
        return res['errorCode'] == 0 and res['state'] == 'on'

    def turnOff(self):
        assert(self.token != ''), 'Not logged in!'
        assert(self.switchId != ''), 'Cant get switch associated with the user!'
        
        serviceParams = {'token':self.token,'switchId':self.switchId, 'state':'off'}
        req = requests.get(self.baseUri + 'appServiceSetSwitchState', params=serviceParams, headers=self.headers)
        res = json.loads(req.text)
        return res['errorCode'] == 0 and res['state'] == 'off'