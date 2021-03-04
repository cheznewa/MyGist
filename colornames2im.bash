printf "<colormap>\n"
if test \! \( -f colornames.zip \)
then
curl -O -s https://colornames.org/download/colornames.zip
fi
for line in $(unzip -p colornames.zip | tr -d " " |  sort -n -t , -k 3 -r)
do
color=$(cut -d , -f 1 <<< $line)
name=$(cut -d , -f 2 <<< $line)
printf "<color name=\"${name}\" color=\"#${color}\" compliance=\"SVG, X11, XPM\"/>\n"
done
printf "</colormap>\n"
