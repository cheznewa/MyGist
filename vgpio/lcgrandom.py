import sys
import time
a=0
while True:
 f=open("/sys/kernel/vgpio/gpio"+sys.argv[1]+"/value","w")
 a = (int(sys.argv[2])*a+int(sys.argv[3])) % int(sys.argv[4])
 f.write(str(a%2))
 f.close()
 time.sleep(0.1)