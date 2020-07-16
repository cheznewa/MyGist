# Radio Emulation Generator France
timing=$1
output=$2
tmp=$(mktemp -d)
sox -t mp3 http://live02.rfi.fr/rfimonde-96k.mp3 -t u16 -r 12000 -c 1 $tmp/rfi.raw trim 0 $timing &
sox -t mp3 http://direct.francebleu.fr/live/fb1071-midfi.mp3 -t u16 -r 12000 -c 1 $tmp/francebleu.raw trim 0 $timing &
sox -t mp3 http://direct.franceinter.fr/live/franceinter-midfi.mp3 -t u16 -r 12000 -c 1 - trim 0 $timing | python $MYGIST/radio/radiosend.py 8760000 8770000 16 > $tmp/franceinter.radio &
sox -t mp3 http://generationfm.ice.infomaniak.ch/generationfm-high.mp3 -t u16 -r 12000 -c 1 - trim 0 $timing | python $MYGIST/radio/radiosend.py 8820000 8812000 16 > $tmp/generations.radio &
sox -t mp3 https://scdn.nrjaudio.fm/audio1/fr/30601/mp3_128.mp3 -t u16 -r 12000 -c 1 - trim 0 $timing | python $MYGIST/radio/radiosend.py 9040000 9050000 16 > $tmp/nostalgie.radio &
sox -t mp3 http://stream1.evasionfm.com/Chante_France -t u16 -r 12000 -c 1 - trim 0 $timing | python $MYGIST/radio/radiosend.py 9090000 9100000 16 > $tmp/chantefrance.radio &
sox -t mp3 http://icecast.skyrock.net/s/natio_mp3_128k -t u16 -r 12000 -c 1 - trim 0 $timing | python $MYGIST/radio/radiosend.py 9600000 9610000 16 > $tmp/skyrock.radio &
sox -t mp3 http://broadcast.infomaniak.net/start-voltage-high.mp3 -t u16 -r 12000 -c 1 - trim 0 $timing | python $MYGIST/radio/radiosend.py 9690000 9700000 16 > $tmp/voltage.radio &
sox -t mp3 https://scdn.nrjaudio.fm/audio1/fr/30401/mp3_128.mp3 -t u16 -r 12000 -c 1 - trim 0 $timing | python $MYGIST/radio/radiosend.py 9740000 9750000 16 > $tmp/rireetchansons.radio &
sox -t mp3 https://scdn.nrjaudio.fm/audio1/fr/30001/mp3_128.mp3 -t u16 -r 12000 -c 1 - trim 0 $timing | python $MYGIST/radio/radiosend.py 10012000 10040000 16 > $tmp/nrj.radio &
sox -t mp3 https://start-sud.ice.infomaniak.ch/start-sud-high.mp3 -t u16 -r 12000 -c 1 - trim 0 $timing | python $MYGIST/radio/radiosend.py 9990000 10000000 16 > $tmp/sudradio.radio &
sox -t mp3 http://streaming.radio.funradio.fr/fun-1-44-128 -t u16 -r 12000 -c 1 - trim 0 $timing | python $MYGIST/radio/radiosend.py 10190000 10200000 16 > $tmp/virginradio.radio &
sox -t mp3 http://streaming.radio.rtl.fr/rtl-1-44-128 -t u16 -r 12000 -c 1 - trim 0 $timing | python $MYGIST/radio/radiosend.py 10412000 10440000 16 > $tmp/rtl.radio &
sleep $timing
sox -t u16 -r 12000 -c 1 $tmp/rfi.raw -r 12000 -t ul -c 1 $tmp/rfi_ul.raw
python $MYGIST/radio/radiosend.py 8900000 8910000 16 < $tmp/rfi.raw > $tmp/rfi.radio
python $MYGIST/radio/radiosend.py 73800 73900 8 < $tmp/rfi_ul.raw > $tmp/rfi_ul.radio
sox -t u16 -r 12000 -c 1 $tmp/francebleu.raw -r 12000 -t ul -c 1 $tmp/francebleu_ul.raw
python $MYGIST/radio/radiosend.py 10710000 10720000 16 < $tmp/francebleu.raw > $tmp/francebleu.radio
python $MYGIST/radio/radiosend.py 86400 86500 8 < $tmp/francebleu_ul.raw > $tmp/francebleu_ul.radio
paste -d "\n" $tmp/*.radio | sed "/^$/d" | zstd -v -22 --ultra > "${output}.radio.zstd"
rm -r $tmp