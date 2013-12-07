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
        provider => 'init',
        require => [Package["supervisor"], File["/etc/supervisord.conf"],
                    File["/etc/init.d/supervisor"]]
    }

    # FIXME: For some reason "service" doesn't setup supervisor to run at
    # boot time, so we've got to call update rc.d manually.
    exec {'update_rcd':
        command => "update-rc.d supervisor defaults",
        path => ["/usr/sbin", "/usr/bin/", "/sbin"],
        require => [Service['supervisor']],
    }
}
