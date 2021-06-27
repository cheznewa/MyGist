tmp=$(mktemp -d)
for win in $(wmctrl -l | cut -d " " -f 1)
do
import -window "$win" "$tmp/$win.png"
done
tar -C $tmp -cf "$1".tar .
rm -r $tmp
