# Ansible module that manages perlbrew and installs perl versions

## Requirements

This module requires Ansible >=2.2 version.

## Role variables

`perlbrew_user` - the user to install perls to

`perlbrew_root` - destination directory to install perls to

`perlbrew_perls` - a list of perl versions to be installed

## Examples

```
- hosts: Desktops 
  roles:
    - { role: perlbrew }
```

## Dependencies

- Development tools (Ubuntu: build-essential, CentOS: Development Tools)

## License

MIT

## Author

Tamas Molnar - <tmolnar0831@gmail.com>
