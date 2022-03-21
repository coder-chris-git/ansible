#!/usr/bin/python
# -*- coding: utf-8 -*-

from ansible.module_utils.basic import *


class imutilsc():
    module = None,

    def __init__(self):

        # set Dict to variable 
        
        saveCredential = dict(type='dict',options=dict(
                username=dict(required=True),
                password=dict(required=True),
                url=dict(default = 'http://www.ibm.com/software/repositorymanager/entitled/repository.xml'),
        ))

        # add dict to Ansible agruement spec by variables created above or by adding them directly.

        self.module = AnsibleModule(argument_spec=dict(

            #add dict to arguement spec from var

            saveCredential=dict(**saveCredential),

            #add directly

            encryptString =dict(type='str'),
            get=dict(type='str'),
            source=dict(type='str', default="/opt/IBM/InstallationManager/eclipse/tools/imutilsc")
        ))

    #subpro function exists the module with json response 

    def subpro(self,cmd,msg):
        child = subprocess.Popen([
            cmd
        ],
            shell=True  
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)
            stdout_value, stderr_value = child.communicate()
        # Read arguments

        if child.returncode != 0:
            self.module.fail_json(msg="failed",
            stderr=stderr_value,
            stdout=stdout_value)
        self.module.exit_json(changed=True, stdout=stdout_value)

    # imutilsc encrypt string command
   
    def encryptString(self,module_params):
        encryptString = module_params['encryptString']
        source = module_params['source']
        cmd = source + " encryptString " + encryptString
        msg = encryptString
        self.subpro(cmd,msg)


    # imutilsc save credential command
    
    def saveCredential(self, module_params):
        saveCredential = module_params.get('saveCredential')

        username = saveCredential['username']
        password = saveCredential['password']
        url = saveCredential['url']
        source = module_params['source']

        cmd =  source + ' saveCredential -url ' + url + ' -userName ' + username + ' -userPassword ' + password
        msg = saveCredential

        self.subpro(cmd,msg)
       
    # command used call help and or version command 
   
    def get(self,module_params):
        name = module_params['get']
        source = module_params['source']


        cmd = source + " " +  name
        msg =  "uddsd"
        self.subpro(cmd,msg)

    # call function based on user parameters
    
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

