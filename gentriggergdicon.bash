tmp=$(mktemp)
color=$1
text=$2
convert -size 64x64 xc:none miff:$tmp
mogrify -fill $color -stroke black -draw "circle 32,32 15,32" miff:$tmp
mogrify -pointsize 12 -font Pusab -fill white -stroke black -gravity south -draw "text 0,0 \"$text\"" miff:$tmp
if test -n $3
then
mogrify -pointsize 24 -font Pusab -fill white -stroke black -gravity center -draw "text 0,0 \"$3\"" miff:$tmp
fi
convert $tmp png:-
rm $tmp
