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
split -a 16 -d -b 65536 $tmp ${tmp}_
for h in ${tmp}_*
do
sha3-256sum -N 1024 -b $h >> $hmp
done
rm ${tmp}_*
addr=$(sha3-256sum -N 1024 -b $hmp | base58)
printf "${server}/ppng${addr}\n"
while [[ $count -gt 0 ]]
do
curl -s -T - ${server}/ppng${addr} < $tmp > /dev/null
count=$(($count - 1))
done
rm $tmp $hmp