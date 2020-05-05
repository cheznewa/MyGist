n=4
m=$1
for g in $(seq 1 64)
do
n=$(python $MYGIST/knutharrow/knutharrow.py 3 $n 3 $m)
printf "G${g} ::: $n\n"
done
printf "\nGraham Number :::: $n\n"