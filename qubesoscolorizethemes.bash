if test -z $MYGIST
then
printf "Please Declare MYGIST Variable When MyGist Repo On GitHub ::::: cheznewa/mygist\nAnd Dont Forget Use \"sudo\" For Admin With -E MYGIST=... To Declare The Variable.\n"
exit 1
fi
git clone https://github.com/B00merang-Project/B00merang-Flat /tmp/B00merang-Flat
acol=(
cc0000\;Red
f57900\;Orange
edd400\;Yellow
73d216\;Green
555753\;Gray
3465a4\;Blue
75507b\;Purple
000000\;Black
)
for n in $(seq 0 7)
do
name=$(cut -d ";" -f 2 <<< ${acol[$n]})
cp -r /tmp/B00merang-Flat /tmp/B00merang-Flat-${name}
hex=$(cut -d ";" -f 1 <<< ${acol[$n]})
python2 $MYGIST/coloreffectreplacer.py rmp "2081CE" "$hex" 200 < /tmp/B00merang-Flat/gtk-3.0/gtk.css > /tmp/B00merang-Flat-${name}/gtk-3.0/gtk.css
python2 $MYGIST/coloreffectreplacer.py rmp "2081CE" "$hex" 200 < /tmp/B00merang-Flat/gtk-3.0/gtk-dark.css > /tmp/B00merang-Flat-${name}/gtk-3.0/gtk-dark.css
python2 $MYGIST/coloreffectreplacer.py rmp "2081CE" "$hex" 200 < /tmp/B00merang-Flat/gtk-3.0/gtk-light.css > /tmp/B00merang-Flat-${name}/gtk-3.0/gtk-light.css
python2 $MYGIST/coloreffectreplacer.py rmp "2081CE" "$hex" 200 < /tmp/B00merang-Flat/gtk-2.0/gtkrc > /tmp/B00merang-Flat-${name}/gtk-2.0/gtkrc
cp -r /tmp/B00merang-Flat-${name} /usr/share/themes
printf "The Color ${name} Has Installed\n"
done
printf "Please Edit .xsettingsd In Line Gtk/KeyThemeName=standard-(yourcolor) And Net/ThemeName=standard-(yourcolor)\n"
