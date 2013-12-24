# Puppet manifest for setting up kite on a server
import "settings.pp"
import "default.pp"

file {'/home/kite/app':
    ensure => 'directory',
    require => User['kite'],
    source => "/root/kite/src",
    recurse => true,
    owner => 'kite',
}

class {'sshd':

}
