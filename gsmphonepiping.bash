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
rec -t s16 -r 8000 -c 1 - trim 0 1 | toast -l | curl -T - ${server}/${up}_gsmphone &
curl -s ${server}/${down}_gsmphone | toast -d -l | play -t s16 -r 8000 -c 1 - trim 0 1 &
sleep 1
done
