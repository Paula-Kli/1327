# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.require_version ">= 1.8.1"

Vagrant.configure("2") do |config|
  config.vm.box = "bento/ubuntu-20.04"
  config.vm.box_version = "202012.23.0"

  # port forwarding
  config.vm.network :forwarded_port, guest: 8000, host: 8000

  config.vm.provider :virtualbox do |v, override|
    # disable logfile
    v.customize [ "modifyvm", :id, "--uartmode1", "disconnected" ]
    v.customize [ "modifyvm", :id, "--cpus", "4" ]
    # show virtualbox gui, uncomment this to debug startup problems
    #v.gui = true
  end

  config.vm.provision "shell", path: "deployment/provision_vagrant_vm.sh"
end
