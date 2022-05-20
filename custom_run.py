#!/usr/bin/python
# -*- coding: utf-8 -*-

from ansible.module_utils.basic import *

class custom_run():
    
    def __init__(self):
             
        self.module = AnsibleModule(argument_spec=dict(

                cmd = dict(),

        ))

    def main(self):
        cmd = self.module.params['cmd']
    

        child = subprocess.Popen([cmd],shell=True,stdout=subprocess.PIPE,)
        stdout_value, stderr_value = child.communicate()

    

        self.module.exit_json(changed=True, stdout=stdout_value)

if __name__ == '__main__':
    run= custom_run()
    run.main() 
