cat /dev/urandom | tr -cd 0124 | while read -n 1 y
do
if test $y = 0
then
xdotool mousemove_relative -- -1 0
fi
if test $y = 1
then
xdotool mousemove_relative -- 1 0
fi
if test $y = 2
then
xdotool mousemove_relative -- 0 -1
fi
if test $y = 4
then
xdotool mousemove_relative -- 0 1
fi
done