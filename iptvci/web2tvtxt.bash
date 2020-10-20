render=$(mktemp)
title=$(mktemp)
if test $2 = A
then
font=/usr/local/share/fonts/EuropeanTeletext.ttf
fi
if test $2 = B
then
font=/usr/local/share/fonts/EuropeanTeletextNuevo.ttf
fi
gm convert -font $font -pointsize 16 -size 768x560 -background black -fill white "caption:$(curl -s '$1' | vilistextum - -" miff:$render
gm convert -font $font -pointsize 16 -size 768x16  -background white -fill black "caption:'$3' - $(date)" miff:$title
gm convert -append $reader $title "$4"