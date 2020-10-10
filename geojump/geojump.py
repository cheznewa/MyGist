import sys
fs = open(sys.argv[1],"r")
ur = open("/dev/urandom","rb")
code = fs.read()
la = len(code)
jumpprob = float(sys.argv[2])
for c in range(la):
 jump = ord(ur.read(1))/256.0
 if code[c] == "+":
  if jump < jumpprob:
   print("perdu a " + str((100*c)/la))
   exit(1)
 if code[c] == "-":
  if jump > jumpprob:
   print("perdu a " + str((100*c)/la))
   exit(1)
 if code[c] == ".":
  print("rien ce passe")
  
print("gagner !!!")
exit(0)