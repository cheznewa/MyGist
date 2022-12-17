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
read -p "you : " send
curl -s -T - ${server}/${up}_chat <<< "$send" > /dev/null &
printf "$down : "
curl -s ${server}/${down}_chat
done
