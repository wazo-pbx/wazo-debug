#!/usr/bin/env python3
# Copyright 2017 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from setuptools import setup
from setuptools import find_packages


setup(
    name='wazo-debug',
    version='1.0',
    author='Wazo Authors',
    author_email='dev@wazo.community',
    url='http://wazo.community',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'wazo-debug-collect= wazo_debug.main_collect:main',
            'wazo-debug = wazo_debug.main:main',
        ],
        'wazo_debug.commands': [
            'capture = wazo_debug.main_capture:CaptureCommand',
            'collect = wazo_debug.main_collect:CollectCommand',
        ],
    },
)
