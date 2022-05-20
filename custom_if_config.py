#!/usr/bin/python
# -*- coding: utf-8 -*-

from ansible.module_utils.basic import *


class custom_if_config:

    def __init__(self):

        self.module = AnsibleModule(argument_spec=dict(option=dict(),
                                    dest=dict()))

    def main(self):

        if_config = self.module.params
        option = if_config['option']
        dest = if_config['dest']
        cmd = 'ifconfig'

        if option and option == 'all':
            cmd = cmd + ' -a'

        child = subprocess.Popen([cmd], shell=True,
                                 stdout=subprocess.PIPE)
        (stdout_value, stderr_value) = child.communicate()

        path = str(dest) + '/ifconfig.out'
        with open(path, 'w') as log:
            print >> log, stdout_value
        self.module.exit_json(changed=True, stdout=stdout_value)

if __name__ == '__main__':
    if_config = custom_if_config()
    if_config.main()
