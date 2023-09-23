name=$1
lang=$2
publisher=$3
output=$4
tmp=$(mktemp -d)
yt-dlp -o "$tmp/%(title)s.%(ext)s" -f mp4 --write-thumbnail --write-description https://www.youtube.com/@${name}
printf "<h1>@${name}</h1>" >> $tmp/index.html
mogrify -format jpg $tmp/*.webp
for i in $tmp/*.mp4
do
n=$(basename "$i" .mp4)
printf "<img width="250" src=\"${n}.jpg\"/><br/>" >> $tmp/index.html
printf "<a href=\"${n}.html\">$n</a><br/><br/>" >> $tmp/index.html
printf "<h1>${n}</h1>" >> "$tmp/${n}.html"
printf "<video controls><source src=\"${n}.mp4\"/></video><br/>" >> "$tmp/${n}.html"
cat "$tmp/${n}.description" | sed ':a;N;$!ba;s/\n/<br\/>/g' >> "$tmp/${n}.html"
done
rm $tmp/*.description $tmp/*.webp
convert -size 256x256 xc: -fill red -draw "polygon 20,20 20,236 236,128" $tmp/icon.png
zimwriterfs -w index.html -f icon.png -l $lang -t "@${name}" -d "${name} Videos" -c "${name}" -p "${publisher}" $tmp "$output"
rm -r $tmp
