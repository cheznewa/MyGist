printf "Applications Installed On System :::\n"
for apps in /usr/share/applications/*.desktop
do
catch=$(grep ^Name= $apps)
name=$(cut -f 2 -d = <<< $catch)
printf "$name\n"
done
if test -d /usr/local/share/applications
then
printf "\nApplications Installed On User :::\n"
for apps in /usr/local/share/applications/*.desktop
do
catch=$(grep ^Name= $apps)
name=$(cut -f 2 -d = <<< $catch)
printf "$name\n"
done
fi
