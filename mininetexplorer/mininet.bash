git clone https://github.com/SaiLikhith7/sailikhith7.github.io /tmp/website01
git clone https://github.com/ybqu/ybqu.github.io /tmp/website02
git clone https://github.com/femmebot/google-type /tmp/website03
git clone https://github.com/randomlike/randomlike /tmp/website04
head -c 20000000 /dev/srandom > /tmp/website04/sample.bin
git clone https://github.com/openssl/web /tmp/website05
git clone https://github.com/timovn/MyWebTools website06
git clone https://github.com/php/web-php website07
git clone https://github.com/cathschmidt/cathschmidt.github.io website08
tr ";" "\n" <<< "h1 cd /tmp/website01;h1 php -S 0.0.0.0:80 &;h2 cd /tmp/website02;h2 php -S 0.0.0.0:80 &;h3 cd /tmp/website03;h3 php -S 0.0.0.0:80 &;h4 cd /tmp/website04;h4 php -S 0.0.0.0:80 &;h5 cd /tmp/website05;h5 php -S 0.0.0.0:80 &;h6 cd /tmp/website06;h6 php -S 0.0.0.0:80 &;h7 cd /tmp/website07;h7 php -S 0.0.0.0:80 &;h8 cd /tmp/website08;h8 php -S 0.0.0.0:80 &;h9 dillo;exit" | sudo mn --topo tree,2,3
