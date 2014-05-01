# fabfile for update and deploy
# it's necessary to specify an host
from fabric.api import *
from fabric.contrib.project import rsync_project
from fabric.contrib.files import upload_template
from setup_config import *

PACKAGES = ('rsync', 'puppet')

def update_sources():
    rsync_project("~", "../kite", exclude=[".git/", "*.swp", "*.pyc"])

def provision():
    cmd = """FACTER_server_name="%s" && export FACTER_server_name && FACTER_user_home_dir=$HOME && export FACTER_user_home_dir && puppet apply $HOME/kite/manifests/server.pp --modulepath=$HOME/kite/puppet_modules""" % env.hosts[0]
    sudo(cmd)

def update():
    update_sources()
    provision()
 
def setup():
    sudo("apt-get update")
    for package in PACKAGES:
        sudo('apt-get -y install %s' % package)

    update()
 
def tighten():
    local("ssh-copy-id %s@%s" % (env.user, env.hosts[0]))
    sudo("puppet apply $HOME/kite/manifests/sshd.pp --modulepath=$HOME/kite/puppet_modules")



