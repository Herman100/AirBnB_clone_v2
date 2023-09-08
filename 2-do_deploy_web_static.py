#!/usr/bin/python3
"""Fabric script for distributing an archive to web servers"""
from fabric.api import put, run, env
import os

env.hosts = ['100.25.182.117', '52.86.206.209']


def do_deploy(archive_path):
    """Distributes an archive to web servers"""
    if not os.path.exists(archive_path):
        return False

    try:
        file_name = archive_path.split("/")[-1]
        name = file_name.split(".")[0]
        put(archive_path, "/tmp/")
        run("mkdir -p /data/web_static/releases/{}/".format(name))
        run("tar -xzf /tmp/{} -C \
            /data/web_static/releases/{}/".format(file_name, name))
        run("rm /tmp/{}".format(file_name))
        run("mv /data/web_static/releases/{}/web_static/* \
                /data/web_static/releases/{}/".format(name, name))
        run("rm -rf /data/web_static/releases/{}/web_static".format(name))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ \
            /data/web_static/current".format(name))
        return True
    except BaseException:
        return False
