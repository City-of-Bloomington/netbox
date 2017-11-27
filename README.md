City-of-Bloomington.netbox
=========
Ansible role for configuring a NetBox installation to serve as a datacenter management utility.

Requirements
------------

City-of-Bloomington.linux


Example Playbook
----------------

```yml
- hosts: linux-netbox
  become: yes
  roles:
  - City-of-Bloomington.linux
  - City-of-Bloomington.wsgi
```

Copying and License
-------
This material is copyright 2016 City of Bloomington, Indiana
It is open and licensed under the GNU General Public License (GPL) v3.0 whose full text may be found at:
https://www.gnu.org/licenses/gpl.txt
