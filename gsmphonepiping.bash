# Required :::::::::::::::::::: https://quut.com/gsm/
# And SoX
up=$1
down=$2
server=$3
if [[ -z $server ]]
then
server="https://ppng.io"
fi
enc=$(tr -cd 0-9 < /dev/urandom | head -c 100)
curl -s -T - ${server}/${up}_gsmphone <<< $enc > /dev/null &
sleep 1
dec=$(curl -s ${server}/${down}_gsmphone)
while test 1
do
rec -q -t s16 -r 8000 -c 1 - trim 0 1 | toast -l | openssl rc4 -pbkdf2 -k $enc | curl -s -T - ${server}/${up}_gsmphone > /dev/null &
curl -s ${server}/${down}_gsmphone | openssl rc4 -pbkdf2 -d -k $dec | toast -d -l
sleep 1
done | play -q -t s16 -r 8000 -c 1 -
