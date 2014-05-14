# a class configuring the kite config files

class app_config ($server_name) {
    file {"/home/kite/app/back/kite/config.py":
        owner => "kite",
        group => "kite",
        content => template('app_config/config.erb'),
    }
}
