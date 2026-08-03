1. Add SUMO’s official stable repository to the local APT sources.
``` bash

sudo add-apt-repository ppa:sumo/stable
sudo apt-get update
sudo apt-get install sumo sumo-tools sumo-doc
```

2. Install SUMO and set SUMO_HOME env variavle
```bash 
sudo apt install -y sumo sumo-tools sumo-doc
echo 'export SUMO_HOME="/usr/share/sumo"' >> ~/.bashrc
source ~/.bashrc
```