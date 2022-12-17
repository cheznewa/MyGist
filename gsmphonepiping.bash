# Required :::::::::::::::::::: https://quut.com/gsm/
# And SoX
up=$1
down=$2
server=$3
if [[ -z $server ]]
then
server="https://ppng.io"
fi
while test 1
do
rec -q -t s16 -r 8000 -c 1 - trim 0 1 | toast -l | curl -s -T - ${server}/${up}_gsmphone > /dev/null &
curl -s ${server}/${down}_gsmphone | toast -d -l | play -q -t s16 -r 8000 -c 1 - trim 0 1 &
sleep 1
done
