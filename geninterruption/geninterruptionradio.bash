intone=30
inttwo=43
intthree=67
intfour=101
intfive=115

tmp=$(mktemp -d)

sox "$1" -r 10000 -c 1 -t u16 - trim 0 $(expr $intone + $7)   | python $MYGIST/radio/radiosend.py 0 1000 16 > $tmp/intone.radio
sox "$2" -r 10000 -c 1 -t u16 - trim 0 $(expr $inttwo + $7)   | python $MYGIST/radio/radiosend.py 1000 2000 16 > $tmp/inttwo.radio
sox "$3" -r 10000 -c 1 -t u16 - trim 0 $(expr $intthree + $7) | python $MYGIST/radio/radiosend.py 2000 3000 16 > $tmp/intthree.radio
sox "$4" -r 10000 -c 1 -t u16 - trim 0 $(expr $intfour + $7)  | python $MYGIST/radio/radiosend.py 3000 4000 16 > $tmp/intfour.radio
sox "$5" -r 10000 -c 1 -t u16 - trim 0 $(expr $intfive + $7)  | python $MYGIST/radio/radiosend.py 4000 5000 16 > $tmp/intfive.radio

paste -d "\n" $tmp/intone.radio $tmp/inttwo.radio $tmp/intthree.radio $tmp/intfour.radio $tmp/intfive.radio | sed "/^$/d" > "$6"
