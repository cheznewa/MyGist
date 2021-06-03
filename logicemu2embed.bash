# That Embed LogicEmu Circuit, Into A PNG File, And For Extract Read The Size At Quotient In "Car" Using tail Command.
# Embed :::: logicemu2embed.bash nameofcircuit < thecircuit.txt > output.png
# extract :: tail -c sizereadquotienttaiascar thepngfileasembed.png | lzcomp -d
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
cat | lzcomp -f -o $circ
s=$(wc -c < $circ)
r=$(lzcomp -d < $circ | wc -c)
n=$(lzcomp -d < $circ | python2 $MYGIST/logicemu2luxar.py)
convert -font OCRA -pointsize 9 -background none "label:${s}/${r} Car" miff:- | composite -gravity southeast - $t miff:$w
convert -font OCRA -pointsize 9 -background none "label:${n}" miff:- | composite -gravity northeast - $w png:$x
cat $x $circ
rm $img $circ $t $x $w
