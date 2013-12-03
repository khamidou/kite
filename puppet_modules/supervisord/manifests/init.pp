# a class for installing and configuring a basic nginx setup

class supervisord ($maildirs) {
    $packages = ["supervisor"]

    package { $packages:
        ensure => present,
    }

    file {"/etc/supervisord.conf":
        owner => "root",
        group => "root",
        content => template('supervisord/supervisord.conf.erb')  
    }

    service {'supervisor':
        ensure => running,
        enable => true,
        hasstatus => true,
        hasrestart => true,
        require => Package["supervisor"]
    }
}
