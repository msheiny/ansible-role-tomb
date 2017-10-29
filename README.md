ansible-role-tomb
=================

[![BSD License](http://img.shields.io/badge/license-BSD-blue.svg)](http://opensource.org/licenses/BSD-3-Clause)

[![CircleCI](https://circleci.com/gh/msheiny/ansible-role-tomb/tree/master.svg?style=svg)](https://circleci.com/gh/msheiny/ansible-role-tomb/tree/master)

Ansible role for managing tomb installation from https://nuetzlich.net/tomb/

Forked from https://github.com/eddyhub/ansible-tomb

Role Variables
--------------

```yaml
---
# defaults file for ansible-role-tomb

# tomb version to install
tomb_version: 'latest'

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

# Web Urls
tomb_base_url: 'https://files.dyne.org/tomb'
tomb_package_meta_json: 'https://api.github.com/repos/dyne/Tomb/tags'

# install optional tools as defined in the tomb installation docs
# https://github.com/dyne/Tomb/blob/master/INSTALL.md
tomb_install_optional_tools: "false"

# Key from https://keybase.io/jaromil
tomb_dyne_gpg_key: |
  -----BEGIN PGP PUBLIC KEY BLOCK-----
  Version: GnuPG v1
  [ ... ]
  wSk4lJDtTCi9L0cjfo2xt2DSYDOt4NdZ1mbDavlv/K0KMns/LCIbDHE5lrhxoKLQ
  2mjWpi95PsdnW3BbfAtvpgxqdvTO1fdIZEdBy/WBOxBF3RpPiSFbcTNzXMzwOI9f
  fQ8eS5QjyJwJcsbM50DKtvlOHeRUigjS3p+u4kXLspqy9lafpviHpbQ6VBiX5MgM
  /wST/LRjesJvwPqHyW1Mj57FN22KRkPSCpcMvzRY7hHvJLjIALdAEe6oqb62JLrA
  rUPLLNUtPz9Q9MtVcrTmFsdYT0v0fNZnsuu3A0ioJQe1kB0vbJbBXImB3odSAQdW
  nybDbRloiirCWTJD6KCihxdeQ/4KHngQc6KAYTmMXZ87eLioxMh1Abv0t1Y4/i9a
  gT1qQmzalWIyOB0o8+lDaYefxehnAD7QBEcpQ3qB3huw0oQ7J9u4Lkhb4mE9mGdI
  =HXVw
  -----END PGP PUBLIC KEY BLOCK-----
```

Example Playbook
----------------

```yaml
- name: Installing tomb
  hosts: all
  sudo: yes
  roles:
    - role: msheiny.tomb
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

* ORIGINAL AUTHOR: eddyhub@users.noreply.github.com
* REFACTOR: m.sheiny@gmail.com
