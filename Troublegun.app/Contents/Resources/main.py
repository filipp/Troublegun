#! /usr/bin/env python

import os
import subprocess
import ConfigParser
from string import Template
from tempfile import NamedTemporaryFile


def getresource(res):
    from os.path import realpath, join, dirname
    return join(dirname(realpath(__file__)), res)

def getconfig():
    config = dict()
    ini = ConfigParser.ConfigParser()
    inipath = getresource('config.ini')
    ini.read(inipath)
    for i in ini.options('message'):
        config[i] = ini.get('message', i)

    return config

def gethelper():
    helper = subprocess.check_output(['sh', getresource('gethelper.sh')])
    return helper.strip()

def screencapture():
    f = NamedTemporaryFile(delete=False, suffix=".png")
    f.close()
    subprocess.call(['screencapture', '-C', f.name])
    return f.name

def makemail(config):
    helper = gethelper()

    if helper == "" or "com.apple.mail" in helper:
        scpt = file(getresource("mail.scpt"), "r")
    elif "entourage" in helper:
        scpt = file(getresource("entourage.scpt"), "r")
    else:
        raise Exception("%s is not a supported mail app" % helper)

    compiled_scpt = Template.substitute(Template(scpt.read()), config)
    exe = NamedTemporaryFile(delete=False, suffix=".scpt")
    exe.write(compiled_scpt)
    exe.close()
    return exe.name

def main():
    config = getconfig()

    if 'screencapture' in config.get('attachments'):
        config['filename'] = screencapture()

    exe = makemail(config)
    subprocess.call(['osascript', exe])
    os.unlink(exe)


if __name__ == '__main__':
    main()
