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
        
        path = "{}/df.out".format(dest)

        
        if option == 'human':
            cmd = cmd + ' -h'
            path = "{}/df_h.out".format(dest)

        child = subprocess.Popen([cmd], shell=True,
                                 stdout=subprocess.PIPE)
        (stdout_value, stderr_value) = child.communicate()

        with open(path, 'w') as log:
            print >> log, stdout_value
        self.module.exit_json(changed=True, stdout=stdout_value)


if __name__ == '__main__':
    df = custom_df()
    df.main()
