mkdir /usr/share/fonts/Consolas
cp fonts/* /usr/share/fonts/Consolas/
apt install ttf-mscorefonts-installer -y
apt install fontconfig -y
mkfontscale
mkfontdir
fc-cache -fv