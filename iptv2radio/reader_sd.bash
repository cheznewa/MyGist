video=$(mktemp)
audio=$(mktemp)
zstd -dcq "$1" | python $MYGIST/radio/radiorecv.py $2 $3 16 | python $MYGIST/radio/avsplit.py 18000 320x240 25 4> $audio 7> $video
php $MYGIST/secam/secam2rgb.php 320 < $video | ffmpeg -video_size 320x240 -f rawvideo -pix_fmt rgb24 -i - -ar 18000 -ac 1 -f mulaw -i $audio -vcodec libx264 -acodec copy -f avi -y "$4"
rm $audio $video