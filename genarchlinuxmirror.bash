function genlist()
{
printf "<h1>Index : $1</h1>\n"
for a in $1/*
do
b=$(basename "$a")
printf "<a href=\"$b\">$b</a><br/>\n"
done
}
rsync --exclude=pool/* --exclude=iso/* --exclude=images/* -v --copy-links -r rsync://ftp.rnl.tecnico.ulisboa.pt/pub/archlinux /tmp/archlinux
for h in $(find /tmp/archlinux/archlinux -type d)
do
genlist "$h" > "$h/index.html"
done
zip -r archlinux /tmp/archlinux
rm -fr /tmp/archlinux
