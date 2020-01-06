title=$(echo "${1%%.*}")
printf "<style>
@font-face
{
font-family:'EuropeanTeletext';
src:url('file:///usr/local/share/fonts/EuropeanTeletext.ttf');
}
body
{
margin:0px 0px 0px 0px;
color:white;
background-color:black;
font-family:'EuropeanTeletext';
font-size:16px;
}
.title
{
background-color:white;
color:black;
}
.view
{
color:cyan;
}
.like
{
color:green;
}
.dislike
{
color:red;
}
</style>
" > "$title.html"
printf "<div class='title'>" >> "$title.html"
jt [ uploader % ] < "$title.info.json" >> "$title.html"
printf " -:- $title</div>" >> "$title.html"
sed 's/$/<br>/' < "$title.description" >> "$title.html"
printf "<br><span class='view'>" >> "$title.html"
jt [ view_count % ] < "$title.info.json" >> "$title.html"
printf "</span> - <span class='like'>" >> "$title.html"
jt [ like_count % ] < "$title.info.json" >> "$title.html"
printf "</span> - <span class='dislike'>" >> "$title.html"
jt [ dislike_count % ] < "$title.info.json" >> "$title.html"
printf "</span>" >> "$title.html"