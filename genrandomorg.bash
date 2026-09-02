nbbytes=$1
bytes=16384
while [ $nbbytes -ge 0 ]
do
if [ $nbbytes -lt 16384 ]
then
bytes=$nbbytes
fi
curl -s "https://www.random.org/cgi-bin/randbyte?nbytes=$bytes&format=f"
sleep 0.1
nbbytes=$(($nbbytes - 16384))
done