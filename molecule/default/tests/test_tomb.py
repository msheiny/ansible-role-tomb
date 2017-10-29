import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_tomb_functional(host):
    """ Is tomb installed ? Let's just try running basic dig command
    """
    host.run('tomb dig -s 10 /tmp/digfile')

    f = host.file('/tmp/digfile')

    assert f.exists
