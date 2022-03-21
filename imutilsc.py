#!/usr/bin/python
# -*- coding: utf-8 -*-
import subprocess
import os
from ansible.module_utils.basic import *


class imutilsc():
    module = None,
    module_facts = dict(username=None, stdout=None, stderr=None)

    def __init__(self):
        source_default = "/opt/IBM/InstallationManager/eclipse/tools/imutilsc"

        # create Dictionaries

        encryptString = dict(type='dict', options=dict(
                str = dict(required = True),
                source = dict(default=source_default)))
        get = dict(type='str')
        saveCredentials = dict(type='dict',options=dict(
                username=dict(required=True),
                password=dict(required=True),
                url=dict(default = 'http://www.ibm.com/software/repositorymanager/entitled/repository.xml'),
                source=dict(default=source_default)))
#       set dictiornaires to Ansible agruement spec
        self.module = AnsibleModule(argument_spec=dict(
            #add dict to list
            saveCredentials=dict(**saveCredentials),
            encryptString =dict(**encryptString),
            get=dict(**get)

        ))

    #functions using module params
    def subpro(self,cmd,msg):
        child = subprocess.Popen([
            cmd
        ],
                                 shell=True,
                                 stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE)
        stdout_value, stderr_value = child.communicate()
        # Read arguments

        if child.returncode != 0:
            self.module.fail_json(msg="failed",
                                   stderr=stderr_value,
                                   stdout=stdout_value)
        self.module.exit_json(changed=True, stdout=stdout_value)
    def encryptString(self,module_params):
        encryptString = module_params.get('encryptString')
        source = encryptString['source']
        str = encryptString['str']
        cmd = source + " encryptString " + str
        msg = str
        self.subpro(cmd,msg)



    def saveCredentials(self, module_params):
        saveCredentials = module_params.get('saveCredentials')

        username = saveCredentials['username']
        password = saveCredentials['password']
        url = saveCredentials['url']
        source = saveCredentials['source']

        cmd =  source + ' saveCredential -url ' + url + ' -userName ' + username + ' -userPassword ' + password
        msg = saveCredentials

        self.subpro(cmd,msg)

    def get(self,module_params):
        name = module_params['get']
        source = "/opt/IBM/InstallationManager/eclipse/tools/imutilsc"


        cmd = source + " " +  name
        msg =  "uddsd"
        self.subpro(cmd,msg)

    def main(self):
        if self.module.params['saveCredentials']:
            self.saveCredentials(self.module.params)
        if self.module.params['encryptString']:
            self.encryptString(self.module.params)
        if self.module.params['get']:
            self.get(self.module.params)
if __name__ == '__main__':
    imutilsc = imutilsc()
    imutilsc.main()
