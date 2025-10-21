#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Author: vivek Mistry @[Vivek M.]​
Date: 2017-10-11T20:28:17.096Z

Disclaimer:
All information, documentation, and code is provided to you AS-IS and should
only be used in an internal, non-production laboratory environment.

License:
Copyright 2017 BlueCat Networks, Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
'''
from zeep import Client
from getpass import getpass

#Parameters
BAMAddress="bam.lab.corp"
# SSL is unverified in this script see 1-firstscript-SOAP.py in this dir for
# example on how to make sure ssl certificate is verified.
url="http://"+BAMAddress+"/Services/API?wsdl"
account="api"

# Password Prompt
account_password=getpass("Enter Password: ")

#api session
# get the HTTPS session verified
client = Client(url)

#login to api session
client.service.login(account,account_password)

#APi calls
BAM_system_info = client.service.getSystemInfo()


# logout of api session
client.service.logout()

# procesing
print("--------")
for item in BAM_system_info.split("|"):
    print(item)
