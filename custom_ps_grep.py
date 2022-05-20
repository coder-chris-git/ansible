#!/usr/bin/python
# -*- coding: utf-8 -*-

from ansible.module_utils.basic import *

class custom_ps_grep():
    
    def __init__(self):
             
        self.module = AnsibleModule(argument_spec=dict(

                name = dict(),
                sort = dict(),
                awk =  dict(),
                dest = dict(),
                count = dict(type='bool'),
                v_grep = dict(type='bool'),
                user = dict()

        ))

    def main(self):

        ps_grep = self.module.params

        name = ps_grep['name']
        user = ps_grep['user']
        sort = ps_grep['sort']
        awk = ps_grep['awk']
        dest = ps_grep['dest']
        count = ps_grep['count']
        v_grep = ps_grep['v_grep']

        path = str(dest) + "/" + str(name)+".out"
        cmd = "ps -ef | grep " + name

        if user:
            cmd += " | grep {}".format(name)

        if v_grep:
            cmd += "| grep -v grep"

        if sort:
            path = "{0}/{1}_sort.out".format(dest,name)
            cmd +=" | sort -k {}".format(sort)

        if count:
             cmd += " | wc -l"
             path = "{}/number_process_running.out".format(dest)

        if awk:
            cmd += " | awk '{ print $" + awk + " }'"

        child = subprocess.Popen([cmd],shell=True,stdout=subprocess.PIPE,)
        stdout_value, stderr_value = child.communicate()

        with open(path, "w") as log:
            print >> log, stdout_value                  
        # Read arguments

        self.module.exit_json(changed=True, stdout=stdout_value)

if __name__ == '__main__':
    ps_grep= custom_ps_grep()
    ps_grep.main() 
