exec {"apt-get update":
        path =>  ["/usr/bin/", "/usr/sbin"],
}

$packages = ["postfix"]

group { "kite":
    ensure => "present"
}

package { $packages:
    ensure => present,
    require => Exec["apt-get update"]
}

service {'postfix':
    ensure => running,
    enable => true,
    hasstatus => true,
    hasrestart => true,
    require => Package["postfix"]
}

user { "kite":
    require => Group["kite"],
    ensure => present,
    gid => "kite",
    shell => "/bin/true",
    home => "/home/kite",
    managehome => true,
}

file { "/var/kitemail":
    require => User["kite"],
    ensure => "directory",
    owner => "kite",
    group => "kite",
}


# nginx
class {'nginx':
    server_name => "example.com",
    appdir => "/home/kite/app",
    require => Exec["apt-get update"]
}

#nginx::resource::location {'kiteapp':
#    ensure => present,
#  www_root => '/home/kite/app',
#    location => '/',
#    vhost => 'kiteapp'
#}

# code comes from : https://bitbucket.org/daks/puppet-postfix/src/2e93e657cab6/manifests/definitions/config.pp
define postfix_config ($ensure = present, $value, $nonstandard = false) {
      exec {"postconf -e ${name}='${value}'":
        path =>  ["/usr/bin/", "/usr/sbin"],
        unless  => $nonstandard ? {
          false => "test \"x$(postconf -h ${name})\" == 'x${value}'",
          true  => "test \"x$(egrep '^${name} ' /etc/postfix/main.cf | cut -d= -f2 | cut -d' ' -f2)\" == 'x${value}'",
        },
        notify  => Service["postfix"],
        require => Package["postfix"]
      }
}

postfix_config { 'home_mailbox':
    value => "Maildir/",
}

# deliver a copy of all the received emails to user kite
postfix_config { 'always_bcc':
    value => "kite",
}

# deploy files
if $is_virtual == 'true' {
    file {'/home/kite/app':
        ensure => 'link',
        target => '/vagrant/src',
        owner => 'kite',
    }

    # FIXME: copy/deploy files correctly if not running in vagrant
}
