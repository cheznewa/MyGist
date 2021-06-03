# That Embed LogicEmu Circuit, Into A PNG File, And For Extract Read The Size In "Car" Using tail Command.
# Embed :::: logicemu2embed.bash output.png nameofcircuit < thecircuit.txt
# extract :: tail -c sizereadascar thepngfileasembed.png
img=$(mktemp)
circ=$(mktemp)
t=$(mktemp)
x=$(mktemp)
name=$2
out=$1
if test -z $name
then
name=CircuitSansNom
fi
convert -size 200x50 xc:none -stroke black -fill white -draw "rectangle 0,0 199,49 circle 25,25 15,25" miff:$img
convert -font OCRA -pointsize 9 -background none "label:$name" miff:- | composite -gravity center - $img miff:$t
base64 -w0 > $circ
s=$(base64 -d $circ | wc -c)
convert -font OCRA -pointsize 9 -background none "label:${s} Car" miff:- | composite -gravity southeast - $t png:$x
base64 -d $circ | cat $x - > $out
rm $img $circ $t