cd /tmp/
curl -sL https://github.com/SaiLikhith7/sailikhith7.github.io/tarball/master | tar -xvzf - && mv SaiLikhith7-sailikhith7.github.io* website01
curl -sL https://github.com/ybqu/ybqu.github.io/tarball/master | tar -xvzf - && mv ybqu-ybqu.github.io* website02
curl -sL https://github.com/femmebot/google-type/tarball/master | tar -xvzf - && mv femmebot-google-type* website03
curl -sL https://github.com/randomlike/randomlike/tarball/master | tar -xvzf - && mv randomlike-randomlike* website04
head -c 20000000 /dev/srandom > /tmp/website04/sample.bin
curl -sL https://github.com/mono/website/tarball/gh-pages | tar -xvzf - && mv mono-website* website05
curl -sL https://github.com/timovn/MyWebTools/tarball/master | tar -xvzf - && mv timovn-MyWebTools* website06
curl -sL https://github.com/php/web-php/tarball/master | tar -xvzf - && mv php-web-php* website07
curl -sL https://github.com/cathschmidt/cathschmidt.github.io/tarball/89db633ea0ec6c567e082b9dfb5de18361842afb | tar -xvzf - && mv cathschmidt-cathschmidt.github.io* website08
cd $HOME
tr ";" "\n" <<< "h1 cd /tmp/website01;h1 php -S 0.0.0.0:80 &;h2 cd /tmp/website02;h2 php -S 0.0.0.0:80 &;h3 cd /tmp/website03;h3 php -S 0.0.0.0:80 &;h4 cd /tmp/website04;h4 php -S 0.0.0.0:80 &;h5 cd /tmp/website05;h5 php -S 0.0.0.0:80 &;h6 cd /tmp/website06;h6 php -S 0.0.0.0:80 &;h7 cd /tmp/website07;h7 php -S 0.0.0.0:80 &;h8 cd /tmp/website08;h8 php -S 0.0.0.0:80 &;h9 dillo;exit" | sudo mn --topo tree,2,3
rm -fr /tmp/website*
