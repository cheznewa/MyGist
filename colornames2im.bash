printf "<colormap>\n"
tmp=$(mktemp -d)
names=()
ids=()
curl -s -o $tmp/cn.zip https://colornames.org/download/colornames.zip
for line in $(unzip -p $tmp/cn.zip | tr -d " ")
do
id=0
color=$(cut -d , -f 1 <<< $line)
name=$(cut -d , -f 2 <<< $line)
for n in ${!names[@]}
do
if test ${names[n]} = ${name}
then
id=$(expr $id + 1)
fi
done
printf "<color name=\"${name}${id}\" color=\"#${color}\" compliance=\"SVG, X11, XPM\"/>\n"
names+=(${name})
done
printf "</colormap>\n"