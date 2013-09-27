#Vagrant::Config.run do |config|
Vagrant.configure("2") do |config|
    config.vm.box = "lucid32"
    config.vm.box_url = "http://files.vagrantup.com/lucid32.box"
    #config.vm.forward_port 80, 3000
    config.vm.provision :puppet
    config.vm.host_name = "example.com"
    config.vm.network "private_network", ip: "192.168.50.4"
    #config.vm.network :bridged
end
