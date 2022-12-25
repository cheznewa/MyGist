# Required :::::::::::::::::::: https://quut.com/gsm/
# And SoX
up=$1
down=$2
delay=$3
server=$4
if [[ -z $MYGIST ]]
then
exit 1
fi
if [[ -z $server ]]
then
server="https://ppng.io"
fi
enc=$(shuf -i 0-255 | tr "\n" " ")
curl -s -T - ${server}/${up}_gsmphone <<< $enc > /dev/null &
sleep 1
dec=$(curl -s ${server}/${down}_gsmphone)
while test 1
do
rec -q -t s16 -r 8000 -c 1 - trim 0 $delay | toast -l | python2 $MYGIST/rc4.py $enc | curl -s -T - ${server}/${up}_gsmphone > /dev/null &
curl -s ${server}/${down}_gsmphone | python2 $MYGIST/rc4.py $dec | toast -d -l
done | play -q -t s16 -r 8000 -c 1 -
