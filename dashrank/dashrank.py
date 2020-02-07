import time
import datetime
import sys
from youtube_dl import YoutubeDL
video = str(sys.argv[1])
ydl = YoutubeDL()
info_dict = ydl.extract_info(video,download=False)
like = int(info_dict.get("like_count",None))+1
view = int(info_dict.get("view_count",None))+1
date = info_dict.get("upload_date",None)
dateh = int(time.mktime(datetime.datetime.strptime(date,"%Y%m%d").timetuple())/86400)
todayh = int(time.time()/86400)
time = todayh-dateh
edgerank = view*like*(10.0/time)
print("%.2f" % edgerank)
