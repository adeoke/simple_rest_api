# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|
  # The most common configuration options are documented and commented below.
  # For a complete reference, please see the online documentation at
  # https://docs.vagrantup.com.

  # Every Vagrant development environment requires a box. You can search for
  # boxes at https://vagrantcloud.com/search.
  config.vm.box = "ubuntu/bionic64"
  config.vm.box_version = '~> 20190314.0.0'

  config.vm.network "forwarded_port", guest: 8000, host: 8000

  config.vm.provision "shell", inline: <<-SHELL
    # disable auto updates with system ctl commands
    # systemctl disable apt-daily.service
    # systemctl disable apt-daily.timer

    sudo apt update
    sudo apt upgrade
    # sudo apt install -y zip
    # sudo apt install -y python3-pip
    # pip3 --version
    # sudo pip3 install pipenv
    # pip3 uninstall -y pipenv
    # pip3 install pipenv
    # pip3 uninstall -y virtualenv
    # pip3 install virtualenv
    # pip3 uninstall -y appdirs
    # pip3 install appdirs
    # pip3 uninstall -y filelock
    # pip3 install filelock
    # pip3 uninstall -y importlib_metadata
    # pip3 install importlib_metadata
    # pip3 uninstall -y zipp
    # pip3 install zipp
    # pip3 uninstall -y distlib
    # pip3 install distlib
    # pip3 uninstall -y importlib_resources
    # pip3 install importlib_resources
    cd /vagrant 
    pipenv shell 
    pipenv install -r requirements.txt
    pip3 install --upgrade pipenv --user
  SHELL
end
