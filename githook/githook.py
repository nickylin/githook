
#!/usr/bin/python
# -*- coding: UTF-8 -*-
# *********************************************************
# description: githook.py
#    it is for copy githook file to dst dir
# Auth: wanmin.lwm@alibaba-inc.com
# Date: 2017-05-24
# *********************************************************

import filecmp
import os
import sys
import shutil

def checkSameFile(src, dst):
    return filecmp.cmp(src, dst)

def moveFileto(sourceDir,  targetDir):
    shutil.copy(sourceDir,  targetDir)

def chmodExecFile(filename):
    cmd = 'chmod 777 ' + filename
    os.system(cmd)

curDir = os.getcwd()
print 'enter git hook task' + curDir

SRC_PRE_PUSH_FILE = curDir +'/pre-push'
DST_FILE_DIR=  '../.git/hooks/'
DST_PRE_PUST_FILE= DST_FILE_DIR + 'pre-push'

print SRC_PRE_PUSH_FILE
print DST_PRE_PUST_FILE

if os.path.exists(SRC_PRE_PUSH_FILE):
    if os.path.exists(DST_FILE_DIR) == False:
        os.makedirs(DST_FILE_DIR)
    else:
        print 'DST_FILE_DIR exists'
    if os.path.exists(DST_PRE_PUST_FILE) == False:
        moveFileto(SRC_PRE_PUSH_FILE, DST_PRE_PUST_FILE)
        chmodExecFile(DST_PRE_PUST_FILE)
        print 'do copy githook file'
    elif checkSameFile(SRC_PRE_PUSH_FILE, DST_PRE_PUST_FILE) == False:
        moveFileto(SRC_PRE_PUSH_FILE, DST_PRE_PUST_FILE)
        chmodExecFile(DST_PRE_PUST_FILE)
        print 'do copy githook file'
    else:
        print 'this file is no update,no need to copy githook file'
else:
    print SRC_PRE_PUSH_FILE + ' file not found'
