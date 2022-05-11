import sys
a = int(sys.stdin.read())
wordbase = [
"Trual",
"Electe",
"Double Electe",
"Triple Electe",
"Electro",
"Double Electro",
"Triple Electro",
"Electra",
"Double Electra",
"Triple Electra",
"Dast Electe",
"Dast Double Electe",
"Dast Triple Electe",
"Dast Electro",
"Dast Double Electro",
"Dast Triple Electro",
"Dast Electra",
"Dast Double Electra",
"Dast Triple Electra",
"Electel",
"Electrol",
"Electral"
]
letterbase = [
"U",
"E",
"DE",
"TE",
"O",
"DO",
"TO",
"A",
"DA",
"TA",
"SE",
"SDE",
"STE",
"SO",
"SDO",
"STO",
"SA",
"SDA",
"STA",
"EL",
"OL",
"AL"
]
out = ""

if sys.argv[1] == "letter":
 while a:
  a,int = divmod(a,22)
  out = letterbase[int] + out

if sys.argv[1] == "word":
 while a:
  a,int = divmod(a,22)
  out = wordbase[int] + " " + out

sys.stdout.write(out)
sys.stdout.write("\n")