video=$(mktemp)
audio=$(mktemp)
zstd -dcq "$1" | python $MYGIST/radio/radiorecv.py $2 $3 16 | python $MYGIST/radio/avsplit.py 43200 768x576 25 4> $audio 7> $video
php $MYGIST/secam/secam2rgb.php 768 < $video | ffmpeg -video_size 768x576 -f rawvideo -pix_fmt rgb24 -i - -ar 43200 -ac 1 -f u8 -i $audio -vcodec libx264 -acodec copy -f avi -y "$4"
rm $audio $video