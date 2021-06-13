if test -z $MYGIST
then
printf "Please Declare MYGIST Variable When MyGist Repo On GitHub ::::: cheznewa/mygist\nAnd Dont Forget Use \"sudo\" For Admin With -E MYGIST=... To Declare The Variable.\n"
exit 1
fi
git clone https://github.com/B00merang-Project/B00merang-Flat /tmp/B00merang-Flat 2> /dev/null
acol=(
E41B1B\;Red
E4601B\;Orange
E4DD1B\;Yellow
1BE41E\;Green
868A93\;Gray
1B4DE4\;Blue
681BE4\;Purple
363B48\;Black
)
for n in $(seq 0 7)
do
name=$(cut -d ";" -f 2 <<< ${acol[$n]})
cp -r /tmp/B00merang-Flat /tmp/B00merang-Flat-${name}
hex=$(cut -d ";" -f 1 <<< ${acol[$n]})
python2 $MYGIST/coloreffectreplacer/coloreffectreplacer.py rmp "2081CE" "$hex" 200 < /tmp/B00merang-Flat/gtk-3.0/gtk.css > /tmp/B00merang-Flat-${name}/gtk-3.0/gtk.css
python2 $MYGIST/coloreffectreplacer/coloreffectreplacer.py rmp "2081CE" "$hex" 200 < /tmp/B00merang-Flat/gtk-3.0/gtk-dark.css > /tmp/B00merang-Flat-${name}/gtk-3.0/gtk-dark.css
python2 $MYGIST/coloreffectreplacer/coloreffectreplacer.py rmp "2081CE" "$hex" 200 < /tmp/B00merang-Flat/gtk-3.0/gtk-light.css > /tmp/B00merang-Flat-${name}/gtk-3.0/gtk-light.css
python2 $MYGIST/coloreffectreplacer/coloreffectreplacer.py rmp "2081CE" "$hex" 200 < /tmp/B00merang-Flat/gtk-2.0/gtkrc > /tmp/B00merang-Flat-${name}/gtk-2.0/gtkrc
python2 $MYGIST/coloreffectreplacer/coloreffectreplacer.py rmp "2081CE" "$hex" 200 < /tmp/B00merang-Flat/gnome-shell/gnome-shell.css > /tmp/B00merang-Flat-${name}/gnome-shell/gnome-shell.css
for m in /tmp/B00merang-Flat/gtk-2.0/assets/*.png
do
convert $m -fuzz 20% -fill "#$hex" -opaque "#2081CE" /tmp/B00merang-Flat-${name}/gtk-2.0/assets/$(basename $m)
done
for m in /tmp/B00merang-Flat/gtk-3.0/assets/*.png
do
convert $m -fuzz 20% -fill "#$hex" -opaque "#2081CE" /tmp/B00merang-Flat-${name}/gtk-3.0/assets/$(basename $m)
done
for m in /tmp/B00merang-Flat/gnome-shell/assets/*.png
do
convert $m -fuzz 20% -fill "#$hex" -opaque "#2081CE" /tmp/B00merang-Flat-${name}/gnome-shell/assets/$(basename $m)
done
cp -r /tmp/B00merang-Flat-${name} /usr/share/themes
printf "The Color ${name} Has Installed\n"
done
git clone https://github.com/vmware/clarity-city /tmp/Clarity-City 2> /dev/null
mkdir -p /usr/share/fonts/truetype/clarity-city
cp /tmp/Clarity-City/TrueType/*.ttf /usr/share/fonts/truetype/clarity-city
printf "The Font Clarity-City Has Installed\n"
printf "Please Edit .xsettingsd In Line Gtk/KeyThemeName=B00merang-Flat-(yourcolor) And Net/ThemeName=B00merang-Flat-(yourcolor)\n"
