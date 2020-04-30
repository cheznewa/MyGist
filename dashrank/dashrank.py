import time
import datetime
import sys
from youtube_dl import YoutubeDL
video = str(sys.argv[1])
ydl = YoutubeDL()
info_dict = ydl.extract_info(video,download=False)
timing = int(info_dict.get("duration",None))
view = int(info_dict.get("view_count",None))
like = int(info_dict.get("like_count",None))
date = info_dict.get("upload_date",None)
dateh = int(time.mktime(datetime.datetime.strptime(date,"%Y%m%d").timetuple())/86400)
todayh = int(time.time()/86400)
dating = todayh-dateh
dash = view+like
edgerank = (dash*timing)/dating
print("%.2f" % edgerank)
