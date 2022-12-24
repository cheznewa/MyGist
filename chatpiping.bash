up=$2
down=$1
server=$3
if [[ -z $server ]]
then
server="https://ppng.io"
fi
enc=$(tr -cd 0-9 < /dev/urandom | head -c 100)
curl -s -T - ${server}/${up}_chat <<< $enc > /dev/null &
sleep 1
dec=$(curl -s ${server}/${down}_chat)
while test 1
do
read -p "you : " send
openssl rc4 -pbkdf2 -k $enc <<< "$send" | curl -s -T - ${server}/${up}_chat > /dev/null &
printf "$down : "
curl -s ${server}/${down}_chat | openssl rc4 -pbkdf2 -d -k $dec
done
