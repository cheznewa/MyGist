if test -z $MYGIST
then
echo "Please Declare MYGIST Variable When MyGist Repo On GitHub ::::: cheznewa/mygist"
exit 1
fi
git clone https://github.com/B00merang-Project/Adwaita /tmp/standard
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
cp -r /tmp/standard /tmp/standard-${name}
hex=$(cut -d ";" -f 1 <<< ${acol[$n]})
python2 $MYGIST/coloreffectreplacer.py rmp "4A90D9" "$hex" 300 < /tmp/standard/gtk-3.0/gtk.css > /tmp/standard-${name}/gtk-3.0/gtk.css
python2 $MYGIST/coloreffectreplacer.py rmp "4A90D9" "$hex" 300 < /tmp/standard/gtk-3.0/gtk-dark.css > /tmp/standard-${name}/gtk-3.0/gtk-dark.css
python2 $MYGIST/coloreffectreplacer.py rmp "4A90D9" "$hex" 300 < /tmp/standard/gtk-2.0/gtkrc > /tmp/standard-${name}/gtk-2.0/gtkrc
cp -r /tmp/standard-${name} /usr/share/themes
done
echo "Please Edit .xsettingsd In Line Gtk/KeyThemeName=standard-(yourcolor) And Net/ThemeName=standard-(yourcolor)"
