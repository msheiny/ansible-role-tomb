ansible-tomb
=========

[![BSD License](http://img.shields.io/badge/license-BSD-blue.svg)](http://opensource.org/licenses/BSD-3-Clause)
[![Build Status](https://travis-ci.org/eddyhub/ansible-tomb.svg?branch=master)](https://travis-ci.org/eddyhub/ansible-tomb)

Ansible role for managing tomb installation from https://nuetzlich.net/tomb/

Installation
------------

ansible-galaxy install eddyhub.tomb

Requirements
------------

None.

Role Variables
--------------

```yaml
---
# defaults file for ansible-tomb

ansible_unit_test: false
tomb_role_release: '0.0.1'

# tomb version to install
tomb_version: 'latest'

# tomb platform
tomb_platform: 'amd64'

# tomb name with installed version
tomb_name: 'tomb'

# tomb install directory
tomb_install_directory: '/usr/local/bin'

# tomb install directory
tomb_manpage_directory: '/usr/local/share/man/man1'

# tomb owner
tomb_owner: 'root'

# tomb group
tomb_group: 'root'

# tomb set suid access
tomb_mode: '4755'
```

Dependencies
------------

None, for role to install.

Example Playbook
----------------

```yaml
- name: Installing tomb
  hosts: all
  sudo: yes
  roles:
    - role: eddyhub.tomb
```

License
-------

Copyright (c) 2017, Eduard Angold
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice, this
  list of conditions and the following disclaimer.

* Redistributions in binary form must reproduce the above copyright notice,
  this list of conditions and the following disclaimer in the documentation
  and/or other materials provided with the distribution.

* Neither the name of ansible-tomb nor the names of its
  contributors may be used to endorse or promote products derived from
  this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

Author Information
------------------

eddyhub@users.noreply.github.com
