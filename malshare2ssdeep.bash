getdate=$1
tmp=$(mktemp)
taa=$(mktemp)
tab=$(mktemp)
tac=$(mktemp)
tad=$(mktemp)
curl -s -o $tmp https://malshare.com/daily/${getdate}/malshare_fileList.${getdate}.all.txt
cut -d "	" -f 3 $tmp > $taa
cut -d "	" -f 4 $tmp > $tab
for h in $(cat $taa)
do
printf "\"${h}\"\n"
done > $tad
paste -d , $tab $tad > $tac
printf "ssdeep,1.1--blocksize:hash:hash,filename\n" | cat - $tac > malshare_fileList.${getdate}.all.ssdeep
rm $tmp $taa $tab $tac $tad