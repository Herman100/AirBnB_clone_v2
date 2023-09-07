#!/usr/bin/python3
"""
Fabric script for deploying an archive to web servers
"""

from fabric.api import env, put, run, local
from os.path import exists
from datetime import datetime

env.hosts = ['100.25.182.117', '52.86.206.209']


def do_pack():
    """packs code into an archive"""
    try:
        now = datetime.now()
        dt_string = now.strftime("%Y%m%d%H%M%S")
        local("mkdir -p versions")
        local("tar -cvzf \
              versions/web_static_{}.tgz web_static".format(dt_string))
        return "versions/web_static_{}.tgz".format(dt_string)
    except Exception as e:
        print(e)
        return None


def do_deploy(archive_path):
    """deploys code to server"""
    if not exists(archive_path):
        return False

    try:
        file_name = archive_path.split("/")[-1]
        name = file_name.split(".")[0]
        tmp_path = "/tmp/" + file_name
        data_path = "/data/web_static/releases/" + name + "/"
        current_path = "/data/web_static/current"

        put(archive_path, tmp_path)
        run("mkdir -p " + data_path)
        run("tar -xzf " + tmp_path + " -C " + data_path)
        run("rm " + tmp_path)
        run("mv " + data_path + "web_static/* " + data_path)
        run("rm -rf" + " /data/web_static/releases/" + name + "/web_static")
        run("rm -rf " + current_path)
        run("ln -s " + data_path + " " + current_path)

        return True
    except Exception as e:
        print(e)
        return False


def deploy():
    """creates and distributes an archive to web servers"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
