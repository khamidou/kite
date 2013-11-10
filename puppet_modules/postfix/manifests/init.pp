# a class for installing and configuring a basic nginx setup

class postfix ($server_name, $appdir) {
    $packages = ["postfix"]

    package { $packages:
        ensure => present,
    }

    service {'postfix':
        ensure => running,
        enable => true,
        hasstatus => true,
        hasrestart => true,
        require => Package["postfix"],
    }

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

    
    postfix_config { 'virtual_mailbox_domains':
        value => "/etc/postfix/vhosts",
    }

   file {'/home/kite/Maildirs':
        ensure => 'directory',
        group => '5000',
        owner => '500',
    }

    file {"/home/kite/Maildirs/${server_name}":
        ensure => 'directory',
        group => '5000',
        owner => '500',
        require => File['/home/kite/Maildirs'],
    }


    postfix_config { 'virtual_mailbox_base':
        value => "/home/kite/Maildirs/",
        require => File['/home/kite/Maildirs'],
    }

    postfix_config { 'virtual_mailbox_maps' :
        value => "hash:/etc/postfix/vmaps"
    }
    
    postfix_config { 'virtual_minimum_uid':
        value => "500",
    }

    postfix_config { 'virtual_uid_maps':
        value => "static:500",
    }

    postfix_config { 'virtual_gid_maps':
        value => "static:5000",
    }

    file {"/etc/postfix/vhosts":
        owner => "root",
        group => "root",
        content => template('postfix/postfix_vhosts.erb'),
    }

    file {"/etc/postfix/vmaps":
        owner => "root",
        group => "root",
        content => template('postfix/postfix_vmaps.erb'),
    }

    exec {"postmap /etc/postfix/vmaps":
        path =>  ["/usr/bin/", "/usr/sbin"],
        require => File["/etc/postfix/vmaps"],
        notify => Service["postfix"],
    }

    # deliver a copy of all the received emails to user kite
    #postfix_config { 'always_bcc':
    #    value => "kite",
    #}

}
