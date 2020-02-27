while test 1
do
c=$(ls channels | pick)
mpv --osd-font=retrotv --sub-font=retrotv --video-aspect=16:9 --fs $(cat channels/$c | grep -v "#" | pick)
done