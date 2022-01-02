# radiosocket.py numberid numstram rate < mainstream.radio
# nc -U /sock/radioN
import socket
import sys
import time
sock = socket.socket(socket.AF_UNIX,socket.SOCK_STREAM)
sock.bind("/sock/radio%s" %(int(sys.argv[1])))
sock.listen(1)
s,a = sock.accept()
while True:
 audio = sys.stdin.read(int(sys.argv[3])*4*int(sys.argv[2]))
 try:
  s.send(audio)
 except:
  s,a = sock.accept()
 time.sleep(1)