fileplaylist=$1
timetorecord=$2
outputfile=$3
tmp=$(mktemp -d)
n=0
for url in $(grep -v "^#" "$fileplaylist")
do
ffmpeg -t $timetorecord -i "$url" -f rawvideo -pix_fmt rgb24 -vf framerate=25,scale=320x240 $tmp/${n}_video.raw -ar 18000 -ac 1 -f u8 $tmp/${n}_audio.raw
n=$(expr $n + 1)
done
for n in $(seq 0 $n)
do
python $MYGIST/radio/radiosend.py $(expr $n \* 100) $(expr $n \* 100 + 100) 8 < $tmp/${n}_audio.raw > $tmp/${n}_audio.radio
rm $tmp/${n}_audio.raw
php $MYGIST/secam/rgb2secam.php 320 < $tmp/${n}_video.raw | python $MYGIST/radio/radiosend.py $(expr $n \* 100) $(expr $n \* 100 + 100) 8 > $tmp/${n}_video.radio
rm $tmp/${n}_video.raw
done
paste -d "\n" $tmp/*_audio.radio | sed "/^$/d" | zstd -v -22 --ultra > "${outputfile}_audio.radio.zstd"
paste -d "\n" $tmp/*_video.radio | sed "/^$/d" | zstd -v -22 --ultra > "${outputfile}_video.radio.zstd"
rm -r $tmp
