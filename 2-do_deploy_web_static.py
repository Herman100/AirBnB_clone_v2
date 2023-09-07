#!/usr/bin/python3
"""
Fabric script for deploying an archive to web servers
"""

from fabric.api import env, put, run
from os.path import exists

env.hosts = ['100.25.182.117', '52.86.206.209']


def do_deploy(archive_path):
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
        run("rm -rf " + data_path + "web_static")
        run("rm -rf " + current_path)
        run("ln -s " + data_path + " " + current_path)

        return True
    except Exception as e:
        print(e)
        return False
