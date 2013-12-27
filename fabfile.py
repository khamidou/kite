# fabfile for update and deploy
# it's necessary to specify an host
from fabric.api import *
from fabric.contrib.project import rsync_project
from fabric.contrib.files import upload_template
from setup_config import *

PACKAGES = ('rsync', 'puppet')

def setup():
    sudo("apt-get update")

    for package in PACKAGES:
        sudo('apt-get -y install %s' % package)

    rsync_project("~", "../kite", exclude=[".git/", "*.swp", "*.pyc"])
    sudo("FACTER_user_home_dir=$HOME && export FACTER_user_home_dir && puppet apply $HOME/kite/manifests/server.pp --modulepath=$HOME/kite/puppet_modules")

    local("ssh-copy-id %s@%s" % (env.user, env.hosts[0]))
    sudo("puppet apply $HOME/kite/manifests/sshd.pp --modulepath=$HOME/kite/puppet_modules")
