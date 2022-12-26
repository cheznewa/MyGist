# Usage ::: chatpiping.bash you peer [server]
up=$1
down=$2
server=$3
if [[ -z $MYGIST ]]
then
exit 1
fi
if [[ -z $server ]]
then
server="https://ppng.io"
fi
enc=$(shuf -i 0-255 | tr "\n" " ")
curl -s -T - ${server}/${up}_chat <<< $enc > /dev/null &
sleep 1
dec=$(curl -s ${server}/${down}_chat)
while test 1
do
read -p "you : " send
python2 $MYGIST/rc4.py $enc <<< "$send" | curl -s -T - ${server}/${up}_chat > /dev/null &
printf "$down : "
curl -s ${server}/${down}_chat | python2 $MYGIST/rc4.py $dec
done
