# Usage ::: chatpiping.bash you peer [server]
# Required ::: https://github.com/electrorys/speckcipher
up=$1
down=$2
server=$3
if [[ -z $server ]]
then
server="https://ppng.io"
fi
enc=$(tr -cd A-Za-z0-9 < /dev/urandom | head -c 8)
curl -s -T - ${server}/${up}_${down}_chat <<< $enc > /dev/null &
sleep 1
dec=$(curl -s ${server}/${down}_${up}_chat)
while test 1
do
read -p "you : " send
speckcrypt <(printf "$enc") - - <<< "$send" | curl -s -T - ${server}/${up}_${down}_chat > /dev/null &
printf "$down : "
curl -s ${server}/${down}_${up}_chat | speckcrypt <(printf "$dec") - -
done
