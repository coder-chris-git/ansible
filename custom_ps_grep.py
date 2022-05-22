#!/usr/bin/python
# -*- coding: utf-8 -*-
from ansible.module_utils.basic import *

class custom_ps_grep():
    
    def __init__(self):
             
        self.module = AnsibleModule(argument_spec=dict(

                grep_for = dict(type='list'),
                sort = dict(),
                awk =  dict(type = 'list'),
                dest = dict(),
                count = dict(type='bool'),
                user = dict()

        ))
    



    # def create_ps_ef_file(self,file_name):

    #     ps_grep_response = subprocess.Popen(['ps -ef'],shell=True,stdout=subprocess.PIPE,)
    #     stdout_value, stderr_value = ps_grep_response.communicate()
    #     path = file_name


    #     with open(path, "w") as log:
    #         print >> log, stdout_value

     

    def main(self):
        # file_name = "ps_grep.txt"
        # self.create_ps_ef_file(file_name)


        ps_grep = self.module.params

        grep_for = ps_grep['grep_for']
        user = ps_grep['user']
        sort = ps_grep['sort']
        awk = ps_grep['awk']
        dest = ps_grep['dest']
        count = ps_grep['count']
        path = str(dest) + "/" + str(grep_for[0])+".out"
        name = grep_for[0]
        cmd = "ps -ef | grep " + name

        for name in grep_for[1:]:
          cmd += '| grep -E ' + name 
        cmd += ' | grep -v grep'




        if awk:

            awk_cmd = " | awk '{print $" + str(awk[0])
            
            for col in awk[1:]:
                awk_cmd += " \"  \"$" + str(col)

            cmd += awk_cmd + "}'"

        if sort:
            path = "{}/{}_sort.out".format(dest,grep_for[0])
            cmd +=" | sort -k {}".format(sort)


             
        if count:
             cmd += " | wc -l"
             path = "{}/{}_number_process_running.out".format(dest,grep_for[0])
            

        child = subprocess.Popen([cmd],shell=True,stdout=subprocess.PIPE,)
        stdout_value, stderr_value = child.communicate()

        with open(path, "w") as log:
            print >> log, stdout_value                  
        # Read arguments

        self.module.exit_json(changed=True, stdout=stdout_value)

if __name__ == '__main__':
    ps_grep= custom_ps_grep()
    ps_grep.main() 
