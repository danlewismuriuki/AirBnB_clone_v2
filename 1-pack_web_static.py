#!/usr/bin/python3
""" Fabric script that generates a .tgz archive from
the contents of the web_static
"""
from collections.abc import Mapping
# local function used to run shell commands on the local machine
from fabric.api import local
from datetime import datetime

# import decorator to ensure fucn runs only once
from fabric.decorators import runs_once


@runs_once
def do_pack():
    """ generates a .tgz archive from the contents of web_static folder """
    local("mkdir -p versions")
    path = ("versions/web_static_{}.tgz"
            .format(datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")))

    result = local("tar -cvzf {} web_static"
                   .format(path),
                   capture=True)

    if result.failed:
        return None
    return path
