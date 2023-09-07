#!/usr/bin/python3
"""fabric script that deploys compressed archive to servers"""

from fabric.api import env, put, run
from os.path import exists

env.hosts = ['100.25.182.117', '52.86.206.209']


def do_deploy(archive_path):
    """Distributes an archive to your web servers"""
    if not exists(archive_path):
        return False

    file_name = archive_path.split("/")[-1]
    name = file_name.split(".")[0]

    try:
        put(archive_path, "/tmp/{}".format(file_name))
        run("mkdir -p /data/web_static/releases/{}/".format(name))
        run("tar -xzf /tmp/{} -C \
                /data/web_static/releases/{}/".format(file_name, name))
        run("rm /tmp/{}".format(file_name))
        run("rm -rf /data/web_static/releases/{}/images \
            /data/web_static/releases/{}/styles".format(name, name))
        run("mv /data/web_static/releases/{}/web_static/* \
            /data/web_static/releases/{}/".format(name, name))
        run("rm -rf /data/web_static/releases/{}/web_static".format(name))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ \
            /data/web_static/current".format(name))
        return True
    except Exception as e:
        print(e)
        return False
