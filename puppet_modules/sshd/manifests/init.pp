# a class for installing and configuring a basic nginx setup

class sshd {
    $packages = ["openssh-server"]

    package { $packages:
        ensure => present,
    }

    file {"/etc/ssh/sshd_config":
        owner => "root",
        group => "root",
        content => template('sshd/sshd_config.erb'),
        notify => Service['ssh'],
    }

    service {'ssh':
        ensure => running,
        enable => true,
        hasstatus => true,
        hasrestart => true,
        require => Package["openssh-server"],
    }
}
