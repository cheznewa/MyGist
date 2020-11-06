# Please Run On Dom0 (You Cannot Copy/Paste To Dom0) :::::::::: qvm-run -p yourvm "cat /home/user/mygist/morecolorqubesos.bash" | bash
colors=(
800000
9A6324
808000
469990
000075
000000
E6194B
F58231
FFE119
BFEF45
3CB44B
42D4F4
4363D8
911EB4
F032E6
A9A9A9
FABED4
FFD8B1
FFFAC8
AAFFC3
DCBEFF
FFFFFF
)
names=(
Maroon
Brown
Olive
Teal
Navy
Black
Red
Orange
Yellow
Lime
Green
Cyan
Blue
Purple
Magenta
Gray
Pink
Apricot
Beige
Mint
Lavender
White
)
for n in $(seq 0 21)
do
qubesd-query dom0 admin.label.Create dom0 ${names[$n]} <<< "0x${colors[$n]}"
sudo convert -size 20x20 xc:\#${colors[$n]} -stroke black -fill none -draw "rectangle 0,0 20,20" /usr/share/icons/hicolor/128x128/devices/appvm-${names[$n]}.png
sudo convert -size 20x20 xc:\#${colors[$n]} -stroke black -fill none -draw "rectangle 0,0 20,20" -fill white -stroke none -draw "rectangle 8,8 12,12" /usr/share/icons/hicolor/128x128/devices/dispvm-${names[$n]}.png
done
