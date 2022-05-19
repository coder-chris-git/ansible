#!/usr/bin/python
# -*- coding: utf-8 -*-

from ansible.module_utils.basic import *

class custom_if_config():
    

    def __init__(self):
 
        # create Dictionaries usually when the dict is lengthy or nested


        # set dictiornaires to Ansible agruement spec  or add directly

        self.module = AnsibleModule(argument_spec=dict(

            #add dict to list from var
        
           
                option = dict(),
                dest = dict()


        ))







    def main(self):
        if_config = self.module.params
        option = if_config['option']
        dest = if_config['dest']
        
        cmd = "ifconfig > {0}/ifconfig.out".format(dest)

        if option and option =='all':
             cmd = "-a >".join(cmd.split(">"))

        if option and option =='eth0':
          cmd = "-a >".join(cmd.split(">"))
        
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


    

if __name__ == '__main__':
    run_cmd = custom_if_config()
    run_cmd.main()
