# Require ::::::: https://github.com/alanshaw/ipfs-only-hash
count=$1
server=$2
if [[ -z $server ]]
then
server="https://ppng.io"
fi
tmp=$(mktemp)
cat - > $tmp
n=0
addr=$(ipfs-only-hash --cid-version 0 $tmp)
printf "${server}/$addr\n"
while [[ $count -gt 0 ]]
do
curl -s -T - ${server}/$addr < $tmp > /dev/null
count=$(($count - 1))
done
rm $tmp