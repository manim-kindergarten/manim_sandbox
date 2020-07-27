sudo mkdir /usr/share/fonts/Consolas
sudo cp docs/fonts/* /usr/share/fonts/Consolas/
sudo apt install ttf-mscorefonts-installer -y
sudo apt install fontconfig -y
sudo mkfontscale
sudo mkfontdir
sudo fc-cache -fv