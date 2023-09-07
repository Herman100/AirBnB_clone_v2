#!/usr/bin/python3
"""packing fabric file function"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """Generates a .tgz archive from the contents of the web_static folder"""
    local("mkdir -p versions")
    now = datetime.now()
    now = now.strftime("%Y%m%d%H%M%S")
    file_name = "web_static_{}.tgz".format(now)
    result = local("tar -cvzf versions/{} web_static".format(file_name))

    if result.failed:
        return None
    else:
        return "versions/{}".format(file_name)
