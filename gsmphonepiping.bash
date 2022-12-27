# Usage ::: gsmphonepiping.bash you peer delay [server]
# Required :::::::::::::::::::: https://quut.com/gsm/ Then https://github.com/electrorys/speckcipher
# And SoX
up=$1
down=$2
delay=$3
server=$4
if [[ -z $server ]]
then
server="https://ppng.io"
fi
enc=$(mktemp)
dec=$(mktemp)
head -c 16 /dev/urandom > $enc
curl -s -T - ${server}/${up}_gsmphone < $enc > /dev/null &
sleep 1
curl -s ${server}/${down}_gsmphone > $dec
while test 1
do
rec -q -t s16 -r 8000 -c 1 - trim 0 $delay | toast -l | speckcrypt $enc - - | curl -s -T - ${server}/${up}_gsmphone > /dev/null &
curl -s ${server}/${down}_gsmphone | speckcrypt $dec - - | toast -d -l
done | play -q -t s16 -r 8000 -c 1 -
