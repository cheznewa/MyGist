# required :::::
# https://github.com/lipis/flag-icons
# https://github.com/iptv-org/database/ iptv-data
# https://tools.suckless.org/farbfeld/
# https://github.com/thombashi/sqlitebiter - For Convert The CSV To SQLite Used
for i in $(seq 1 $1)
do
chn=$(sqlite3 -tabs $IPTVDATA_DB "select name,country,is_nsfw from channels order by random() limit 1")
ch=$(cut -f 1 -d "	" <<< "$chn")
cn=$(cut -f 2 -d "	" <<< "$chn" | tr A-Z a-z | sed s/uk/gb/)
ci=$(cut -f 3 -d "	" <<< "$chn")
if test $ci = "1"
then
rsvg-convert -z 10 $FLAGS/flags/4x3/${cn}.svg | convert png:- -resize $2 png:- | convert -fill red -gravity center -font "$3" -pointsize $2 +append png:- "label:\ $ch" png:- | png2ff | python2 $MYGIST/ff2clear.py rgb | DISPLAY=:0 lel -t "$ch" &
else
rsvg-convert -z 10 $FLAGS/flags/4x3/${cn}.svg | convert png:- -resize $2 png:- | convert -gravity center -font "$3" -pointsize $2 +append png:- "label:\ $ch" png:- | png2ff | python2 $MYGIST/ff2clear.py rgb | DISPLAY=:0 lel -t "$ch" &
fi
done
