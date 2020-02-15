cd /tmp/
curl -sL https://github.com/SaiLikhith7/sailikhith7.github.io/tarball/master | tar -xvzf - && mv SaiLikhith7-sailikhith7.github.io* website01
curl -sL https://github.com/ybqu/ybqu.github.io/tarball/master | tar -xvzf - && mv ybqu-ybqu.github.io* website02
curl -sL https://github.com/femmebot/google-type/tarball/master | tar -xvzf - && mv femmebot-google-type* website03
curl -sL https://github.com/randomlike/randomlike/tarball/master | tar -xvzf - && mv randomlike-randomlike* website04
head -c 20000000 /dev/srandom > /tmp/website04/sample.bin
curl -sL https://github.com/libra/website/tarball/gh-pages | tar -xvzf - && mv libra-website* website05
curl -sL https://github.com/timovn/MyWebTools/tarball/master | tar -xvzf - && mv timovn-MyWebTools* website06
curl -sL https://github.com/Cyan4973/xxHash/tarball/gh-pages | tar -xvzf - && mv Cyan4973-xxHash* website07
curl -sL https://github.com/facebook/zstd/tarball/gh-pages | tar -xvzf - && mv facebook-zstd* website08
curl -sL https://github.com/gireeshcse/gireeshcse.github.io/tarball/master | tar -xvzf - && mv gireeshcse-gireeshcse.github.io* website09
curl -sL https://github.com/JonLz/jonlz.github.com/tarball/master | tar -xvzf - && mv JonLz-jonlz.github.com* website10
curl -sL https://github.com/goreliu/asciinema_statistics/tarball/master | tar -xvzf - && mv goreliu-asciinema_statistics* website11
cd website11
zsh bin/update && zsh bin/generate
cd /tmp/
curl -sL https://github.com/revoxhere/duco-statistics/tarball/master | tar -xvzf - && mv revoxhere-duco-statistics* website12
cd $HOME
tr ";" "\n" <<< "h1 cd /tmp/website01;h1 php -S 0.0.0.0:80 &;h2 cd /tmp/website02;h2 php -S 0.0.0.0:80 &;h3 cd /tmp/website03;h3 php -S 0.0.0.0:80 &;h4 cd /tmp/website04;h4 php -S 0.0.0.0:80 &;h5 cd /tmp/website05;h5 php -S 0.0.0.0:80 &;h6 cd /tmp/website06;h6 php -S 0.0.0.0:80 &;h7 cd /tmp/website07;h7 php -S 0.0.0.0:80 &;h8 cd /tmp/website08;h8 php -S 0.0.0.0:80 &;h9 cd /tmp/website09;h9 php -S 0.0.0.0:80 &;
h10 cd /tmp/website10;h10 php -S 0.0.0.0:80 &;h11 cd /tmp/website11;h11 php -S 0.0.0.0:80 &;h12 cd /tmp/website12;h12 php -S 0.0.0.0:80 &;
h27 dillo;exit" | sudo mn --topo tree,3,3
rm -fr /tmp/website*
