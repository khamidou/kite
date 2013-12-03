# this is the main config file for puppet

$server_name = "kitebox.dev"

exec {"apt-get update":
        path =>  ["/usr/bin/", "/usr/sbin"],
}

$packages = ["python", "bpython", "mutt", "python-pyinotify"]

$kite_gid = "5000"
$kite_uid = "500"

group { "kite":
    ensure => "present",
    gid => $kite_gid
}

package { $packages:
    ensure => present,
    require => Exec["apt-get update"],
}

user { "kite":
    require => Group["kite"],
    ensure => present,
    gid => "kite",
    uid => $kite_uid,
    shell => "/bin/true",
    home => "/home/kite",
    managehome => true,
}

# comes from http://serverfault.com/a/524188
class hostname ($fqdn) {
    file { "/etc/hostname":
               ensure => present,
               owner => root,
               group => root,
               mode => 644,
               content => "$fqdn\n",
               notify => Exec["set-hostname"],
    }

    exec { "set-hostname":
        command => "/bin/hostname -F /etc/hostname",
        unless => "/usr/bin/test `hostname` = `/bin/cat /etc/hostname`",
    }
}

class {'hostname':
    fqdn => $server_name
}

host {'kitebox.dev':
    ip => '127.0.0.1'
}

file { "/var/kitemail":
    require => User["kite"],
    ensure => "directory",
    owner => "kite",
    group => "kite",
}

# nginx
class {'nginx':
    server_name => $server_name,
    appdir => "/home/kite/app",
    require => Exec["apt-get update"]
}

# postfix
class {'postfix':
    server_name => $server_name,
    appdir => "/home/kite/app",
    require => Exec["apt-get update"]
}

class {'dovecot':
    server_name => $server_name,
    appdir => "/home/kite/app",
    require => Exec["apt-get update"]
}

class {'supervisord':
    maildirs => '/home/kite/Maildirs'
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
