#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import subprocess
from ansible.module_utils.basic import *


def main():
    module = \
        AnsibleModule(argument_spec=dict(username=dict(required=True),
                      password=dict(required=True),
                      , required=False, aliases=['repo']),
                      , required=False)))
    username = module.params['username']
    password = module.params['password']
    url = module.params['url']
    source = module.params['source']

    # Read arguments

    child = subprocess.Popen([source + ' saveCredential -url ' + url
                             + ' -userName ' + username
                             + ' -userPassword ' + password],
                             shell=True, stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)
    stdout_value, stderr_value = child.communicate()
    # Read arguments

    if child.returncode != 0:
        module.fail_json(msg="failed",stderr=stderr_value, stdout=stdout_value)

                # Module finished

    module.exit_json(changed=True,msg=username,stdout=stdout_value)


if __name__ == '__main__':

    main()
