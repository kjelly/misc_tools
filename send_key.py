#! /usr/bin/env python
import subprocess
import sys
import psutil


def get_active_window_id():
    return subprocess.Popen(["xprop", "-root", "_NET_ACTIVE_WINDOW"], stdout=subprocess.PIPE).communicate()[0].strip().split()[-1]


def get_active_window_title():
    return subprocess.Popen(["xprop", "-id", get_active_window_id(), "WM_NAME"], stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0].strip().split('"', 1)[-1][:-1]


def get_active_window_pid():
    return int(subprocess.Popen(["xprop", "-id", get_active_window_id(), "_NET_WM_PID"], stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0].strip().split('=', 1)[-1].strip(), 10)


if __name__ == '__main__':
    if len(sys.argv) >= 3:
        title = get_active_window_title()
        pid = get_active_window_pid()
        process_name = ' '.join(psutil.Process(pid).cmdline())
        if sys.argv[1] in process_name:
            subprocess.call(["xvkbd", "-text", sys.argv[2]])
