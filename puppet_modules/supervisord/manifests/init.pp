# a class for installing and configuring a basic nginx setup

class supervisord ($maildirs, $appdir) {
    $packages = ["supervisor"]

    package { $packages:
        ensure => present,
        provider => 'pip',
    }

    file {"/etc/supervisord.conf":
            owner => "root",
            group => "root",
            content => template('supervisord/supervisord.conf.erb'), 
    }

    file {"/etc/init.d/supervisor":
            owner => "root",
            group => "root",
            mode => "0744",
            content => template('supervisord/supervisord.init.erb'), 
    }

    service {'supervisor':
        ensure => running,
        enable => true,
        hasstatus => true,
        hasrestart => true,
        path => "/etc/init.d/",
        provider => 'init',
        require => [Package["supervisor"], File["/etc/supervisord.conf"],
                    File["/etc/supervisord.conf"]]
    }
}
