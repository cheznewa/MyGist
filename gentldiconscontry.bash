git clone https://github.com/lipis/flag-icons /tmp/flags
for flag in /tmp/flags/flags/1x1/*.svg
do
printf "ic--"
convert $flag -resize 16x16 ico:- | brotli | base58
printf "\n"
done
rm -fr /tmp/flags
