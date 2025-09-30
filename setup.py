# -*- coding: utf-8 -*-
"""
 Licensed to the Apache Software Foundation (ASF) under one
 or more contributor license agreements.  See the NOTICE file
 distributed with this work for additional information
 regarding copyright ownership.  The ASF licenses this file
 to you under the Apache License, Version 2.0 (the
 "License"); you may not use this file except in compliance
 with the License.  You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing,
 software distributed under the License is distributed on an
 "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 KIND, either express or implied.  See the License for the
 specific language governing permissions and limitations
 under the License.
"""

import os
from setuptools import setup, find_packages

"""
setup module for upgradelink-api-python.

Created on 30/09/2025

@author: upgradelink-api SDK
"""

PACKAGE = "upgradelink_api_python"
NAME = "upgradelink-api-python" or "alibabacloud-package"
DESCRIPTION = "upgradelink_api_python"
AUTHOR = "upgradelink-api SDK"
AUTHOR_EMAIL = "toolsetlink@163.com"
URL = "https://github.com/toolsetlink/upgradelink-api-python"
VERSION = __import__(PACKAGE).__version__
REQUIRES = [
    'alibabacloud-tea>=0.2.0',
    'alibabacloud-tea-util>=0.3.0',
    'darabonba-base-python>=0.0.1'
]

LONG_DESCRIPTION = ''
if os.path.exists('./README.md'):
    with open("README.md", encoding='utf-8') as fp:
        LONG_DESCRIPTION = fp.read()

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license="Apache License 2.0",
    url=URL,
    keywords=["upgradelink","api","python"],
    packages=find_packages(exclude=["tests*"]),
    include_package_data=True,
    platforms="any",
    install_requires=REQUIRES,
    python_requires=">=3.6",
    classifiers=(
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        "Topic :: Software Development"
    )
)
