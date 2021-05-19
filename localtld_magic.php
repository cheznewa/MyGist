<?php
// Je Vais Faire De La Magie Avec ::::::::::::::: https://github.com/jweslley/localtld
// Ou Fois Installer, Faite La Commande :::::: LOCALTLD=chezsick _browser_
// Pour Commencé :::::::::::::::: [linksourmaster.chezsick](http://linksourmaster.chezsick)
// Et Accrochez-Vous !
// Mettez Ce Fichier Sur Votre Serveur Local Et Rennomé En index.php
// Si Ca Ne Marche Pas, Vous Devrait Vous-Même Télécharger Les Fichier Qui Manque à L'apelle.
$freedomaines = ["newanotremaitre.chezsick","timeanddatebletou.chezsick","logicemu.chezsick","jslinux.chezsick","randomlike.chezsick","colormodem.chezsick","dafont.chezsick","pagerankcalc.chezsick","pdf2htmlex.chezsick","lhvtools.chezsick","cestpassorcier.chezsick","dexsilicium.chezsick","logicemu2luxar.chezsick","titeuf.chezsick","codelyoko.chezsick","kidpaddle.chezsick","emonote.chezsick","garfield.chezsick","problemepointageamerindienne.chezsick","visualarm1.chezsick","infernalcounter.chezsick"];
if ($_SERVER["HTTP_HOST"] == "linksourmaster.chezsick")
{
echo "<title>ChezSick Links</title>";
echo "<h1>Liste Des Sites De Newa Disponible</h1>";
foreach ($freedomaines as $domaine)
{
echo "<a href=\"http://$domaine\">$domaine</a><br/>";
}
}
elseif ($_SERVER["HTTP_HOST"] == $freedomaines[0])
{
echo "<title>Newa Notre Maitre - Site Officiel</title><style>body{background-color:#00288c;color:white;}</style><h1>Bonjour Tout Le Monde, C'est Newa Notre Maitre !</h1>Je Suis Un Grand Oiseau, Et Je Joue De La Flute Des Andes, Passionné De Culture Amerindienne (En Interne), Je Suis Sur L'ordinateur Depuis Pas Mal De Temps.";
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
exec("youtube-dl -i -f mp4 -o \"$themevideo/%(title)s.%(ext)s\" --write-thumbnail --write-description $url");
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
exec("youtube-dl -i -f mp4 -o \"$themevideo/%(title)s.%(ext)s\" --write-thumbnail --write-description $url");
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
echo "<head><title>LogicEmu - Online Logic Simulator</title></head>";
echo "<body><noscript>Please Enable Javascript!</noscript>";
echo "<script src=\"logicemu.js\"></script>";
echo "<script src=\"main.js\"></script>";
echo "<script src=\"circuits_help.js\"></script>";
echo "<script src=\"circuits_articles.js\"></script>";
echo "<script src=\"circuits_main.js\"></script>";
echo "<script src=\"footer.js\"></script>";
echo "<script type='text/javascript'>var c = origtext.replace(/\\\"[^\\\"]*\\\"/g,'');var icd = (c.split('I')).length-1;var ic = (c.split('i')).length-1;\n";
echo "var logici = 0;var logici = logici + (c.split('a')).length-1;var logici = logici + (c.split('e')).length-1;var logici = logici + (c.split('o')).length-1;var logici = logici + (c.split('h')).length-1;var logici = logici + (c.split('z')).length-1;\n";
echo "var logicinv = 0;var logicinv = logicinv + (c.split('A')).length-1;var logicinv = logicinv + (c.split('E')).length-1;var logicinv = logicinv + (c.split('O')).length-1;var logicinv = logicinv + (c.split('H')).length-1;var logicinv = logicinv + (c.split('Z')).length-1;\n";
echo "var inputi = 0;var inputi = inputi + (c.split('^')).length-1;var inputi = inputi + (c.split('v')).length-1;var inputi = inputi + (c.split('<')).length-1;var inputi = inputi + (c.split('>')).length-1;\n";
echo "var inputinv = 0;var inputinv = inputinv + (c.split('m')).length-1;var inputinv = inputinv + (c.split('w')).length-1;var inputinv = inputinv + (c.split('[')).length-1;var inputinv = inputinv + (c.split(']')).length-1;\n";
echo "var led = 0;var led = led + (c.split('l')).length-1;var led = led + (c.split('L')).length-1;\n";
echo "var memory = 0;var memory = memory + (c.split('b')).length-1;var memory = memory + (c.split('B')).length-1;\n";
echo "var kinetic = (c.split('K')).length-1;var alu = (c.split('U')).length-1;var termi = (c.split('T')).length-1;var matrix = (c.split('D')).length-1;var quartz = (c.split('t')).length-1;\n";
echo "var switchy = 0;var switchy = switchy + (c.split('s')).length-1;var switchy = switchy + (c.split('\\S')).length-1;var switchy = switchy + (c.split('p')).length-1;var switchy = switchy + (c.split('P')).length-1;\n";
echo "var pist = Math.abs((((alu%11) + (logici - logicinv)) * Math.floor(ic/(icd+1))) + (termi%3) + ((switchy*2)+(led*3)) + (matrix%7) + (quartz%5) + (inputi - inputinv) + (memory % 17) - kinetic)%16;\n";
echo "var tracks = ['LUXAR__Stephane_Marty__01_Birth.mp3','LUXAR__Stephane_Marty__02_First_steps.mp3','LUXAR__Stephane_Marty__03_Curiosity.mp3','LUXAR__Stephane_Marty__04_Process.mp3','LUXAR__Stephane_Marty__05_Free_will.mp3','LUXAR__Stephane_Marty__06_Scar.mp3','LUXAR__Stephane_Marty__07_Loneliness.mp3','LUXAR__Stephane_Marty__08_Explorer.mp3','LUXAR__Stephane_Marty__09_Chase.mp3','LUXAR__Stephane_Marty__10_Revolution.mp3','LUXAR__Stephane_Marty__11_Blooming.mp3','LUXAR__Stephane_Marty__12_Torment.mp3','LUXAR__Stephane_Marty__13_Awareness.mp3','LUXAR__Stephane_Marty__14_Self-confidence.mp3','LUXAR__Stephane_Marty__15_Ambition.mp3','LUXAR__Stephane_Marty__16_Responsability.mp3'];\n"; // http://www.dexsilicium.com/musiques.html
echo "document.write(\"<audio autoplay hidden loop><source src='\"+tracks[pist]+\"'></audio>\");</script>";
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
exec("youtube-dl -i -f mp4 -o \"$themevideo/%(title)s.%(ext)s\" --write-thumbnail --write-description $url");
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
exec("youtube-dl -i -f mp4 -o \"$themevideo/%(title)s.%(ext)s\" --write-thumbnail --write-description $url");
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
exec("youtube-dl -i -f mp4 -o \"$themevideo/%(title)s.%(ext)s\" --write-thumbnail --write-description $url");
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
if (isset($_GET["emo"]))
{
if ((intval($_GET["emo"]) <= 50) and (intval($_GET["emo"]) >= -50))
{
$nota = intval($_GET["emo"])+188;
header("Content-Type: image/png");
$id = uniqid();
$img = exec("convert -size 256x256 xc:none -stroke black -strokewidth 2.5 -fill none -draw \"circle 128,128 128,253 circle 64,64 64,68 circle 192,64 192,68 bezier 64,188 128,$nota 192,188\" /tmp/$id.png");
readfile("/tmp/$id.png");
}
else
{
echo "Choisi Une Valeur Entre -50 Et 50";
}
}
echo "<title>EmoNote - Note Ce Que Tu Veut !</title><h1>Note Ce Que Tu Veut !</h1><form method='GET' action='.'>Négatif<input type='range' min='-50' max='50' name='emo' value='0'/>Positif<br/><input type='submit'/>";
}
elseif ($_SERVER["HTTP_HOST"] == $freedomaines[17])
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
elseif ($_SERVER["HTTP_HOST"] == $freedomaines[18])
{
echo "Contrairement Aux Idée Reçu Ils Viennent Pas Des Etat-Unis Mais Majoritairement D'équateur, Pays Donc Mauvaise Oeuil Quand Il S'agit De Le Faire Sur Toute L'europe L'asie Et Surtout La Russie Que Leur Propre Zone.";
echo "<title>Pointages Amerindien - Imprévisible, Rare, Grave !</title>";
echo "<h1>Imprévisible</h1>Un Pointage En Général Est Une Personne Qui Joue De La Musique Dans La Rue Pour Gagner De L'argent, Bien Que C'est Pas Planifier Publiquement, C'est Pareil Pour Les Pointages Amerindien.";
echo "<h1>Rare</h1>Les Pointage Amerindien Sont Vraiment Pas Frequent Qu'un Pointage Classique Et Portant Ya Sur Une Des Platforme Vidéo Très Populaire Une Circulation Pas Possible De Ces Pointage, Une Chaine Peut Se Retrouvé Avec Une Seul Vidéo D'un Pointage Pour Ca Frequence Pas Possible.";
echo "<h1>Grave</h1>Les Pointage Amerindien, Sont Très Souvant Déconcertante Sur Ces Tenu Introuvable Sur Internet Pour Un Passionné, Est Ces Instrument Mais Un Peut Plus Facile A Retrouvé Sur Le Net, Ils Se Raproche Asser Souvant Du Pow-Wow Car Pour Cause Ya Une Tenu Avec Un Bustle Plus Frequent D'apparition Qu'une Coiffe, Mais Ce Qui Est Déconcertant Avec Leur Tenu C'est Les Déssins Avec Les Frange Longue.";
echo "<h2>Conclusion</h2>Les Pointages Amerindiens Peuvent Basculé Toute Une Journé Voir Toute Une Vie, Et Il Est Pas Possible De S'en Prévenir, Et Encore Moin De Les Eradiqué.";
}
elseif ($_SERVER["HTTP_HOST"] == $freedomaines[19])
{
echo bzdecompress(base64_decode("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")); // From https://github.com/glitchcore/arm1/blob/master/index.html Because Too Complex To Customize
}
elseif ($_SERVER["HTTP_HOST"] == $freedomaines[20])
{
echo "<title>The Infernal Counter !</title>";
echo bzdecompress(base64_decode("QlpoOTFBWSZTWey9qh8ABRVf5XAwc3///z9nzCA/99/6AQAggAgAEABgBlwfUUKoKrlqgAEHGTJoxDE0wEDAmmCMExNNNABhCJMmCaCNAbUAAAAAAAAAcZMmjEMTTAQMCaYIwTE000AGEEmpIk9JP1JkGI009TJ6IMhpppoDI00A00aHGTJoxDE0wEDAmmCMExNNNABhBEkSZAJiJ5KbZUjeVPRqafqZJ6R6mgDwKeo/VBs9qSGQkyMkVURQgskFQYCsIoRSQUBRGCQVRYAiqqT9yajDMhBEYiyLAZIn5Jr1boSiqkFgLhUVoqMEHOGCFihRFltpoDbdHs80Ao3GBzHyHHOwNMm2j4XLDBDkAogroNPST4EJEqY5ws2GMCJHq61gGJDbfJEk8Bu1LQLlSde10OcVoyRvQUN2qHqkD3bHsENndvkIkJ7OR8fpKH4EwsZgyBN/A2bEo33bBI/dcLeHREKcIxjo3c8coezSfJDu96pRoC+IJpS9y0AzWwsGHyA2gWtfMNeLIiiqCsFUkmzDY3/G7XTqtSodrvrTCxcxLVJmuUQoufgZMISA7sKcr3LGwiwiduyCdapYF+PrAyIB8vPDiaxx1mMKMgMSvGULAJJrPDPeS+dyKzpdExCgwMOWJLMUsISoNNF4DRmQsEmr9ldXQjvZ6tmqbzF0NU39K4vrKyhLl4LXigVPSy/HCcPRRVStecvYM5LlUXokAtA9FguEguzCCXsuIaJOsw0rr1i1eOjdThSqzFJi6EtJje2baQnUgfgYwkMCqDdWYz4+ksUXSnJXgClHUGgo2ZzIuSigONnQXzTDRYLR9NF71coDKF9tVhp68QJ2QojuNBYIOTPmC6b7WEJAZohAj9yBpA9cAyupnlRPtWypsDBCbYCEgVKlff+VkML0pGkB/KzdrrxlrFWBStiLktavZrZTAANGoTiTvcSgUDLTuCghRRenCF6wmYzBgdo5jA+9xOR4w6DhE3qRFRaaKoZV5MqyYHBBhs3Y/3StosJCGFUQkNZy8LGPZezoWcoYETShFAQEAalFCAFjMtbMkqBNgy+ywIShpdeISERJioMwRRoEHbOMBnIy6goFWl5oqHQUD4ONACXGmzJiAJIAo5zWDw/a5Y5dJD7SK99q1RR2HGkMhT7D8ZJcsjVmX3N0ugcNSgEKmeWtahsQtDNtNEx9Dx0T1DpvWAJ3jb3fn+Pvv7QICW0V7rvx0d7GCxdpzVgfi6fXnw5c/86Int1oBRJj3RWKqMNMDgqkj6/a7QSHZ5pA8wL3ObBPHp2v0/M6wAt89YFhP5xbu3q/tVjJENxwYnly8jg8gT+oGhELdZc4gnknVr1e+qTBAc+/fRTVISUqE9gLx5WDCHiDpc2OcF0ZZ8gc4epg1mCBxjAYhCLqN2ynVmACj0cT/QGzOajUdx2PY0/K1nvBeaIfUGYiguxINtrfSGArzZIwkjJCISRE4mIAYIHKwXykemwzqEEIRBdsUpPEmpQ+b18nmagA3FgWGsFibhQ3AfQedJz+tA4Am07WzqLH93hCJS7ziLtM5AWBZOYJ9aA29V37DMm1Ad4oZxQx9Ypu39iIdvf27utxMZMtGEOeugTrhOFr4dCjbQJKMVl0oF2hvAD0twPMpnMk8mIDifpDQiL5E0dAfAE0gdE86A9R3HnwOCn1E7hQ+CfHkBmqlonhzA1QhsZjpou0AAN/3CxWoMClgIw0vmlcsqakgySGnuKiMVZrMvtyWqhKxsXJ1BD/BDq0NWI4oIqh/xdyRThQkOy9qh8=")); // Original HTML From :::: dshamlin98
}
else
{
echo "<tt>Name Unknow!<br/><a href='http://linksourmaster.chezsick'>Return The Links</a></tt>";
}
?>
