# Usage ::: chatpiping.bash you peer [server]
# Required ::: https://github.com/electrorys/speckcipher
up=$1
down=$2
server=$3
if [[ -z $server ]]
then
server="https://ppng.io"
fi
enc=$(mktemp)
dec=$(mktemp)
head -c 16 /dev/urandom > $enc
curl -s -T - ${server}/${up}_chat < $enc > /dev/null &
sleep 1
curl -s ${server}/${down}_chat > $dec
while test 1
do
read -p "you : " send
speckcrypt $enc - - <<< "$send" | curl -s -T - ${server}/${up}_chat > /dev/null &
printf "$down : "
curl -s ${server}/${down}_chat | speckcrypt $dec - -
done
