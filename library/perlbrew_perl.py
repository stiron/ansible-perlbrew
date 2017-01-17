#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule
from subprocess import Popen
from subprocess import PIPE
import os.path
import os

def check_installed(root, name):
    path = root + "/perlbrew/perls/" + name
    if os.path.isdir(path):
        return True
    else:
        return False

def check_available(perl):
    p1 = Popen(['which', 'perlbrew'], stdout=PIPE)
    perlbrew = p1.communicate()[0].rstrip()

    p2 = Popen([perlbrew, 'available'], stdout=PIPE)
    available = p2.communicate()[0].split()

    if perl in available:
        return True
    else:
        return False

def remove_perl(perl):
    p1 = Popen(['which', 'perlbrew'], stdout=PIPE)
    perlbrew = p1.communicate()[0].rstrip()
    p2 = Popen([perlbrew, 'uninstall', '-q', perl], stdin=PIPE)
    p2.stdin.write('y')
    return True

def install_perl(perl, perlbrew_root):
    os.environ['PERLBREW_ROOT'] == perlbrew_root
    p1 = Popen(['which', 'perlbrew'], stdout=PIPE)
    perlbrew = p1.communicate()[0].rstrip()
    Popen([perlbrew, 'install', '-q', perl, perlbrew_root])
    return True

def main():
    module = AnsibleModule(
        argument_spec = dict(
            state = dict(default='present', choices=['present', 'absent']),
            name = dict(required=True),
            perlbrew_root = dict(required=True),
        )
    )

    is_installed = check_installed(
        module.params['perlbrew_root'],
        module.params['name']
    )

    is_available = check_available(
        module.params['name']        
    )

    if module.params['state'] == 'present':
        if is_installed:
            module.exit_json(changed=False, msg="Perl version "
                    + module.params['name'] + " is already installed")

        if not is_available:
            module.fail_json(msg="Perl version "
                    + module.params['name'] + " is not available")

        if not is_installed and is_available:
            install_perl(module.params['name'], module.params['perlbrew_root'])
            module.exit_json(changed=True)
    
    if module.params['state'] == 'absent':
        if is_installed:
            remove_perl(module.params['name'])
            module.exit_json(changed=True)
        else:
            module.exit_json(changed=False)

if __name__ == '__main__':
    main()
