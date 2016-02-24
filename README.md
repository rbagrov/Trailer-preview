# Trailer-preview 1.0
All the steps below should be run from within vagrant machine

# Setup (vagrant) 

-- tested on Ubuntu Linux vagrant-ubuntu-trusty-32 3.13.0-76-generic

On host machine (Ubuntu)

sudo apt-get install virtualbox vagrant virtualbox-dkms

mkdir -p /your_favorite_VM_location/Movie_Trailer/

cd /your_favorite_VM_location/Movie_Trailer/

Create the following file "touch Vagrantfile" :

-- cut_here --


Vagrant.configure(2) do |config|

  config.vm.box = "ubuntu/trusty32"
  
  config.vm.network "forwarded_port", guest: 8111, host: 8111
  
  config.vm.synced_folder "/your_favorite_VM_location/Movie_Trailer/", "/usr/local/src/Movie-Trailer/"
  
end


-- cut_here --

vagrant box add precise32 http://files.vagrantup.com/precise32.box

vagrant up 

# Installation

vagrant ssh

sudo apt-get install python2.7 sqlite3

pip install virtualenv

cd /usr/local/src/

git clone 

cp -r /usr/local/src/Trailer-preview/* /usr/local/src/Movie_Trailer/

cd /usr/local/src/Movie_Trailer/

virtualenv env --python=python2.7

source env/bin/activate

pip install -r requirements.txt

# Running / Development

python main.py
