import sys
import time
import os
a=True
b=False
while True:
 f=open("/sys/kernel/vgpio/gpio"+sys.argv[1]+"/value","r")
 p=bool(int(f.read(1)))
 if (p==False)&a:
  os.system("/usr/bin/gsettings set org.gnome.desktop.interface gtk-theme Adwaita-dark")
  a=False
  b=True
 if (p==True)&b:
  os.system("/usr/bin/gsettings set org.gnome.desktop.interface gtk-theme Adwaita")
  a=True
  b=False
 time.sleep(0.1)
