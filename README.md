# Ansible module that manages perlbrew and installs perl versions

## Requirements

This module requires Ansible 2.x version.

## Role variables

```
- name: Install perlbrew perls
  become_user: tmolnar
  perlbrew_perl:
    name:
			- perl-5.24.1
			- perl-5.22.3
    state: present
    perlbrew_root: /home/tmolnar/.perl5
```

## Examples

```
- hosts: Desktops 
  roles:
    - perlbrew
```

## Dependencies

- Development tools (Ubuntu: build-essential, CentOS: Development Tools)

## License

BSD

## Author

Tamas Molnar
