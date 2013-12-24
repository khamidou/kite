Vagrant.configure("2") do |config|
    config.vm.box = "precise32"
    config.vm.box_url = "http://files.vagrantup.com/precise32.box"
    config.vm.provision :puppet do |puppet|
        puppet.module_path = "puppet_modules"
        puppet.manifest = "vagrant.pp"
        #puppet.options = "--debug --verbose"
    end
    config.vm.host_name = "example.com"
    config.vm.network "private_network", ip: "192.168.50.4"
    config.vm.network "forwarded_port", guest: 80, host: 8080
end
