#!/usr/bin/python
# -*- coding: utf-8 -*-

from ansible.module_utils.basic import *

class custom_df:

    def __init__(self):
        self.module = AnsibleModule(argument_spec=dict(option=dict(),
                                    dest=dict()))

    def main(self):

        df = self.module.params
        option = df['option']
        dest = df['dest']
        cmd = 'df'
        
        if option and option == 'human' or 'hr' or 'human_readable':
            cmd = cmd + ' -h'
        child = subprocess.Popen([cmd], shell=True,
                                 stdout=subprocess.PIPE)
        (stdout_value, stderr_value) = child.communicate()

        path = str(dest) + '/df.out'
        with open(path, 'w') as log:
            print >> log, stdout_value
        self.module.exit_json(changed=True, stdout=stdout_value)


if __name__ == '__main__':
    run_cmd = custom_df()
    run_cmd.main()
