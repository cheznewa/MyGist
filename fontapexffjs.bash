# Command Example :::::::::::::::::::::::::::: FONT_APEX=/path/to/font-apex/svgs bash fontapexffjs.bash 000000 ffffff 1
# Source ::::::::::::::::::::::::::::::::::::: https://github.com/oracle/font-apex/
color=$1
bgcol=$2
pntsz=$3
for f in $FONT_APEX/small/*.svg
do
printf "var apex_s_$(basename ${f} .svg | tr - _) = "
sed "s/<path /<path fill=\"#$color\" /g" < $f | rsvg-convert -b \#$bgcol -z $pntsz | png2ff | base256 --format=js
done
for f in $FONT_APEX/large/*.svg
do
printf "var apex_l_$(basename ${f} .svg | tr - _) = "
sed "s/<path /<path fill=\"#$color\" /g" < $f | rsvg-convert -b \#$bgcol -z $pntsz | png2ff | base256 --format=js
done
