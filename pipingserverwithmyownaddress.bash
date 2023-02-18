# Require ::::::: https://github.com/keis/base58 ;;; https://github.com/maandree/sha3sum
count=$1
server=$2
if [[ -z $server ]]
then
server="https://ppng.io"
fi
tmp=$(mktemp)
hmp=$(mktemp)
cat - > $tmp
n=0
split -a 16 -d -b 1024 $tmp ${tmp}_
for h in ${tmp}_*
do
cat $h $hmp | sha3-256sum -b > $hmp
done
rm ${tmp}_*
addr=$(base58 $hmp)
printf "${server}/ppng${addr}\n"
while [[ $count -gt 0 ]]
do
curl -s -T - ${server}/ppng${addr} < $tmp > /dev/null
count=$(($count - 1))
done
rm $tmp $hmp