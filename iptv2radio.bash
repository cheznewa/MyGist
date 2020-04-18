fileplaylist=$1
timetorecord=$2
outputfile=$3
tmp=$(mktemp -d)
n=0
for url in $(grep -v "^#" "$fileplaylist")
do
ffmpeg -t $timetorecord -i "$url" -f rawvideo -pix_fmt yuv422p -vf framerate=25,scale=320x240 $tmp/${n}_video.raw -ar 10000 -ac 1 -f u16le $tmp/${n}_audio.raw
n=$(expr $n + 1)
done
for n in $(seq 0 $n)
do
python $MYGIST/radio/radiosend.py $(expr $n \* 10000) $(expr $n \* 10000 + 10000) 16 < $tmp/${n}_audio.raw > $tmp/${n}_audio.radio
python $MYGIST/radio/radiosend.py $(expr $n \* 10000) $(expr $n \* 10000 + 10000) 16 < $tmp/${n}_video.raw > $tmp/${n}_video.radio
done
paste -d "\n" $tmp/*_audio.radio | sed "/^$/d" | zstd -v -22 --ultra > "${outputfile}_audio.radio.zstd"
paste -d "\n" $tmp/*_video.radio | sed "/^$/d" | zstd -v -22 --ultra > "${outputfile}_video.radio.zstd"