text=$(mktemp)
render=$(mktemp)
curl -s "$1" | vilistextum - $text
if test $2 = A
then
gm convert -font /usr/local/share/fonts/EuropeanTeletext.ttf -pointsize 16 -size 768x5760 -background black -fill white "caption:@$text" miff:$render
fi
if test $2 = B
then
gm convert -font /usr/local/share/fonts/EuropeanTeletextNuevo.ttf -pointsize 16 -size 768x5760 -background black -fill white "caption:@$text" miff:$render
fi
rm $text
convert $render -crop 768x576 "gif:$3"