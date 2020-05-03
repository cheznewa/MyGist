intone=30
inttwo=43
intthree=67
intfour=101
intfive=115

tmp=$(mktemp -d)

ffmpeg -y -t $(expr $intone + $7) -i "$1"    -vf framerate=40,scale=768x576 -vcodec libx264 -an $tmp/one.avi
ffmpeg -y -t $(expr $inttwo + $7) -i "$2"    -vf framerate=40,scale=768x576 -vcodec libx264 -an $tmp/two.avi
ffmpeg -y -t $(expr $intthree + $7) -i "$3"  -vf framerate=40,scale=768x576 -vcodec libx264 -an $tmp/three.avi
ffmpeg -y -t $(expr $intfour + $7)  -i "$4"  -vf framerate=40,scale=768x576 -vcodec libx264 -an $tmp/four.avi
ffmpeg -y -t $(expr $intfive + $7) -i "$5"   -vf framerate=40,scale=768x576 -vcodec libx264 -an $tmp/five.avi

ffmpeg -y  -f rawvideo -pix_fmt gray -video_size 768x576 -r 40 -t $(expr 130 - $intone) -i /dev/urandom   -vcodec libx264 $tmp/intone.avi
ffmpeg -y  -f rawvideo -pix_fmt gray -video_size 768x576 -r 40 -t $(expr 130 - $inttwo) -i /dev/urandom   -vcodec libx264 $tmp/inttwo.avi
ffmpeg -y  -f rawvideo -pix_fmt gray -video_size 768x576 -r 40 -t $(expr 130 - $intthree) -i /dev/urandom -vcodec libx264 $tmp/intthree.avi
ffmpeg -y  -f rawvideo -pix_fmt gray -video_size 768x576 -r 40 -t $(expr 130 - $intfour) -i /dev/urandom  -vcodec libx264 $tmp/intfour.avi
ffmpeg -y  -f rawvideo -pix_fmt gray -video_size 768x576 -r 40 -t $(expr 130 - $intfive) -i /dev/urandom  -vcodec libx264 $tmp/intfive.avi

ffmpeg -y  -i "concat:$tmp/one.avi|$tmp/intone.avi" -an -vcodec copy $tmp/onemerge.avi
ffmpeg -y  -i "concat:$tmp/two.avi|$tmp/inttwo.avi" -an -vcodec copy $tmp/twomerge.avi
ffmpeg -y  -i "concat:$tmp/three.avi|$tmp/intthree.avi" -an -vcodec copy $tmp/threemerge.avi
ffmpeg -y  -i "concat:$tmp/four.avi|$tmp/intfour.avi" -an -vcodec copy $tmp/fourmerge.avi
ffmpeg -y  -i "concat:$tmp/five.avi|$tmp/intfive.avi" -an -vcodec copy $tmp/fivemerge.avi

if test \! \( -f  a2n.mp4 \)
then
youtube-dl -f mp4 -o a2n.mp4 https://www.youtube.com/watch?v=cpNxOE2rMOY
fi

convert -size 768x576 xc:black $tmp/bg.png
sox -n -c 2 -r 41100 -L $tmp/null.wav trim 0 $7
ffmpeg -y -loop 1 -i $tmp/bg.png -i $tmp/null.wav -acodec mp2 -vcodec libx264 -r 40 -t $7 -vf "fps=40,drawtext=fontfile='/usr/share/fonts/truetype/opensans/OpenSans-Regular.ttf':fontcolor=white:fontsize=80:x=\(w-text_w\)/2:y=\(h-text_h\)/2:text='%{eif\:$7-t\:d}'" $tmp/countdown.avi

ffmpeg -y -i a2n.mp4 -acodec mp2 -vcodec libx264 -vf framerate=40,scale=768x576 $tmp/a2n.avi
ffmpeg -y -i "concat:$tmp/countdown.avi|$tmp/a2n.avi" -acodec copy -vcodec copy $tmp/a2ncd.avi

ffmpeg -y -i $tmp/onemerge.avi -i $tmp/twomerge.avi -i $tmp/threemerge.avi -i $tmp/fourmerge.avi -i $tmp/fivemerge.avi -i $tmp/a2ncd.avi -filter_complex "[0][1][2]hstack=inputs=3[ga];[3][4][5]hstack=inputs=3[gb];[ga][gb]vstack=shortest=1[final]" -map "[final]" -map 5:1 -vcodec libx264 -acodec copy -t $(expr 130 + $7) "$6"
