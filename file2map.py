import sys
def coordinate2position(c,b):
 xb = format(c[0],"0"+str(b)+"b")
 yb = format(c[1],"0"+str(b)+"b")
 g = ""
 for n in range(b):
  g = g + yb[n] + xb[n]
 return int(g,2)

if sys.argv[2] == "rgb":
 o = sys.stdin.read(pow(2,int(sys.argv[1])*2)*3)
if sys.argv[2] == "g16":
 o = sys.stdin.read(pow(2,int(sys.argv[1])*2)*2)
else:
 o = sys.stdin.read(pow(2,int(sys.argv[1])*2))
a = format(pow(2,int(sys.argv[1])),"08x")
b = chr(int(a[0:2],16)) + chr(int(a[2:4],16)) + chr(int(a[4:6],16)) + chr(int(a[6:8],16))
col = ["000000","560000","640000","750000","870000","9b0000","b00000","c60000","dd0000","f50000","ff0f0f","ff2828","ff4343","ff5e5e","ff7979","fe9595","4c1600","561900","641e00","752300","872800","9b2e00","b03400","c63b00","dd4200","f54900","ff570f","ff6928","ff7b43","ff8e5e","ffa179","feb595","4c3900","564000","644b00","755700","876500","9b7400","b08400","c69400","dda600","f5b800","ffc30f","ffc928","ffd043","ffd65e","ffdd79","fee495","4c4c00","565600","646400","757500","878700","9b9b00","b0b000","c6c600","dddd00","f5f500","ffff0f","ffff28","ffff43","ffff5e","ffff79","fffe95","324c00","395600","426400","4e7500","5a8700","679b00","75b000","84c600","93dd00","a3f500","afff0f","b7ff28","c0ff43","c9ff5e","d2ff79","dbfe95","1f4c00","235600","296400","307500","388700","409b00","49b000","52c600","5cdd00","66f500","73ff0f","82ff28","91ff43","a1ff5e","b1ff79","c1fe95","004c00","005600","006400","007500","008700","009b00","00b000","00c600","00dd00","00f500","0fff0f","28ff28","43ff43","5eff5e","79ff79","95fe95","004c19","00561c","006421","007527","00872d","009b33","00b03a","00c642","00dd49","00f551","0fff5f","28ff70","43ff81","5eff93","79ffa6","95feb8","004c4c","005656","006464","007575","008787","009b9b","00b0b0","00c6c6","00dddd","00f5f5","0ffffe","28fffe","43fffe","5efffe","79ffff","95fffe","00394c","004056","004b64","005775","006587","00749b","0084b0","0094c6","00a6dd","00b8f5","0fc3ff","28c9ff","43d0ff","5ed6ff","79ddff","95e4fe","00264c","002b56","003264","003a75","004387","004d9b","0058b0","0063c6","006edd","007af5","0f87ff","2893ff","43a1ff","5eaeff","79bcff","95cafe","00134c","001556","001964","001d75","002187","00269b","002cb0","0031c6","0037dd","003df5","0f4bff","285eff","4372ff","5e86ff","799aff","95b0fe","19004c","1c0056","210064","270075","2d0087","33009b","3a00b0","4200c6","4900dd","5100f5","5f0fff","7028ff","8143ff","935eff","a679ff","b895fe","33004c","390056","420064","4e0075","5a0087","67009b","7500b0","8400c6","9300dd","a300f5","af0fff","b728ff","c043ff","c95eff","d279ff","db95fe","4c004c","560056","640064","750075","870087","9b009b","b000b0","c600c6","dd00dd","f500f5","fe0fff","fe28ff","fe43ff","fe5eff","fe79ff","fe95fe","4c0032","560039","640042","75004e","87005a","9b0067","b00075","c60084","dd0093","f500a3","ff0faf","ff28b7","ff43c0","ff5ec9","ff79d2","ffffff"] # Copied From :::: https://github.com/FireyFly/pixd/blob/master/pixd.c#L20
sys.stdout.write("farbfeld%s%s" %(b,b))
for n in range(pow(pow(2,int(sys.argv[1])),2)):
 p = coordinate2position([n%pow(2,int(sys.argv[1])),n/pow(2,int(sys.argv[1]))],int(sys.argv[1]))
 if sys.argv[2] == "bnw":
  r = o[p]
  rr = r
  gg = r
  bb = r
  g = r
  b = r
 elif sys.argv[2] == "col":
  c = col[ord(o[p])]
  r = chr(int(c[0:2],16))
  rr = r
  g = chr(int(c[2:4],16))
  gg = g
  b = chr(int(c[4:6],16))
  bb = b
 elif sys.argv[2] == "rgb":
  r = o[3*p]
  rr = r
  g = o[3*p+1]
  gg = g
  b = o[3*p+2]
  bb = b
 elif sys.argv[2] == "g16":
  r = o[2*p+1]
  rr = o[2*p]
  g = r
  gg = rr
  b = r
  bb = rr
 elif sys.argv[2] == "deg":
  aa = sys.argv[3]
  ar = int(aa[0:2],16)
  ag = int(aa[2:4],16)
  ab = int(aa[4:6],16)
  zz = sys.argv[4]
  zr = int(zz[0:2],16)
  zg = int(zz[2:4],16)
  zb = int(zz[4:6],16)
  ff = ord(o[p])
  rr = chr(int((ar*((255-ff)/255.0))+(zr*(ff/255.0))))
  r = rr
  gg = chr(int((ag*((255-ff)/255.0))+(zg*(ff/255.0))))
  g = gg
  bb = chr(int((ab*((255-ff)/255.0))+(zb*(ff/255.0))))
  b = bb
 sys.stdout.write("%s%s%s%s%s%s\xff\xff" %(r,rr,g,gg,b,bb))