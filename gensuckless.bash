if test -z $ROOT
then
printf "Dont Forget 'ROOT' Variable As Full Path.\n"
exit 1
fi
tmp=$(mktemp -d)
git clone https://github.com/ibara/oksh $tmp/oksh
cd $tmp/oksh
./configure --prefix=$ROOT/usr &&
make LDFLAGS="-static" &&
make install &&
cd ..
git clone git://git.suckless.org/sbase $tmp/sbase
cd $tmp/sbase
make LDFLAGS="-static" &&
make install PREFIX=$ROOT/usr &&
cd ..
mkdir -p $ROOT/root
rm -fr $tmp
printf "Now, You Can Do :::: sudo chroot $ROOT oksh\n"
