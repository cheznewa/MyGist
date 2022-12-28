# Command Example :::::::::::::::::::::::::::: FONT_APEX=/path/to/font-apex/svgs bash fontapexffjs.bash name 000000 1
# Command Example With Modifier :::::::::::::::::::::::::::: FONT_APEX=/path/to/font-apex/svgs bash fontapexffjs.bash name 000000 1 blank ff0000
# Source ::::::::::::::::::::::::::::::::::::: https://github.com/oracle/font-apex/
if [[ -z $FONT_APEX ]]
then
exit 1
fi
names=$1
color=$2
pntsz=$3
modif=$4
clmod=$5
if [[ -z $color ]]
then
color="000000"
pntsz=1
fi
if [[ -n $modif ]]
then
if [[ -z $clmod ]]
then
clmod="000000"
fi
tmp=$(mktemp)
sed "s/<path /<path fill=\"#$clmod\" /g" < $FONT_APEX/small/modifier-$modif.svg | rsvg-convert -z $pntsz | convert png:- -resize 50% miff:$tmp
for f in $FONT_APEX/small/*.svg
do
printf "var apex_s_$(basename ${f} .svg | tr - _)_${names} = "
sed "s/<path /<path fill=\"#$color\" /g" < $f | rsvg-convert -z $pntsz | composite -gravity southeast miff:$tmp png:- png:- | png2ff | base256 --format=js
done
sed "s/<path /<path fill=\"#$clmod\" /g" < $FONT_APEX/large/modifier-$modif.svg | rsvg-convert -z $pntsz | convert png:- -resize 50% miff:$tmp
for f in $FONT_APEX/large/*.svg
do
printf "var apex_l_$(basename ${f} .svg | tr - _)_${names} = "
sed "s/<path /<path fill=\"#$color\" /g" < $f | rsvg-convert -z $pntsz | composite -gravity southeast miff:$tmp png:- png:- | png2ff | base256 --format=js
done
rm $tmp
else
for f in $FONT_APEX/small/*.svg
do
printf "var apex_s_$(basename ${f} .svg | tr - _)_${names} = "
sed "s/<path /<path fill=\"#$color\" /g" < $f | rsvg-convert -z $pntsz | png2ff | base256 --format=js
done
for f in $FONT_APEX/large/*.svg
do
printf "var apex_l_$(basename ${f} .svg | tr - _)_${names} = "
sed "s/<path /<path fill=\"#$color\" /g" < $f | rsvg-convert -z $pntsz | png2ff | base256 --format=js
done
fi

