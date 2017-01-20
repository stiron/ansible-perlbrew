# Ansible module that manages perlbrew and installs perl versions

## Requirements

This module requires Ansible 2.x version.

## Role variables

```
perlbrew_perl:
  name:
    - perl-5.24.1
    - perl-5.22.3
  perlbrew_root: /home/tmolnar/.perl5
  state: present
```

The `become_user` should be set on task level!

## Examples

```
- hosts: Desktops 
  roles:
    - { role: perlbrew,
        name: ['perl-5.24.1', 'perl-5.22.3'], perlbrew_root: /home/tmolnar/.perl5 }
```

## Dependencies

- Development tools (Ubuntu: build-essential, CentOS: Development Tools)

## License

BSD

## Author

Tamas Molnar
