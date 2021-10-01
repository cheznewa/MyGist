<?php
// Je Vais Faire De La Magie Avec ::::::::::::::: https://github.com/jweslley/localtld
// Ou Fois Installer, Faite La Commande :::::: LOCALTLD=chezsick-red,chezsick-green,chezsick-yellow,chezsick-blue,chezsick-orange,chezsick-purple,chezsick-cyan,chezsick-magenta,chezsick-lime,chezsick-pink,chezsick-teal,chezsick-lavender,chezsick-brown,chezsick-beige,chezsick-maroon,chezsick-mint,chezsick-olive,chezsick-apricot,chezsick-navy,chezsick-grey,chezsick-white,chezsick-black _browser_
// Pour Commencé :::::::::::::::: [linksourmaster.chezsick-black](http://linksourmaster.chezsick-black)
// Et Accrochez-Vous !
// Mettez Ce Fichier Sur Votre Serveur Local Et Rennomé En index.php
// Si Ca Ne Marche Pas, Vous Devrait Vous-Même Télécharger Les Fichier Qui Manque à L'apelle.
// Nouveau :::: Désormais Les Sites Sont Labelisé D'une Couleur Les Noir Sont A Moi, Les D'autre En Dépend, Quand Aux Rouge, Pas Touche !
$nonhtml = false;
$freedomaines = ["newanotremaitre.chezsick-black","timeanddatebletou.chezsick-black","logicemu.chezsick-green","jslinux.chezsick-cyan","randomlike.chezsick-black","colormodem.chezsick-white","dafont.chezsick-purple","pagerankcalc.chezsick-magenta","pdf2htmlex.chezsick-teal","lhvtools.chezsick-green","cestpassorcier.chezsick-olive","dexsilicium.chezsick-maroon","logicemu2luxar.chezsick-brown","titeuf.chezsick-beige","codelyoko.chezsick-green","kidpaddle.chezsick-yellow","yakari.chezsick-red","emonote.chezsick-black","garfield.chezsick-blue","problemepointageamerindienne.chezsick-grey","visualarm1.chezsick-green","infernalcounter.chezsick-teal","internetmerespectpas.chezsick-navy","openfoodfacts.chezsick-mint","javascriptreplay.chezsick-lime","powwows.chezsick-red","emoticon-composer.chezsick-mint","ptmeasureonemilliondecimal.chezsick-black","halflife.chezsick-blue","kara.chezsick-green"];
if ($_SERVER["HTTP_HOST"] == "linksourmaster.chezsick-black")
{
echo "<title>ChezSick Links</title>";
echo "<h1>List Of Newa's Website Avaliable</h1>";
if (!(isset($_GET["dont"])))
$_GET["dont"] = 0;
foreach ($freedomaines as $domaine)
{
$dom = explode(".",$domaine);
if (($dom[1] != "chezsick-red") || boolval($_GET["dont"]))
echo "<a href=\"http://$domaine\">$domaine</a><br/>";
}
if (!($_GET["dont"]))
echo "<br/><a href='?dont=1'>Just Don't Click Please, NO!!!</a>";
}
elseif ($_SERVER["HTTP_HOST"] == $freedomaines[0])
{
echo "<style>body{background-color:#00288c;color:white;}a{color:#feec00;}</style>";
$themevideo = "newanotremaitre";
$url        = "https://www.youtube.com/channel/UCZ6aZWdqc2toGWP1xqRoSaw/videos";
if (isset($_GET["v"]))
{
echo "<title>Sick Vidéos :::: ".basename($_GET["v"],".mp4")."</title>";
echo "<h1>".basename($_GET["v"],".mp4")."</h1>";
echo "<video controls><source src=\"".$themevideo."/".$_GET['v']."\"></video><br/>";
echo file_get_contents($themevideo."/".basename($_GET['v'],".mp4").".description");
}
else
{
$vids = scandir($themevideo);
if ($vids == null)
{
mkdir($themevideo);
exec("youtube-dl -i -f 'mp4[height <= 360]' -o \"$themevideo/%(title)s.%(ext)s\" --write-thumbnail --write-description $url");
exec("mogrify -format webp $themevideo/*.jpg");
}
echo "<title>Newa Notre Maitre - Site Officiel</title><h1>Bonjour Tout Le Monde, C'est Newa Notre Maitre !</h1>Je Suis Un Grand Oiseau, Et Je Joue De La Flute Des Andes, Passionné De Culture Amerindienne (En Interne), Je Suis Sur L'ordinateur Depuis Pas Mal De Temps.";
echo "<h1>Mes Vidéos</h1>";
foreach ($vids as $video)
{
if (pathinfo($video,PATHINFO_EXTENSION) == "mp4")
{
echo "<img width='100' src=\"".$themevideo."/".basename($video,".mp4").".webp\"><a href=\"?v=$video\">".basename($video,".mp4")."</a><br/>";
}
}
}
}
elseif ($_SERVER["HTTP_HOST"] == $freedomaines[1])
{
echo "<title>Date Et Heure BLE TOU</title>";
function getdatebt($timestamps)
{
$jour = ["Lundi","Mardi","Mercredi","Jeudi","Vendredi","Samdi","Dimance"];
$sem = $jour;
return intval($timestamps / 49) + 1 . " Foitierre " .$sem[intval(($timestamps % 49) / 7)] .",". $jour[$timestamps % 7];
}
function gettimeday($time)
{
$r = intval($time / 2);
$r .= boolval($time % 2) ? ":" : "";
return $r;
}
echo "La Date Et L'heure BLE TOU ? Il Est Exactement :::::::::::::: ";
echo getdatebt(intval((time() - (989193600 + 18000)) / 86400))." ".gettimeday((time() - 18000) % 86400)."\n";
}
elseif ($_SERVER["HTTP_HOST"] == $freedomaines[2])
{
echo "<title>LogicEmu - Online Logic Simulator</title>";
echo "<body><noscript>Please Enable Javascript!</noscript></body>";
echo "<script src=\"editor.js\"></script>";
echo "<script src=\"logicemu.js\"></script>";
echo "<script src=\"main.js\"></script>";
echo "<script src=\"circuits_help.js\"></script>";
echo "<script src=\"circuits_articles.js\"></script>";
echo "<script src=\"circuits_main.js\"></script>";
echo "<script src=\"footer.js\"></script>";
}
elseif ($_SERVER["HTTP_HOST"] == $freedomaines[3])
{
echo "<title>JSLinux</title>";
echo "<style>.term{font-family:monospace;color:white;background-color:black;}.termReverse{color:black;background-color:lime;}</style>";
echo "<body onload=\"start()\">";
echo "<script src=\"term.js\"></script>";
echo "<script src=\"jslinux.js\"></script>";
echo "<script src=\"utils.js\"></script>";
echo "<script src=\"cpux86-ta.js\"></script>";
echo "JSLinux Par Fabrice B.";
}
elseif ($_SERVER["HTTP_HOST"] == $freedomaines[4])
{
require("config.php");
echo "<title>RandomLike</title>";
echo "<h1><img src='logo.png'/></h1>";
echo "Vous Avez Le Choix De Mes Services ::::: <br/><a href='number.php?min=0&max=100'>Nombre Aléatoire</a><br/><a href='color.php'>Couleur Aléatoire</a><br/><a href='password.php?len=16'>Mot De Passe Aléatoire</a><br/><a href='race.php?pist=6&len=10'>Course Aléatoire</a><br/><a href='loto.php?tirage=5&nbball=20'>Tirage Du Loto</a><br/><a href='galton.php'>La Planche De Galton</a><br/><a href='date.php?future=60'>Un Rendez-Vous Aléatoire</a><br/><a href='text.php?nb=100&lang=fr'>Générateur De Texte Aleatoire</a><br/><a href='naf.php?len=50&plus=0'>Générateur De Partition Pour Flute Amerindienne</a><br/><a href='para.php'>Anti-Probabilité Aléatoire</a><br/><a href='decay.php?nb=100'>Générateur De Demi-Vie</a><br/><a href='carddice.php?card=20&dice=2&joker=0'>Carte Et Dé Aléatoire</a><br/><a href='asciicast.php'>Regarder Une Vidéo Asciinema Aléatoire</a><br/><a href='youtube.php'>Regarder Une Vidéo YouTube Aléatoire</a><br/>";
echo "<br/><a href='syster.php?tp=1&demi=0&frame=1000'>Paramettre D'encodage Nagravision Syster Pour CryptImage</a><br/><a href='videocrypt.php?frame=1000&begin=40&end=215'>Paramettre D'encodage VideoCrypt Pour CryptImage</a><br/><a href='weather.php?frame=1000&cold_hot=0&cloud_sun=0&cloud_rain=0&cloud_snow=0&cloud_storm=0&cloud_fog=0&wind=0&min=-1&max=1'>Générateur De Paramettre Météo</a><br/><a href='graph.php?nbedge=500&maxnode=800'>Généreteur De Graph Aléatoire</a><br/><a href='bytes.php?len=1000&binary=1'>Octets Aléatoire</a><br/>";
$count = file_get_contents($randomsourcecount);
echo "<br/>Le Site A Générer ::::::: " . $count . " Octet -:- Source Aléatoire :::::: ".$randomsourceinfo. " -:- <a href='stats.php'>Les Statistiques</a>";
}
elseif ($_SERVER["HTTP_HOST"] == $freedomaines[5])
{
echo "<title>Color Modem In My World</title>";
echo '<h1>Color Modem In My World At Vilande</h1><form enctype="multipart/form-data" action="proc.php" method="post">Please Select Video To Process ::<input type="file" name="userfile"/><br/>Select Standard From Country In My World :: <select name="country" id="country"><optgroup label="Normal System"><option value="bt">BLE TOU</option><option value="ph">Phélÿn</option><option value="eu">Eurack</option></optgroup><optgroup label="Andean System"><option value="mo">Moênne</option><option value="in">Indie</option><option value="so">Solainie</option><option value="mv">Movenie</option><option value="js">Joséro</option><option value="ln">Luana</option></optgroup><optgroup label="VHS Zone"><option value="ns">Normal System</option><option value="as">Andean System</option></optgroup></select><br/>Select Mode For Process :: <select name="mode" id="mode"><option value="modem">Modulate And Demodulate</option><option value="mod">Modulate Only</option><option value="demod">Demodulate Only</option><option value="multi">Multiplex (Modulate In Second, And Demodulate In First)</option></select><br/><input type="submit" value="Process Now!"></br></form>';
}
elseif ($_SERVER["HTTP_HOST"] == $freedomaines[6])
{
if (!(file_exists("dafont.com_categories_2010-05-19")))
{
exec("curl -OL https://archive.org/download/1.5_million_font_files_collection/dafont.com_categories_2010-05-19.zip");
exec("unzip 'dafont.com_categories_2010-05-19'");
}
if (isset($_GET['cat']))
{
if (isset($_GET['font']))
{
header("Content-Type: image/png");
$id = uniqid();
exec("convert \"dafont.com_categories_2010-05-19/".$_GET['cat']."/".$_GET['font']."\" /tmp/$id.png");
readfile("/tmp/$id.png");
}
else
{
$font = scandir("dafont.com_categories_2010-05-19/".$_GET['cat']);
foreach ($font as $i)
{
if (pathinfo($i,PATHINFO_EXTENSION) == "ttf")
echo "<a href=\"?cat=".$_GET['cat']."&font=$i\">$i</a><br/>";
}
}
}
else
{
$cat = scandir('dafont.com_categories_2010-05-19');
foreach ($cat as $i)
echo "<a href=\"?cat=$i\">$i</a><br/>";
}
}
elseif ($_SERVER["HTTP_HOST"] == $freedomaines[7])
{
echo "<title>PageRank Calculator</title>";
echo "<h1>PageRank Calculator From Wikipedia</h1><form action='.' method='get'>";
echo "Please Type ID Here (Get Name Wiki From Wikidata, Type \"Q\" Begin) ::::: <input name='id' id='id'></input></br>";
if (isset($_GET["id"]))
{
$content = file_get_contents("enwiki.links.rank"); // https://github.com/athalhammer/danker ; And Calulate :::::: https://archive.org/details/enwiki-20150901
$exploded = explode("\n",$content);
unset($content);
foreach ($exploded as $array)
{
$array = explode("\t",$array);
if ($array[0] == $_GET["id"])
{
echo "Result PageRank :::: ";
echo $array[1];
break;
}
}
}
}
elseif ($_SERVER["HTTP_HOST"] == $freedomaines[8])
{
if (isset($_FILES["pdffile"]))
{
set_time_limit(0);
$pdf = uniqid();
if (!move_uploaded_file($_FILES["pdffile"]["tmp_name"],"/tmp/".$pdf.".pdf"))
{
echo "Oops!";
}
exec("/usr/local/bin/pdf2htmlEX --zoom 1.618 --dest-dir /tmp/ ///tmp/".$pdf.".pdf ".$pdf.".html");
header("Content-Type: text/html");
echo "<title>pdf2htmlEX</title>";
$nonhtml = true;
readfile("/tmp/".$pdf.".html");
}
else
{
echo "<title>pdf2htmlEX</title>";
echo "<form enctype='multipart/form-data' action='.' method='post'>Please Select PDF :: <input type='file' name='pdffile' accept='application/pdf'/><br/><input type='submit' value='Submit'/><br/></from>";
}
}
elseif ($_SERVER["HTTP_HOST"] == $freedomaines[9])
{
echo "<title>Les Outils En Ligne Du Hollandais Volant</title>";
echo bzdecompress(base64_decode("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")); // Copied Just The List (Because Too Loong) ::::::::::::::: https://github.com/timovn/MyWebTools/blob/master/index.php
}
elseif ($_SERVER["HTTP_HOST"] == $freedomaines[10])
{
$themevideo = "cestpassorcier";
$themetitle = "C'est Pas Sorcier";
$url        = "https://www.youtube.com/playlist?list=PLh-qVJTuss13DTDtjpx40TASjjXkMdJNI";
echo "<title>$themetitle</title>";
echo "<h1>$themetitle</h1>";
if (isset($_GET["v"]))
{
echo "<video controls><source src=\"".$themevideo."/".$_GET['v']."\"></video><br/>";
echo file_get_contents($themevideo."/".basename($_GET['v'],".mp4").".description");
}
else
{
$vids = scandir($themevideo);
if ($vids == null)
{
mkdir($themevideo);
exec("youtube-dl -i -f 'mp4[height <= 360]' -o \"$themevideo/%(title)s.%(ext)s\" --write-thumbnail --write-description $url");
exec("mogrify -format webp $themevideo/*.jpg");
}
foreach ($vids as $video)
{
if (pathinfo($video,PATHINFO_EXTENSION) == "mp4")
{
echo "<img width='100' src=\"".$themevideo."/".basename($video,".mp4").".webp\"><a href=\"?v=$video\">".basename($video,".mp4")."</a><br/>";
}
}
}
}
elseif ($_SERVER["HTTP_HOST"] == $freedomaines[11])
{
$themevideo = "dexsilicium";
$themetitle = "Deus Ex Silicium";
$url        = "https://www.youtube.com/channel/UCH6ppHEvV3_WIXEwmhv9HEg/videos";
echo "<title>$themetitle</title>";
echo "<h1>$themetitle</h1>";
if (isset($_GET["v"]))
{
echo "<video controls><source src=\"".$themevideo."/".$_GET['v']."\"></video><br/>";
echo file_get_contents($themevideo."/".basename($_GET['v'],".mp4").".description");
}
else
{
$vids = scandir($themevideo);
if ($vids == null)
{
mkdir($themevideo);
exec("youtube-dl -i -f 'mp4[height <= 360]' -o \"$themevideo/%(title)s.%(ext)s\" --write-thumbnail --write-description $url");
exec("mogrify -format webp $themevideo/*.jpg");
}
foreach ($vids as $video)
{
if (pathinfo($video,PATHINFO_EXTENSION) == "mp4")
{
echo "<img width='100' src=\"".$themevideo."/".basename($video,".mp4").".webp\"><a href=\"?v=$video\">".basename($video,".mp4")."</a><br/>";
}
}
}
}
elseif ($_SERVER["HTTP_HOST"] == $freedomaines[12])
{
if (!file_exists("LUXAR"))
{
mkdir("LUXAR");
exec("youtube-dl -o 'LUXAR/%(title)s.%(ext)s' https://soundcloud.com/stephane-marty-185716647/sets/luxar");
}
echo "<head><title>LogicEmu - Online Logic Simulator</title></head>";
echo "<body><noscript>Please Enable Javascript!</noscript>";
echo "<script src=\"logicemu.js\"></script>";
echo "<script src=\"main.js\"></script>";
echo "<script src=\"circuits_help.js\"></script>";
echo "<script src=\"circuits_articles.js\"></script>";
echo "<script src=\"circuits_main.js\"></script>";
echo "<script src=\"footer.js\"></script>";
echo "<script type='text/javascript'>var c = origtext.replace(/\\\"[^\\\"]*\\\"/g,'');var inup = ((c.split('^')).length-1) - ((c.split('m')).length-1);var indown = ((c.split('v')).length-1) - ((c.split('w')).length-1);var inleft = ((c.split('<')).length-1) - ((c.split('[')).length-1);var inright = ((c.split('>')).length-1) - ((c.split(']')).length-1);var pist = ((Math.floor(inleft/3)%2)*8)+((Math.floor(inup/3)%2)*4)+((Math.floor(inright/3)%2)*2)+(Math.floor(indown/3)%2);";
echo "var tracks = ['LUXAR/Birth.mp3','LUXAR/First steps.mp3','LUXAR/Curiosity.mp3','LUXAR/Process.mp3','LUXAR/Free will.mp3','LUXAR/Scar.mp3','LUXAR/Loneliness.mp3','LUXAR/Explorer.mp3','LUXAR/Chase.mp3','LUXAR/Revolution.mp3','LUXAR/Blooming.mp3','LUXAR/Torment.mp3','LUXAR/Awareness.mp3','LUXAR/Self-confidence.mp3','LUXAR/Ambition.mp3','LUXAR/Responsability.mp3'];";
echo "document.write(\"<audio autoplay hidden loop><source format='mp3' src='\"+tracks[pist]+\"'></audio>\");</script>";
echo "<script src=\"editor.js\"></script></body>";
}
elseif ($_SERVER["HTTP_HOST"] == $freedomaines[13])
{
$themevideo = "titeuf";
$themetitle = "Titeuf";
$url        = "https://www.youtube.com/channel/UCrCqUUNGJ_Wo0FBbho70SMg/videos";
echo "<title>$themetitle</title>";
echo "<h1>$themetitle</h1>";
if (isset($_GET["v"]))
{
echo "<video controls><source src=\"".$themevideo."/".$_GET['v']."\"></video><br/>";
echo file_get_contents($themevideo."/".basename($_GET['v'],".mp4").".description");
}
else
{
$vids = scandir($themevideo);
if ($vids == null)
{
mkdir($themevideo);
exec("youtube-dl -i -f 'mp4[height <= 360]' -o \"$themevideo/%(title)s.%(ext)s\" --write-thumbnail --write-description $url");
exec("mogrify -format webp $themevideo/*.jpg");
}
foreach ($vids as $video)
{
if (pathinfo($video,PATHINFO_EXTENSION) == "mp4")
{
echo "<img width='100' src=\"".$themevideo."/".basename($video,".mp4").".webp\"><a href=\"?v=$video\">".basename($video,".mp4")."</a><br/>";
}
}
}
}
elseif ($_SERVER["HTTP_HOST"] == $freedomaines[14])
{
$themevideo = "codelyoko";
$themetitle = "Code Lyoko";
$url        = "https://www.youtube.com/channel/UCQiZ4G8PHqUIji3c74jBiTA/videos";
echo "<title>$themetitle</title>";
echo "<h1>$themetitle</h1>";
if (isset($_GET["v"]))
{
echo "<video controls><source src=\"".$themevideo."/".$_GET['v']."\"></video><br/>";
echo file_get_contents($themevideo."/".basename($_GET['v'],".mp4").".description");
}
else
{
$vids = scandir($themevideo);
if ($vids == null)
{
mkdir($themevideo);
exec("youtube-dl -i -f 'mp4[height <= 360]' -o \"$themevideo/%(title)s.%(ext)s\" --write-thumbnail --write-description $url");
exec("mogrify -format webp $themevideo/*.jpg");
}
foreach ($vids as $video)
{
if (pathinfo($video,PATHINFO_EXTENSION) == "mp4")
{
echo "<img width='100' src=\"".$themevideo."/".basename($video,".mp4").".webp\"><a href=\"?v=$video\">".basename($video,".mp4")."</a><br/>";
}
}
}
}
elseif ($_SERVER["HTTP_HOST"] == $freedomaines[15])
{
$themevideo = "kidpaddle";
$themetitle = "Kid Paddle";
$url        = "https://www.youtube.com/channel/UCdb2F4KPdFlL3vRB1sulgWA";
echo "<title>$themetitle</title>";
echo "<h1>$themetitle</h1>";
if (isset($_GET["v"]))
{
echo "<video controls><source src=\"".$themevideo."/".$_GET['v']."\"></video><br/>";
echo file_get_contents($themevideo."/".basename($_GET['v'],".mp4").".description");
}
else
{
$vids = scandir($themevideo);
if ($vids == null)
{
mkdir($themevideo);
exec("youtube-dl -i -f 'mp4[height <= 360]' -o \"$themevideo/%(title)s.%(ext)s\" --write-thumbnail --write-description $url");
exec("mogrify -format webp $themevideo/*.jpg");
}
foreach ($vids as $video)
{
if (pathinfo($video,PATHINFO_EXTENSION) == "mp4")
{
echo "<img width='100' src=\"".$themevideo."/".basename($video,".mp4").".webp\"><a href=\"?v=$video\">".basename($video,".mp4")."</a><br/>";
}
}
}
}
elseif ($_SERVER["HTTP_HOST"] == $freedomaines[16])
{
$themevideo = "yakari";
$themetitle = "Yakari";
$url        = "https://www.youtube.com/channel/UC7kI7S2COLludBkwJsNJXKg/videos";
echo "<title>$themetitle</title>";
echo "<h1>$themetitle</h1>";
if (isset($_GET["v"]))
{
echo "<video controls><source src=\"".$themevideo."/".$_GET['v']."\"></video><br/>";
echo file_get_contents($themevideo."/".basename($_GET['v'],".mp4").".description");
}
else
{
$vids = scandir($themevideo);
if ($vids == null)
{
mkdir($themevideo);
exec("youtube-dl -i -f 'mp4[height <= 360]' -o \"$themevideo/%(title)s.%(ext)s\" --write-thumbnail --write-description $url");
exec("mogrify -format webp $themevideo/*.jpg");
}
foreach ($vids as $video)
{
if (pathinfo($video,PATHINFO_EXTENSION) == "mp4")
{
echo "<img width='100' src=\"".$themevideo."/".basename($video,".mp4").".webp\"><a href=\"?v=$video\">".basename($video,".mp4")."</a><br/>";
}
}
}
}
elseif ($_SERVER["HTTP_HOST"] == $freedomaines[17])
{
if (isset($_GET["emo"]))
{
if ((intval($_GET["emo"]) <= 50) and (intval($_GET["emo"]) >= -50))
{
$nota = intval($_GET["emo"])+188;
header("Content-Type: image/png");
$id = uniqid();
$img = exec("convert -size 256x256 xc:none -stroke black -strokewidth 2.5 -fill none -draw \"circle 128,128 128,253 circle 64,64 64,68 circle 192,64 192,68 bezier 64,188 128,$nota 192,188\" /tmp/$id.png");
$nonhtml = true;
readfile("/tmp/$id.png");
}
else
{
echo "Choisi Une Valeur Entre -50 Et 50";
}
}
echo "<title>EmoNote - Note Ce Que Tu Veut !</title><h1>Note Ce Que Tu Veut !</h1><form method='GET' action='.'>Négatif<input type='range' min='-50' max='50' name='emo' value='0'/>Positif<br/><input type='submit'/>";
}
elseif ($_SERVER["HTTP_HOST"] == $freedomaines[18])
{
if (isset($_GET["whatgame"]))
{
if (!(file_exists($_GET["whatgame"].".swf")))
exec("curl -OL https://web.archive.org/web/20050910110440oe_/http://www.garfield.com/fungames/games/".$_GET["whatgame"].".swf");
echo "<object><param name='movie' value='".$_GET["whatgame"].".swf'><param name='quality' value='high'><embed src='".$_GET["whatgame"]."'.swf' width='768' height='576' quality='high' pluginspage='http://www.macromedia.com/go/getflashplayer' type='application/x-shockwave-flash' menu='false' bgcolor='#003366'></embed></object>";
}
else
{
echo "<title>Garfiled Games And Fun From Thirtyth Foitierre</title><h1>Garfiled Games And Fun From Thirtyth Foitierre</h1><a href='?whatgame=lasagnafromheaven'>Lasagna From Heaven<br/><a href='?whatgame=dingleballgame'>Dingle Ball<br/><a href='?whatgame=coopcatch'>Coop Catch<br/><a href='?whatgame=sheepshot'>Sheep Shoot<br/><a href='?whatgame='beanme3'>Bean Me<br/><a href='?whatgame=amazinggarf'>The Amazing Garfield<br/>";
}
}
elseif ($_SERVER["HTTP_HOST"] == $freedomaines[19])
{
echo "Contrairement Aux Idée Reçu Ils Viennent Pas Des Etat-Unis Mais Majoritairement D'équateur, Pays Donc Mauvaise Oeuil Quand Il S'agit De Le Faire Sur Toute L'europe L'asie Et Surtout La Russie Que Leur Propre Zone.";
echo "<title>Pointages Amerindien - Imprévisible, Rare, Grave !</title>";
echo "<h1>Imprévisible</h1>Un Pointage En Général Est Une Personne Qui Joue De La Musique Dans La Rue Pour Gagner De L'argent, Bien Que C'est Pas Planifier Publiquement, C'est Pareil Pour Les Pointages Amerindien.";
echo "<h1>Rare</h1>Les Pointage Amerindien Sont Vraiment Pas Frequent Qu'un Pointage Classique Et Portant Ya Sur Une Des Platforme Vidéo Très Populaire Une Circulation Pas Possible De Ces Pointage, Une Chaine Peut Se Retrouvé Avec Une Seul Vidéo D'un Pointage Pour Ca Frequence Pas Possible.";
echo "<h1>Grave</h1>Les Pointage Amerindien, Sont Très Souvant Déconcertante Sur Ces Tenu Introuvable Sur Internet Pour Un Passionné, Est Ces Instrument Mais Un Peut Plus Facile A Retrouvé Sur Le Net, Ils Se Raproche Asser Souvant Du Pow-Wow Car Pour Cause Ya Une Tenu Avec Un Bustle Plus Frequent D'apparition Qu'une Coiffe, Mais Ce Qui Est Déconcertant Avec Leur Tenu C'est Les Déssins Avec Les Frange Longue.";
echo "<h2>Conclusion</h2>Les Pointages Amerindiens Peuvent Basculé Toute Une Journé Voir Toute Une Vie, Et Il Est Pas Possible De S'en Prévenir, Et Encore Moin De Les Eradiqué.";
}
elseif ($_SERVER["HTTP_HOST"] == $freedomaines[20])
{
echo bzdecompress(base64_decode("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")); // From https://github.com/glitchcore/arm1/blob/master/index.html Because Too Complex To Customize
}
elseif ($_SERVER["HTTP_HOST"] == $freedomaines[21])
{
echo "<title>The Infernal Counter !</title>";
echo bzdecompress(base64_decode("QlpoOTFBWSZTWey9qh8ABRVf5XAwc3///z9nzCA/99/6AQAggAgAEABgBlwfUUKoKrlqgAEHGTJoxDE0wEDAmmCMExNNNABhCJMmCaCNAbUAAAAAAAAAcZMmjEMTTAQMCaYIwTE000AGEEmpIk9JP1JkGI009TJ6IMhpppoDI00A00aHGTJoxDE0wEDAmmCMExNNNABhBEkSZAJiJ5KbZUjeVPRqafqZJ6R6mgDwKeo/VBs9qSGQkyMkVURQgskFQYCsIoRSQUBRGCQVRYAiqqT9yajDMhBEYiyLAZIn5Jr1boSiqkFgLhUVoqMEHOGCFihRFltpoDbdHs80Ao3GBzHyHHOwNMm2j4XLDBDkAogroNPST4EJEqY5ws2GMCJHq61gGJDbfJEk8Bu1LQLlSde10OcVoyRvQUN2qHqkD3bHsENndvkIkJ7OR8fpKH4EwsZgyBN/A2bEo33bBI/dcLeHREKcIxjo3c8coezSfJDu96pRoC+IJpS9y0AzWwsGHyA2gWtfMNeLIiiqCsFUkmzDY3/G7XTqtSodrvrTCxcxLVJmuUQoufgZMISA7sKcr3LGwiwiduyCdapYF+PrAyIB8vPDiaxx1mMKMgMSvGULAJJrPDPeS+dyKzpdExCgwMOWJLMUsISoNNF4DRmQsEmr9ldXQjvZ6tmqbzF0NU39K4vrKyhLl4LXigVPSy/HCcPRRVStecvYM5LlUXokAtA9FguEguzCCXsuIaJOsw0rr1i1eOjdThSqzFJi6EtJje2baQnUgfgYwkMCqDdWYz4+ksUXSnJXgClHUGgo2ZzIuSigONnQXzTDRYLR9NF71coDKF9tVhp68QJ2QojuNBYIOTPmC6b7WEJAZohAj9yBpA9cAyupnlRPtWypsDBCbYCEgVKlff+VkML0pGkB/KzdrrxlrFWBStiLktavZrZTAANGoTiTvcSgUDLTuCghRRenCF6wmYzBgdo5jA+9xOR4w6DhE3qRFRaaKoZV5MqyYHBBhs3Y/3StosJCGFUQkNZy8LGPZezoWcoYETShFAQEAalFCAFjMtbMkqBNgy+ywIShpdeISERJioMwRRoEHbOMBnIy6goFWl5oqHQUD4ONACXGmzJiAJIAo5zWDw/a5Y5dJD7SK99q1RR2HGkMhT7D8ZJcsjVmX3N0ugcNSgEKmeWtahsQtDNtNEx9Dx0T1DpvWAJ3jb3fn+Pvv7QICW0V7rvx0d7GCxdpzVgfi6fXnw5c/86Int1oBRJj3RWKqMNMDgqkj6/a7QSHZ5pA8wL3ObBPHp2v0/M6wAt89YFhP5xbu3q/tVjJENxwYnly8jg8gT+oGhELdZc4gnknVr1e+qTBAc+/fRTVISUqE9gLx5WDCHiDpc2OcF0ZZ8gc4epg1mCBxjAYhCLqN2ynVmACj0cT/QGzOajUdx2PY0/K1nvBeaIfUGYiguxINtrfSGArzZIwkjJCISRE4mIAYIHKwXykemwzqEEIRBdsUpPEmpQ+b18nmagA3FgWGsFibhQ3AfQedJz+tA4Am07WzqLH93hCJS7ziLtM5AWBZOYJ9aA29V37DMm1Ad4oZxQx9Ypu39iIdvf27utxMZMtGEOeugTrhOFr4dCjbQJKMVl0oF2hvAD0twPMpnMk8mIDifpDQiL5E0dAfAE0gdE86A9R3HnwOCn1E7hQ+CfHkBmqlonhzA1QhsZjpou0AAN/3CxWoMClgIw0vmlcsqakgySGnuKiMVZrMvtyWqhKxsXJ1BD/BDq0NWI4oIqh/xdyRThQkOy9qh8=")); // Original HTML From :::: dshamlin98
}
elseif ($_SERVER["HTTP_HOST"] == $freedomaines[22])
{
echo "<title>Quand Internet Me Respect Pas :(</title>";
echo "<h1>Les Sites D'actus</h1>";
echo "Ah Les Site D'actus Sont Bien Pointé Du Doigt, Car Ils Peuvent Faire Infinity Scroll, Player Auto Qui Se Lance Tout Seul Le Son Coupé, Et Suit L'internaute Quand Il Scroll Pour Sortir De La Vidéo, Et Bien Sur Il Ya Vais Pas Ces Parasite Au Passer.";
echo "<h1>Les Resultats De Recherche Aux Services Désagreable</h1>";
echo "Le Moteur De Recherche Le Plus Populaire, Met En Tête Des Resultat Des Site Ou Votre Télécharchement Ce Requis D'une Inscription, Au Sujet De Télécharger Des Sons Pour Vos Effet Sonores, Ou Encores Des icones Et J'empasse, Portant Il Ya 10 Ans (2012) Ce Moteur De Recherche Retournais Pas Ces Desagrement On POuvais Télécharger Sans S'inscrire, Il Ya Des Alternative A Ces Services Mais Il Sont Plus En Tête Comme C'etait Au Passé.";
echo "<h1>Les Protection Anti-Copie</h1>";
echo "Vous Etes Peut Etre Deja Tombé Sur Un Site Qui Vous Empeche De Copier/Coller Quelque Chose Voir De Faire CTRL-I Et j'empasse ? <i>(Pour L'occasion Seulement Cette Page A Ce Type De Désagrement)</i> Ca Signifie Que L'aueteur N'est Pas Un Ami C'est Un Enemie Des Copieur Et Ami Des Droit D'auteur Autrement Dit, \"NonFreeUser\" !";
echo "<h1>L'incription Forcer Pour Continuer</h1>";
echo "A L'époque Un Site Ne Vous Forcez Pas A Vous Inscrire Pour Télécharger Quelque Chose Et Ne Devrais Jamais Le Faire Jusqu'a Présent, Et Portant On A Des Site Qui Force La Main A L'internaute, Comme Ca Il Collecte Des Noms Utilisateur Mails Ceux Qui Sont Abilité A Télécharger, C'est Innaccetable !, Et Les Alternative (Ceux Ou Ya Pas Inscription) Sont Pas Evidant A Trouvé.";
echo "<h2>Conclusion</h2>";
echo "Internet Devient De + En + Désagreable En Terme De Chose Indésirable A S'inscire Pour Les Enlevé Bien Que C'est Une Méthode Indésirable, Il Faut Bien S'inscrire Pour Faire Ces Achats Posté etc Mais, Pas Pour Télécharger Et Pour Enlevé Ces Désagrement, Bien Qui Avais Pas Ca Au Passer (2010)";
echo "<script src='jquery.min.js'></script><script src='amparecopyprotection.js'></script>"; // https://github.com/juthawong/Ampare-Copy-Protection
}
elseif ($_SERVER["HTTP_HOST"] == $freedomaines[23])
{
echo "<title>OpenFoodFacts</title><h1>Vefifier Un Produit Avec OpenFoodFacts</h1><form action='.' method='get'>";
echo "Tapez Le Code-Barre Du Produit ::::::::::: <input name='code' id='code'></input></br>";
if (isset($_GET["code"]))
{
$content = file_get_contents("en.openfoodfacts.org.products.csv"); // https://static.openfoodfacts.org/data/en.openfoodfacts.org.products.csv
$exploded = explode("\n",$content);
$namefield = explode("\t",$exploded[0]);
unset($content);
foreach ($exploded as $array)
{
$array = explode("\t",$array);
if ($array[0] == $_GET["code"])
{
echo "Conclusion ::::::::: <br/><tt>";
foreach ($array as $n => $field)
{
echo "$namefield[$n] :: $field<br/>";
}
break;
}
}
echo "</tt>";
}
}
elseif ($_SERVER["HTTP_HOST"] == $freedomaines[24])
{
echo bzdecompress(base64_decode("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")); // Need :::::::::::: https://github.com/josch/scriptreplayjs Just VT100.js And scriptreplay.js
}
elseif ($_SERVER["HTTP_HOST"] == $freedomaines[25])
{
$themevideo = "powwows";
$themetitle = "Pow-Wow";
$url        = "https://www.youtube.com/c/Powwows/videos";
echo "<title>$themetitle</title>";
echo "<h1>$themetitle</h1>";
if (isset($_GET["v"]))
{
echo "<video controls><source src=\"".$themevideo."/".$_GET['v']."\"></video><br/>";
echo file_get_contents($themevideo."/".basename($_GET['v'],".mp4").".description");
}
else
{
$vids = scandir($themevideo);
if ($vids == null)
{
mkdir($themevideo);
exec("youtube-dl -i -f 'mp4[height <= 360]' -o \"$themevideo/%(title)s.%(ext)s\" --write-thumbnail --write-description --playlist-end 100 $url");
exec("mogrify -format webp $themevideo/*.jpg");
}
foreach ($vids as $video)
{
if (pathinfo($video,PATHINFO_EXTENSION) == "mp4")
{
echo "<img width='100' src=\"".$themevideo."/".basename($video,".mp4").".webp\"><a href=\"?v=$video\">".basename($video,".mp4")."</a><br/>";
}
}
}
}
elseif ($_SERVER["HTTP_HOST"] == $freedomaines[26])
{
echo "<title>Emoticon Composer</title>";
echo "<style>@font-face{font-family:'emoticon-composer';src:url('emoticon-composer-Regular.ttf');}</style>"; // You Need :::::::::::::: https://github.com/google/emoticon-composer-font/blob/master/fonts/emoticon-composer-Regular.ttf
echo "<h1>Emoticon Composer</h1>";
echo "<input type='text' id='emo_in'><br/><font face='emoticon-composer' style='font-size:72px;' id='emo_out'></font>";
echo "<h2>Eyes (Uppercase)</h2><font style='font-size:48px;' face='emoticon-composer'>";
for ($n = 65;$n <= 90;$n++)
{
echo chr($n);
}
echo "</font><h2>Mouth (Lowercase)</h2><font style='font-size:48px;' face='emoticon-composer'>";
for ($n = 97;$n <= 122;$n++)
{
echo chr($n);
}
echo "</font><h2>Extra (Digit)</h2><font style='font-size:48px;' face='emoticon-composer'>";
for ($n = 48;$n <= 57;$n++)
{
echo chr($n);
}
echo "<script>function emo_time(){emo_out.innerHTML = emo_in.value;};setInterval(emo_time,40);</script>";
}
elseif ($_SERVER["HTTP_HOST"] == $freedomaines[27])
{
echo "<title>PT Measure - One Million Digits</title>";
echo "<tt>4.";
for ($n = 2;$n <= 1000000;$n++)
{
$s = strval($n*$n);
$u = 0;
for ($m=0;$m<strlen($s);$m++)
$u = $u + intval($s[$m]);
$a = (10-($u%10))%10;
echo $a;
if (boolval($n % 200) == 0)
echo "<br/>";
}
echo "</tt>";
}
elseif ($_SERVER["HTTP_HOST"] == $freedomaines[28]) // Here Need :::::::::::: https://github.com/Pixelsuft/hl ;; Without ::::::: index.html xash.html favicon.ico
{
if (boolval($_GET["xash"]))
echo bzdecompress(base64_decode("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"));
else
echo bzdecompress(base64_decode("QlpoOTFBWSZTWV7N1coAAjDfgHAwev//X7/nzuq/7//6UAX4WhlC3bva1vWnLUtEEkhBoEwj1TamEaKflQ9J6npqGmQD1A0PUejRBoVPCZSbCR6EyeiNAyZMEZGmQGgaNGTQSIRFM0mqeU0e0TajQ0NTaT9RogwDTQI2iG1BlSMg0aAZDRoAaaaAAGgAAABJJMCqexU/FTBNM9ER6ajEaDRiaYjEyAGmqnqRChCFwtIpikTSLMgBNgmDQhgmJNjYgTYk2khn3shDbBtMbS6mIhpNk9qFTcIGNh09PoiwFjCMDBjKCWSQ4GxNxLMRcZ3A0+0g/5jmOjoimF2jQDC3QchMMeX6+bvGD4X99MxWVPXTqOXwoMK9O9EHUI1dTUKc9jfvcAvqEBSsADT1KkRgPUuSmEsxIcQgdLZO/ovlZGS+rt3WTz4lbUs2iEuV8ZbfLNmxfAXYyZkHc0rk5hyYHMDNUdPfZ547qK0Yz6VLGEn0dd3NU3bsfQ9oP401QposJO8oXPHUlpHZfcFbND3sHU/3Xg5O1OjrcFCGgO+N73v3RLdxgaaG6vc9ckVr3ufsqbVw2GXFcWMWlj/XD5Hu+hnWfnKPTQ0XIfpi6s+c7f+MUhayzExhMQw5QaG5QR3ifW2xW71Gilz6xM0oypOEdyHPwNos32jATHED0dXDNjYDYDGMIMzUHHLsrRbFXbdzHktjVmTN0YYHGzfm43h4iObZHhoZRLqXMHwLesn9dyK2Z8fBbReC1tE2Zblxub7vN7S1qrz8jM2yP4Ih2meFxUKJkUjbPb36MP06tIdmfxcmV1D1vgOKjO8otkUWub0lnH5mxk1Lid8tllduD9dncTT/JodmVltpEqU+X+Qm9fhP4xcT4rsNL3+RV5EqSy2FwRzeMOuzpDQ6fv6YcDBlDv224v4THwk8nVGEM/QoGYaBmslmohlIxLjGUi0GwFW9SoQK6RiC2fYUMYDzFUBvCgtFUS8/rMVE9UcCvXcYNbSl/G8U6IE9VQ7e2rbHD07QFcfKdc5VkRnzGmapwQiux4dZa2laGxjGzflBTCfBh3KNqKkV2BkY2chD4xA4XlxoWvVULC/ag1SqipF6iQd7fY6BAY7LQyW5iPBsIU8H7X+0GewtaDgiTBoEypzMEWzkQ0uc8UYhkguGDzlKFnrDv7ZdffPwdaF4LwwiAiAZrjYbqg0iyQ1EGoSQ+7EvqnXWBwOHGdLyreFcDi94svaMlvbuMj1XB162+cvFkKq6CIRMURxot1jxmk4XUQmwJcNbZSW0RLOqCnSPCwlBCOi9K0xPqtUokjiAcuEIN4zOjm2hdbvxFWUJaVNc9NkWqaYQ1iGXwWs6a85CpJGzyvDCOoDDFy9LkaZAxUB1mq4fDSkZ0o7mgkSdgzcJw3HiqlFRvpLA523zI4+g0EUlmJrtZQs8AgQm2kNwrZilFecYAxfeicIvRTNpOHpB0qK9Bgw4qUyoY22G68yZtoNF7ooQwhWhUxaZEWlFCi9xuEmghohJl+3q1Yxt7mvkYbwZmawOgIpLnaNbnDOGZKrItEb/ZYk1AqVcgrYVViCJlM1PBNWomsT0SWBWMDA1C+12qtwzFlaybt60uqZTLoZ9diPz0j2XgeAf0chfywzA7rOIm1mEGmAwwDsW2ysTxGw9X40F3c9FCSJlPMiZoeOayDnlxiGapzE7cA16NasuVmpUFEbZ4VN45cpucUFk5lR61juURlvptuyrONoWc0JmO5gYZVjRGHXG1cNGE44LfeLjeCpJGqzqUc1ss1Y7y2kcVKWmDrDkFZZVrxuJhNp1PImOSHUqRa4fgoLRg1OU6iZB4lbMUQ7+nDXqYj8YG6JINm1IcspGhy1UzZil2xLG61XusPsM16VQrnxromgyRoHtOTUk09oHYaSfVoz2A4tT1Uwaj6EK3EHOxZG0jc/Ab6opkvocANvc/8XckU4UJBezdXKA"));
}
elseif ($_SERVER["HTTP_HOST"] == $freedomaines[29])
{
$themevideo = "kara";
$themetitle = "Kara";
$url        = "https://www.youtube.com/channel/UCM4ElalZityYotQIhqpBCpw/videos";
echo "<title>$themetitle</title>";
echo "<h1>$themetitle</h1>";
if (isset($_GET["v"]))
{
echo "<video controls><source src=\"".$themevideo."/".$_GET['v']."\"></video><br/>";
echo file_get_contents($themevideo."/".basename($_GET['v'],".mp4").".description");
}
else
{
$vids = scandir($themevideo);
if ($vids == null)
{
mkdir($themevideo);
exec("youtube-dl -i -f 'mp4[height <= 360]' -o \"$themevideo/%(title)s.%(ext)s\" --write-thumbnail --write-description $url");
exec("mogrify -format webp $themevideo/*.jpg");
}
foreach ($vids as $video)
{
if (pathinfo($video,PATHINFO_EXTENSION) == "mp4")
{
echo "<img width='100' src=\"".$themevideo."/".basename($video,".mp4").".webp\"><a href=\"?v=$video\">".basename($video,".mp4")."</a><br/>";
}
}
}
}
else
{
echo "<tt>Name Unknow!<br/><a href='http://linksourmaster.chezsick-black'>Return The Links</a></tt>";
}
$domcum = explode(".",$_SERVER["HTTP_HOST"]);
switch ($domcum[1])
{
case "chezsick-red":
$color = "E6194B";
break;
case "chezsick-green":
$color = "3CB44B";
break;
case "chezsick-yellow":
$color = "FFE119";
break;
case "chezsick-blue":
$color = "4363D8";
break;
case "chezsick-orange":
$color = "F58231";
break;
case "chezsick-purple":
$color = "911EB4";
break;
case "chezsick-cyan":
$color = "42D4F4";
break;
case "chezsick-magenta":
$color = "F032E6";
break;
case "chezsick-lime":
$color = "BFEF45";
break;
case "chezsick-pink":
$color = "FABED4";
break;
case "chezsick-teal":
$color = "469990";
break;
case "chezsick-lavender":
$color = "DCBEFF";
break;
case "chezsick-brown":
$color = "9A6324";
break;
case "chezsick-beige":
$color = "FFFAC8";
break;
case "chezsick-maroon":
$color = "800000";
break;
case "chezsick-mint":
$color = "AAFFC3";
break;
case "chezsick-olive":
$color = "808000";
break;
case "chezsick-abricot":
$color = "FFD8B1";
break;
case "chezsick-navy":
$color = "000075";
break;
case "chezsick-abricot":
$color = "FFD8B1";
break;
case "chezsick-grey":
$color = "A9A9A9";
break;
case "chezsick-white":
$color = "FFFFFF";
break;
case "chezsick-black":
$color = "000000";
break;
default:
$color = "000000";
break;
}
$imgpadlock = base64_encode("<?xml version='1.0' encoding='UTF-8' standalone='no'?><svg xmlns:inkscape='http://www.inkscape.org/namespaces/inkscape' xmlns:rdf='http://www.w3.org/1999/02/22-rdf-syntax-ns#' xmlns='http://www.w3.org/2000/svg' xmlns:cc='http://creativecommons.org/ns#' xmlns:dc='http://purl.org/dc/elements/1.1/' xmlns:sodipodi='http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd' xmlns:svg='http://www.w3.org/2000/svg' xmlns:ns1='http://sozi.baierouge.fr' xmlns:xlink='http://www.w3.org/1999/xlink' id='svg2064' sodipodi:docname='padlock_silhouette_a.j.__01.svg' viewBox='0 0 85.603 121.62' sodipodi:version='0.32' version='1.0' inkscape:output_extension='org.inkscape.output.svg.inkscape' y='0' x='0' inkscape:version='0.46'><sodipodi:namedview id='base' bordercolor='#666666' inkscape:pageshadow='2' guidetolerance='10.0' pagecolor='#ffffff' gridtolerance='10.0' inkscape:zoom='3.0933333' objecttolerance='10.0' borderopacity='1.0' inkscape:current-layer='g2061' inkscape:cx='19.881466' inkscape:cy='72.737069' inkscape:window-y='44' inkscape:window-x='0' inkscape:window-height='1006' showgrid='false' inkscape:pageopacity='0.0' inkscape:window-width='1680'/><g id='layer1' transform='translate(-32.199 -14.191)'><g id='g2061' transform='translate(10.641 12.191)'><path id='rect2723' style='fill-rule:evenodd;fill:#$color' d='m64.359 2c-20.072 0-36.231 16.159-36.231 36.231v40.256h10.064v-40.256c0-14.497 11.671-26.167 26.167-26.167s26.167 11.67 26.167 26.167v40.256h10.064v-40.256c0-20.072-16.159-36.231-36.231-36.231z'/><rect id='rect1941' style='fill-rule:evenodd;fill:#$color' rx='0.5' ry='.5' height='66.259' width='85.603' y='57.359' x='21.558'/></g></g></svg>"); // https://openclipart.org/download/17932/AJ-Padlock-Silhouette.svg
if (!($nonhtml))
echo "<img width='24' style='position:fixed;right:8px;top:8px;' src='data:image/svg+xml;base64,$imgpadlock'/>";
?>