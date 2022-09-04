function genlist()
{
printf "<h1>Index : $1</h1>\n"
printf "<a href=\"../index.html\">..</a><br/>\n"
for a in $1/*
do
b=$(basename "$a")
if test -d "$a"
then
printf "<a href=\"$b/index.html\">$b</a><br/>\n"
else
printf "<a href=\"$b\">$b</a><br/>\n"
fi
done
}
rsync --exclude=pool/* --exclude=iso/* --exclude=images/* -v --copy-links -r rsync://ftp.rnl.tecnico.ulisboa.pt/pub/archlinux /tmp/archlinux
for h in $(find /tmp/archlinux/archlinux -type d)
do
genlist "$h" > "$h/index.html"
done
zip -r archlinux /tmp/archlinux
rm -fr /tmp/archlinux
