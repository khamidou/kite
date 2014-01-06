# Puppet manifest for setting up kite on vagrant
import "default.pp"

host {'kitebox.dev':
    ip => '127.0.0.1'
}

file {'/home/kite/app':
    ensure => 'link',
    target => '/vagrant/src',
    owner => 'kite',
}
