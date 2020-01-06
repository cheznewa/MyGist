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
</style>
" > "$title.html"
printf "<div class='title'>$title</div>" >> "$title.html"
sed 's/$/<br>/' < "$title.description" >> "$title.html"