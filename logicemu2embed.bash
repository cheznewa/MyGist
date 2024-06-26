# That Embed LogicEmu Circuit, Into A PNG File, And For Extract Read The Size At Quotient In "Car" Using tail Command.
# Embed :::: logicemu2embed.bash nameofcircuit < thecircuit.txt > output.png
# extract :: tail -c sizereadquotienttaiascar thepngfileasembed.png | lzcomp -d
img=$(mktemp)
circ=$(mktemp)
logo=$(mktemp)
t=$(mktemp)
w=$(mktemp)
x=$(mktemp)
name=$1
logo=$2
if test -z $name
then
name=CircuitSansNom
fi
if test ! \( -z $logo \)
then
curl -o $logo https://raw.githubusercontent.com/gilbarbara/logos/master/logos/${logo}.svg
logoblacked=$(mktemp)
python2 $MYGIST/coloreffectreplacer/coloreffectreplacer.py sub 255 255 255 < $logo > $logoblacked
fi
convert -size 200x50 xc:none -stroke black -fill white -draw "rectangle 0,0 199,49 circle 25,25 15,25" miff:$img
convert -font OCRA -pointsize 9 -background none "label:$name" miff:- | composite -gravity center - $img miff:$t
cat | lzcomp -f -o $circ
s=$(wc -c < $circ)
r=$(lzcomp -d < $circ | wc -c)
n=$(lzcomp -d < $circ | python2 $MYGIST/logicemu2luxar.py)
convert -font OCRA -pointsize 9 -background none "label:${s}/${r} Car" miff:- | composite -gravity southeast - $t miff:$w
convert -font OCRA -pointsize 9 -background none "label:${n}" miff:- | composite -gravity northeast - $w png:$x
if test ! \( -z $logo \)
then
rsvg-convert -z 0.1 $logoblacked | composite -gravity east - $x png:$x
rm $logoblacked
fi
cat $x $circ
rm $img $circ $t $x $w $logo
