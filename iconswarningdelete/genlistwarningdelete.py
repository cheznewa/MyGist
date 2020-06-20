import sys
for o in sys.stdin:
 url = o.split(";")[0]
 name = o.split(";")[1]
 using = o.split(";")[2]
 level = int(o.split(";")[3])
 if level == 1:
  levelname = "NoProblem"
 if level == 2:
  levelname = "Kissing"
 if level == 3:
  levelname = "Trouble"
 if level == 4:
  levelname = "PleaseDoNot"
 sys.stdout.write("<img width='32' height='32' src='Delete%s.svg'/>" %(levelname))
 sys.stdout.write("<a href='%s'>%s</a> => %s<br/>" %(url,name,using))
