import os
import os.path


def get_base_path():
    return os.path.dirname(os.path.abspath(os.path.realpath(__file__)))


def get_mybin_path():
    return os.path.expanduser("~/mybin/")


def get_target_path(name):
    return os.path.join(get_mybin_path(), name)


if __name__ == '__main__':
    mybin_path = get_mybin_path()
    if not os.path.exists(mybin_path):
        os.mkdir(mybin_path)
    name_list = ['asyn', 'copy.sh', 'paste.sh', 'init_sbt.py', 'send_key.py', 'set_cpu_governor.py', 'use_ssh_for_github.py', 'ydict.sh']
    for name in name_list:
        target = get_target_path(name)
        os.symlink(get_base_path() + "/%s" % name, target)

