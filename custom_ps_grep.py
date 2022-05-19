#!/usr/bin/python
# -*- coding: utf-8 -*-

from ansible.module_utils.basic import *

class run_cmd():
    

    def __init__(self):
             
    #subpro function exits module with json response
       
        # create Dictionaries usually when the dict is lengthy or nested


        # set dictiornaires to Ansible agruement spec  or add directly

        self.module = AnsibleModule(argument_spec=dict(

            #add dict to list from var
                name = dict(),
                sort = dict(),
                awk =  dict(),
                dest = dict(),
                count = dict(type='bool'),
                v_grep = dict(type='bool'),
                user = dict()

        ))




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
            stdout_value = "none"
            self.module.exit_json(changed=True, stdout=stdout_value)
        self.module.exit_json(changed=True, stdout=stdout_value)

    def ps_grep(self,module_params):
        name = module_params['name']
        user = module_params['user']
        sort = module_params['sort']
        awk = module_params['awk']
        dest = module_params['dest']
        count = module_params['count']
        v_grep = module_params['v_grep']

        
        cmd = "ps -ef | grep {0} > {1}/{0}.out".format(name,dest)

        if v_grep:
             cmd = "| grep -v grep >".join(cmd.split(">"))
        if sort:
            cmd = "ps -ef | grep {0} | sort -k {1} > {2}/{0}_sort.out".format(name,sort,dest)
        if count:
            cmd = "| wc -l >".join(cmd.split(">"))
            cmd= "_number_process_running.out".join(cmd.split(".out"))

           
        if awk:
            cmd = "ps -ef | grep " + name + " | awk '{ print $" + awk + " }' > " + name+"jhj.out"


        msg =  cmd
        self.subpro(cmd,msg)

    def main(self):
            self.ps_grep(self.module.params)

if __name__ == '__main__':
    run_cmd = run_cmd()
    run_cmd.main()
