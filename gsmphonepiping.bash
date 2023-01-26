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
enc=$(tr -cd A-Za-z0-9 < /dev/urandom | head -c 8)
curl -s -T - ${server}/${up}_${down}_gsmphone <<< $enc > /dev/null &
sleep 1
dec=$(curl -s ${server}/${down}_${up}_gsmphone)
while test 1
do
rec -q -t s16 -r 8000 -c 1 - trim 0 $delay | toast -l | speckcrypt <(printf "$enc") - - | curl -s -T - ${server}/${up}_${down}_gsmphone > /dev/null &
curl -s ${server}/${down}_${up}_gsmphone | speckcrypt <(printf "$dec") - - | toast -d -l
done | play -q -t s16 -r 8000 -c 1 -
