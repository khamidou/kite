# a class for installing and configuring a basic nginx setup

class dovecot ($server_name, $appdir) {
    $packages = ["dovecot-common", "dovecot-imapd", "dovecot-pop3d"]

    package { $packages:
        ensure => present,
    }

    service {'dovecot':
        ensure => running,
        enable => true,
        hasstatus => true,
        hasrestart => true,
        require => [Package["postfix"],
                    File['/etc/dovecot/dovecot.conf'],
                    File["/etc/dovecot/users"],
                    File["/etc/dovecot/passwd"],],

    }

   file {'/etc/dovecot/dovecot.conf':
        owner => 'root',
        group => "root",
        content => template('dovecot/dovecot.conf.erb')
    }

    file {"/etc/dovecot/users":
        owner => 'root',
        group => "root",
        content => template('dovecot/users.erb')
    }

    file {"/etc/dovecot/passwd":
        owner => 'root',
        group => "root",
        content => template('dovecot/passwd.erb')
    }
}
