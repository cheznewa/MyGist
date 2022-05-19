# required :::::
# https://github.com/vidaaudrey/011-World-Flags-SVG-And-PDF/
# https://github.com/iptv-org/database/ iptv-data
# https://ctan.org/texarchive/fonts/newcomputermodern
# https://tools.suckless.org/farbfeld/
for i in $(seq 1 $1)
do
chn=$(cut -f 2,5 -d , iptv-data/data/channels.csv | shuf -n 1)
ch=$(cut -f 1 -d , <<< "$chn")
cn=$(cut -f 2 -d , <<< "$chn" | tr A-Z a-z | sed s/uk/gb/)
rsvg-convert -z 10 flag-icons/flags/4x3/${cn}.svg | convert png:- -resize $2 png:- | convert -gravity center -font newcomputermodern/otf/NewCM10-Regular.otf -pointsize $2 +append png:- "label:\ $ch" png:- | png2ff | DISPLAY=:0 lel -t "$ch" &
done
