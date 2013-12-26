# fabfile for update and deploy
# it's necessary to specify an host
from fabric.api import *
from fabric.contrib.project import rsync_project
from fabric.contrib.files import upload_template
import paramiko

remote_user = "karim" # this needs to be a user who can run sudo

paramiko.util.log_to_file("paramiko.log", 10)
env.hosts = ["dogfood.kiteapp.io"]

PACKAGES = ('rsync', 'puppet')

def setup():
    local("ssh-copy-id %s@%s" % (remote_user, env.hosts[0]))
    sudo("apt-get update")

    for package in PACKAGES:
        sudo('apt-get -y install %s' % package)

    rsync_project("~", "../kite", exclude=[".git/", "*.swp", "*.pyc"])
    sudo("puppet apply $HOME/kite/manifests/server.pp --modulepath=$HOME/kite/puppet_modules")
