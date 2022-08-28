# This Script Allow Replace Sound Effect From Assaut Rigs Game
RDT=$1
soundrmp=$2
a=$(mktemp)
b=$(mktemp)
sndone=$(mktemp)
sndtwo=$(mktemp)
head -c 594000 "$RDT" > $a
sox "$soundrmp" -r 22000 -c 1 -t u8 $sndone trim 0 1:41
sox "$soundrmp" -r 11000 -c 1 -t u8 $sndtwo trim 0 1:40
tail -c 77533507 "$RDT" > $b
cat $a $sndone $sndone $sndtwo $b
rm $a $sndone $sndtwo $b
