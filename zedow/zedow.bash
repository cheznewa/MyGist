tmp=$(mktemp -d)
mode=$1
vmname=$2
key=$3
site=$4
if test export = $mode
then
vboxmanage export "$vmname" -o $tmp/${vmname}.ova
mcencrypt 4< "$key" < $tmp/${vmname}.ova | split -a 10 -b 5242880 - "$ZERONET/data/${site}/${vmname}"
python3 "$ZERONET/zeronet.py" siteSign $site
python3 "$ZERONET/zeronet.py" sitePublish $site
fi

if test import = $mode
then
if test \! \( -d $ZERONET/data/${site} \)
then
python3 "$ZERONET/zeronet.py" siteDownload $site
fi
cat "$ZERONET/data/${site}/${vmname}"?????????? | mcdecrypt 8< "$key" > $tmp/${vmname}.ova
vboxmanage import $tmp/${vmname}.ova
fi

rm -r $tmp