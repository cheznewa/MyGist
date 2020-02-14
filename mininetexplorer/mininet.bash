git clone https://github.com/SaiLikhith7/sailikhith7.github.io /tmp/website01
git clone https://github.com/ybqu/ybqu.github.io /tmp/website02
tr ";" "\n" <<< "h1 cd /tmp/website01;h1 php -S 0.0.0.0:80 &;h2 cd /tmp/website02;h2 php -S 0.0.0.0:80 &;h25 pterm -e links;exit" | sudo mn --topo tree,3,3
