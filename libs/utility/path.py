#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian
# 路径相关函数

import inspect
import os
import sys


def get_root_path():
    """
    get the automatic test framework root directory
    :return:
    """
    file_path = os.path.abspath(inspect.getfile(sys.modules[__name__]))
    parent_path = os.path.dirname(file_path)
    lib_path = os.path.dirname(parent_path)
    root_path = os.path.dirname(lib_path)
    return root_path


def get_root_parent_path():
    """
    get the parent directory of the automated test framework root
    :return:
    """
    root_parent_path = os.path.dirname(get_root_path())
    return root_parent_path


def get_root_dir_name():
    return os.path.basename(get_root_path())


MISC_PATH = get_root_path() + "/misc"


###############################
# Debugging use
###############################
if __name__ == "__main__":
    print get_root_path()
    print get_root_dir_name()



