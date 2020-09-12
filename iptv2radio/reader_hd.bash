video=$(mktemp)
audio=$(mktemp)
zstd -dcq "$1" | python $MYGIST/radio/radiorecv.py $2 $3 16 | python $MYGIST/radio/avsplit.py 43200 720x576 25 4> $audio 7> $video
python $MYGIST/secam/secam2rgb.py 720 < $video | ffmpeg -video_size 720x576 -f rawvideo -pix_fmt rgb24 -i - -ar 43200 -ac 1 -f mulaw -i $audio -vcodec libx264 -acodec copy -f avi -y "$4"
rm $audio $video