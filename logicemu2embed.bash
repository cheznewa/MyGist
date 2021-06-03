# That Embed LogicEmu Circuit, Into A PNG File, And For Extract Read The Size In "Car" Using tail Command.
# Embed :::: logicemu2embed.bash nameofcircuit < thecircuit.txt > output.png
# extract :: tail -c sizereadascar thepngfileasembed.png
img=$(mktemp)
circ=$(mktemp)
t=$(mktemp)
w=$(mktemp)
x=$(mktemp)
name=$1
if test -z $name
then
name=CircuitSansNom
fi
convert -size 200x50 xc:none -stroke black -fill white -draw "rectangle 0,0 199,49 circle 25,25 15,25" miff:$img
convert -font OCRA -pointsize 9 -background none "label:$name" miff:- | composite -gravity center - $img miff:$t
base64 -w0 > $circ
s=$(base64 -d $circ | wc -c)
n=$(base64 -d $circ | python2 $MYGIST/logicemu2luxar.py)
convert -font OCRA -pointsize 9 -background none "label:${s} Car" miff:- | composite -gravity southeast - $t miff:$w
convert -font OCRA -pointsize 9 -background none "label:${n}" miff:- | composite -gravity northeast - $w png:$x
base64 -d $circ | cat $x -
rm $img $circ $t $x $w
