# Radio Emulation Generator France
if test -z $MYGIST
then
exit 1
fi
timing=$1
tmp=$(mktemp -d)
sox -t mp3 http://direct.francebleu.fr/live/fb1071-midfi.mp3 -t u16 -r 15000 -c 1 $tmp/francebleu.raw trim 0 $timing &
sox -t mp3 http://direct.francebleu.fr/live/fbbreizizel-midfi.mp3 -t u16 -r 15000 -c 1 - trim 0 $timing | python2 $MYGIST/radio/radiosend.py 10720000 10730000 16 > $tmp/fbbzh.radio &
sox -t mp3 http://direct.francebleu.fr/live/fbhautenormandie-midfi.mp3 -t u16 -r 15000 -c 1 - trim 0 $timing | python2 $MYGIST/radio/radiosend.py 10730000 10740000 16 > $tmp/fbhaut.radio &
sox -t mp3 http://direct.francebleu.fr/live/fbbassenormandie-midfi.mp3 -t u16 -r 15000 -c 1 - trim 0 $timing | python2 $MYGIST/radio/radiosend.py 10740000 10750000 16 > $tmp/fbbass.radio &
sox -t mp3 http://direct.francebleu.fr/live/fbtoulouse-midfi.mp3 -t u16 -r 15000 -c 1 - trim 0 $timing | python2 $MYGIST/radio/radiosend.py 10750000 10760000 16 > $tmp/fbtoulouse.radio &
sox -t mp3 http://direct.francebleu.fr/live/fbnord-midfi.mp3 -t u16 -r 15000 -c 1 - trim 0 $timing | python2 $MYGIST/radio/radiosend.py 10760000 10770000 16 > $tmp/fbnord.radio &
sox -t mp3 http://live02.rfi.fr/rfimonde-96k.mp3 -t u16 -r 15000 -c 1 $tmp/rfi.raw trim 0 $timing &
sox -t mp3 http://direct.franceinter.fr/live/franceinter-midfi.mp3 -t u16 -r 15000 -c 1 - trim 0 $timing | python2 $MYGIST/radio/radiosend.py 8760000 8770000 16 > $tmp/franceinter.radio &
sox -t mp3 http://generationfm.ice.infomaniak.ch/generationfm-high.mp3 -t u16 -r 15000 -c 1 - trim 0 $timing | python2 $MYGIST/radio/radiosend.py 8820000 8830000 16 > $tmp/generations.radio &
sox -t mp3 https://scdn.nrjaudio.fm/audio1/fr/30601/mp3_128.mp3 -t u16 -r 15000 -c 1 - trim 0 $timing | python2 $MYGIST/radio/radiosend.py 9040000 9050000 16 > $tmp/nostalgie.radio &
sox -t mp3 http://stream1.evasionfm.com/Chante_France -t u16 -r 15000 -c 1 - trim 0 $timing | python2 $MYGIST/radio/radiosend.py 9090000 9100000 16 > $tmp/chantefrance.radio &
sox -t mp3 http://icecast.skyrock.net/s/natio_mp3_128k -t u16 -r 15000 -c 1 - trim 0 $timing | python2 $MYGIST/radio/radiosend.py 9600000 9610000 16 > $tmp/skyrock.radio &
sox -t mp3 https://scdn.nrjaudio.fm/audio1/fr/30401/mp3_128.mp3 -t u16 -r 15000 -c 1 - trim 0 $timing | python2 $MYGIST/radio/radiosend.py 9740000 9750000 16 > $tmp/rireetchansons.radio &
sox -t mp3 https://windu.radionotredame.net/RadioNotreDame-Fm.mp3 -t u16 -r 15000 -c 1 - trim 0 $timing | python2 $MYGIST/radio/radiosend.py 10070000 10080000 16 > $tmp/radionotredame.radio &
sox -t mp3 https://scdn.nrjaudio.fm/audio1/fr/30001/mp3_128.mp3 -t u16 -r 15000 -c 1 - trim 0 $timing | python2 $MYGIST/radio/radiosend.py 10030000 10040000 16 > $tmp/nrj.radio &
sox -t mp3 https://start-sud.ice.infomaniak.ch/start-sud-high.mp3 -t u16 -r 15000 -c 1 - trim 0 $timing | python2 $MYGIST/radio/radiosend.py 9990000 10000000 16 > $tmp/sudradio.radio &
sox -t mp3 http://streaming.radio.funradio.fr/fun-1-44-128 -t u16 -r 15000 -c 1 - trim 0 $timing | python2 $MYGIST/radio/radiosend.py 10190000 10200000 16 > $tmp/fun.radio &
sox -t mp3 http://stream.virginradio.fr/virgin.mp3 -t u16 -r 15000 -c 1 - trim 0 $timing | python2 $MYGIST/radio/radiosend.py 10350000 10360000 16 > $tmp/europe2.radio &
sox -t mp3 http://streaming.radio.rtl.fr/rtl-1-44-128 -t u16 -r 15000 -c 1 - trim 0 $timing | python2 $MYGIST/radio/radiosend.py 10430000 10440000 16 > $tmp/rtl.radio &
sox -t mp3 http://ais-live.cloud-services.paris:8000/europe1.mp3 -t u16 -r 15000 -c 1 - trim 0 $timing | python2 $MYGIST/radio/radiosend.py 10470000 10480000 16 > $tmp/europe1.radio &
sox -t mp3 https://start-voltage.ice.infomaniak.ch/start-voltage-high.mp3 -t u16 -r 15000 -c 1 - trim 0 $timing | python2 $MYGIST/radio/radiosend.py 9690000 9700000 16 > $tmp/voltage.radio &
sox -t mp3 http://radio-contact.ice.infomaniak.ch/radio-contact-high.mp3 -t u16 -r 15000 -c 1 - trim 0 $timing | python2 $MYGIST/radio/radiosend.py 9070000 9080000 16 > $tmp/contact.radio &
sox -t mp3 https://stream.rfm.fr/rfm.mp3 -t u16 -r 15000 -c 1 - trim 0 $timing | python2 $MYGIST/radio/radiosend.py 10390000 10400000 16 > $tmp/rfm.radio &
sox -t mp3 https://scdn.nrjaudio.fm/audio1/fr/30201/mp3_128.mp3 -t u16 -r 15000 -c 1 - trim 0 $timing | python2 $MYGIST/radio/radiosend.py 9130000 9140000 16 > $tmp/cheriefm.radio &
sox -t mp3 http://mfm.ice.infomaniak.ch/mfm-128.mp3 -t u16 -r 15000 -c 1 - trim 0 $timing | python2 $MYGIST/radio/radiosend.py 10270000 10280000 16 > $tmp/mfm.radio &
sox -t mp3 http://radioclassique.ice.infomaniak.ch/radioclassique-high.mp3 -t u16 -r 15000 -c 1 - trim 0 $timing | python2 $MYGIST/radio/radiosend.py 10110000 10120000 16 > $tmp/classique.radio &
sox -t mp3 http://str0.creacast.com/radio_vinci_autoroutes_1 -t u16 -r 15000 -c 1 - trim 0 $timing | python2 $MYGIST/radio/radiosend.py 10770000 10780000 16 > $tmp/trafic1.radio &
sox -t mp3 http://str0.creacast.com/radio_vinci_autoroutes_2 -t u16 -r 15000 -c 1 - trim 0 $timing | python2 $MYGIST/radio/radiosend.py 10780000 10790000 16 > $tmp/trafic2.radio &
sox -t mp3 http://str0.creacast.com/radio_vinci_autoroutes_3 -t u16 -r 15000 -c 1 - trim 0 $timing | python2 $MYGIST/radio/radiosend.py 10790000 10800000 16 > $tmp/trafic3.radio &
sox -t mp3 http://str0.creacast.com/radio_vinci_autoroutes_4 -t u16 -r 15000 -c 1 - trim 0 $timing | python2 $MYGIST/radio/radiosend.py 10800000 10810000 16 > $tmp/trafic4.radio &
sox -t mp3 http://str0.creacast.com/radio_vinci_autoroutes_5 -t u16 -r 15000 -c 1 - trim 0 $timing | python2 $MYGIST/radio/radiosend.py 10810000 10820000 16 > $tmp/trafic5.radio &
sox -t mp3 http://str0.creacast.com/radio_vinci_autoroutes_6 -t u16 -r 15000 -c 1 - trim 0 $timing | python2 $MYGIST/radio/radiosend.py 10820000 10830000 16 > $tmp/trafic6.radio &
sox -t mp3 http://str0.creacast.com/radio_vinci_autoroutes_7 -t u16 -r 15000 -c 1 - trim 0 $timing | python2 $MYGIST/radio/radiosend.py 10830000 10840000 16 > $tmp/trafic7.radio &
sox -t mp3 https://ice.creacast.com/radio_vinci_autoroutes_a355 -t u16 -r 15000 -c 1 - trim 0 $timing | python2 $MYGIST/radio/radiosend.py 10850000 10860000 16 > $tmp/trafica355.radio &
sox -t mp3 http://direct.franceinfo.fr/live/franceinfo-midfi.mp3 -t u16 -r 15000 -c 1 - trim 0 $timing | python2 $MYGIST/radio/radiosend.py 10550000 10560000 16 > $tmp/franceinfo.radio &
sox -t mp3 https://audio.bfmtv.com/bfmradio_128.mp3 -t u16 -r 15000 -c 1 - trim 0 $timing | python2 $MYGIST/radio/radiosend.py 10860000 10870000 16 > $tmp/bfmradio.radio &
sox -t mp3 http://icecast.radiofrance.fr/fbalsace-midfi.mp3 -t u16 -r 15000 -c 1 - trim 0 $timing | python2 $MYGIST/radio/radiosend.py 10870000 10880000 16 > $tmp/fbalsace.radio &
sox -t mp3 http://14993.live.streamtheworld.com/NV1.mp3 -t u16 -r 15000 -c 1 - trim 0 $timing | python2 $MYGIST/radio/radiosend.py 10900000 10910000 16 > $tmp/nvone.radio &
sleep $timing
sox -t u16 -r 15000 -c 1 $tmp/francebleu.raw -r 15000 -t ul -c 1 $tmp/francebleu_ul.raw
python2 $MYGIST/radio/radiosend.py 10710000 10720000 16 < $tmp/francebleu.raw > $tmp/francebleu.radio
python2 $MYGIST/radio/radiosend.py 86400 86500 8 < $tmp/francebleu_ul.raw > $tmp/francebleu_ul.radio
sox -t u16 -r 15000 -c 1 $tmp/rfi.raw -r 15000 -t ul -c 1 $tmp/rfi_ul.raw
python2 $MYGIST/radio/radiosend.py 8900000 8910000 16 < $tmp/rfi.raw > $tmp/rfi.radio
python2 $MYGIST/radio/radiosend.py 73800 73900 8 < $tmp/rfi_ul.raw > $tmp/rfi_ul.radio
python2 $MYGIST/radio/radiomerge.py $tmp/*.radio
rm -r $tmp
