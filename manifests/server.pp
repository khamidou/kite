# Puppet manifest for setting up kite on a server
import "settings.pp"
import "default.pp"

file {'/home/kite/app':
    ensure => 'directory',
    require => User['kite'],
    source => "$user_home_dir/kite/src", # $user_home_dir is an env var exposed by facter
                                         # it seems that there's no simpler solution. The env var
                                         # is defined in the fabfile
    recurse => true,
    owner => 'kite',
}


