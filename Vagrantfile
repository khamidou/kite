Vagrant::Config.run do |config|
    config.vm.box = "lucid32"
    config.vm.box_url = "http://files.vagrantup.com/lucid32.box"
    config.vm.forward_port 80, 3000
    config.vm.provision :puppet
end
