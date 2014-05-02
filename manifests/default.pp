# this is the main config file for puppet

exec {"apt-get update":
        path =>  ["/usr/bin/", "/usr/sbin"],
}

$packages = ["python", "python-pip", "bpython", 
             "mutt", "python-pyinotify", "mailutils", "python-leveldb"]

$python_packages = ["python-dateutil"]

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

package { $python_packages:
    ensure => present,
    require => Exec["apt-get update"],
    provider => 'pip',
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
    maildirs => '/home/kite/Maildirs/', 
    appdir => "/home/kite/app/back/kite/",
    require => File["/home/kite/app"]
}
