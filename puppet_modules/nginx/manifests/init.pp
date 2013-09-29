# a class for installing and configuring a basic nginx setup

class nginx ($server_name, $appdir) {
    $packages = ["nginx"]

    package { $packages:
        ensure => present,
    }

    file {"/etc/nginx/sites-enabled/kite":
        owner => "root",
        group => "root",
        content => template('nginx/nginx_config.erb')  
    }

    # default file has a very annoying catchall rule
    file {"/etc/nginx/sites-enabled/default":
        ensure => absent,
    }

    service {'nginx':
        ensure => running,
        enable => true,
        hasstatus => true,
        hasrestart => true,
        require => Package["nginx"]
    }
}
