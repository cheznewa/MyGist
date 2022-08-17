rsync --exclude=pool/* --exclude=iso/* --exclude=images/* -v --copy-links -r rsync://ftp.rnl.tecnico.ulisboa.pt/pub/archlinux /tmp/archlinux
zip -r archlinux /tmp/archlinux
rm -fr /tmp/archlinux
