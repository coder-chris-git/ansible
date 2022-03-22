#!/usr/bin/python
# -*- coding: utf-8 -*-

from ansible.module_utils.basic import *


class imutilsc():
    module = None,

    def __init__(self):

        # create Dictionaries usually when the dict is lengthy or nested

        saveCredential = dict(type='dict',options=dict(
                username=dict(required=True),
                password=dict(required=True),
                url=dict(default = 'http://www.ibm.com/software/repositorymanager/entitled/repository.xml'),
        ))

        # set dictiornaires to Ansible agruement spec  or add directly

        self.module = AnsibleModule(argument_spec=dict(

            #add dict to list from var

            saveCredential=dict(**saveCredential),

            #add directly

            encryptString =dict(type='str'),
            get=dict(type='str',choices=['help','version']),
            source=dict(type='str', default="/opt/IBM/InstallationManager/eclipse/tools/imutilsc")
        ))

    #subpro function exits module with json response

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
        encryptString = module_params['encryptString']
        source = module_params['source']
        cmd = source + " encryptString " + encryptString
        msg = encryptString
        self.subpro(cmd,msg)



    def saveCredential(self, module_params):
        saveCredential = module_params.get('saveCredential')

        username = saveCredential['username']
        password = saveCredential['password']
        url = saveCredential['url']
        source = module_params['source']

        cmd =  source + ' saveCredential -url ' + url + ' -userName ' + username + ' -userPassword ' + password
        msg = saveCredential

        self.subpro(cmd,msg)

    def get(self,module_params):
        name = module_params['get']
        source = module_params['source']


        cmd = source + " " +  name
        msg =  "uddsd"
        self.subpro(cmd,msg)

    def main(self):
        if self.module.params['saveCredential']:
            self.saveCredential(self.module.params)
        if self.module.params['encryptString']:
            self.encryptString(self.module.params)
        if self.module.params['get']:
            self.get(self.module.params)
if __name__ == '__main__':
    imutilsc = imutilsc()
    imutilsc.main()

