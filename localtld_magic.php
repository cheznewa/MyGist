<?php
// Je Vais Faire De La Magie Avec ::::::::::::::: https://github.com/jweslley/localtld
// Ou Fois Installer, Faite La Commande :::::: LOCALTLD=free _browser_
// Pour Commencé :::::::::::::::: [freelinks.free](http://freelinks.free)
// Et Accrochez-Vous !
// Mettez Ce Fichier Sur Votre Serveur Et Rennomé En index.php
// Si Ca Ne Marche Pas, Vous Devrait Vous-Même Télécharger Les Fichier Qui Manque à L'apelle.
$freedomaines = ["newanotremaitre.free","timeanddatebletou.free","logicemu.free","jslinux.free","randomlike.free","colormodem.free","randomfonts.free","pagerankcalc.free","pdf2htmlex.free"];
if ($_SERVER["HTTP_HOST"] == "freelinks.free")
{
echo "<title>Free Links</title>";
echo "<h1>Liste Des Sites Free Disponible</h1>";
foreach ($freedomaines as $domaine)
{
echo "<a href=\"http://$domaine\">$domaine</a><br/>";
}
}
if ($_SERVER["HTTP_HOST"] == $freedomaines[0])
{
echo "<title>Newa Notre Maitre -  Site Officiel</title><style>body{background-color:#00288c;color:white;}</style><h1>Bonjour Tout Le Monde, C'est Newa Notre Maitre !</h1>Je Suis Un Grand Oiseau, Et Je Joue De La Flute Des Andes, Passionné De Culture Amerindienne (En Interne), Je Suis Sur L'ordinateur Depuis Pas Mal De Temps.";
}
if ($_SERVER["HTTP_HOST"] == $freedomaines[1])
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
if ($_SERVER["HTTP_HOST"] == $freedomaines[2])
{
echo "<title>LogicEmu - Online Logic Simulator</title>";
echo "Please Enabled Javascript!";
echo "<script src=\"editor.js\"></script>";
echo "<script src=\"logicemu.js\"></script>";
echo "<script src=\"main.js\"></script>";
echo "<script src=\"circuits_help.js\"></script>";
echo "<script src=\"circuits_articles.js\"></script>";
echo "<script src=\"circuits_main.js\"></script>";
echo "<script src=\"footer.js\"></script>";
}
if ($_SERVER["HTTP_HOST"] == $freedomaines[3])
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
if ($_SERVER["HTTP_HOST"] == $freedomaines[4])
{
require("config.php");
echo "<title>RandomLike</title>";
echo "<h1><img src='logo.png'/></h1>";
echo "Vous Avez Le Choix De Mes Services ::::: <br/><a href='number.php?min=0&max=100'>Nombre Aléatoire</a><br/><a href='color.php'>Couleur Aléatoire</a><br/><a href='password.php?len=16'>Mot De Passe Aléatoire</a><br/><a href='race.php?pist=6&len=10'>Course Aléatoire</a><br/><a href='loto.php?tirage=5&nbball=20'>Tirage Du Loto</a><br/><a href='galton.php'>La Planche De Galton</a><br/><a href='date.php?future=60'>Un Rendez-Vous Aléatoire</a><br/><a href='text.php?nb=100&lang=fr'>Générateur De Texte Aleatoire</a><br/><a href='naf.php?len=50&plus=0'>Générateur De Partition Pour Flute Amerindienne</a><br/><a href='para.php'>Anti-Probabilité Aléatoire</a><br/><a href='decay.php?nb=100'>Générateur De Demi-Vie</a><br/><a href='carddice.php?card=20&dice=2&joker=0'>Carte Et Dé Aléatoire</a><br/><a href='asciicast.php'>Regarder Une Vidéo Asciinema Aléatoire</a><br/><a href='youtube.php'>Regarder Une Vidéo YouTube Aléatoire</a><br/>";
echo "<br/><a href='syster.php?tp=1&demi=0&frame=1000'>Paramettre D'encodage Nagravision Syster Pour CryptImage</a><br/><a href='videocrypt.php?frame=1000&begin=40&end=215'>Paramettre D'encodage VideoCrypt Pour CryptImage</a><br/><a href='weather.php?frame=1000&cold_hot=0&cloud_sun=0&cloud_rain=0&cloud_snow=0&cloud_storm=0&cloud_fog=0&wind=0&min=-1&max=1'>Générateur De Paramettre Météo</a><br/><a href='graph.php?nbedge=500&maxnode=800'>Généreteur De Graph Aléatoire</a><br/><a href='bytes.php?len=1000&binary=1'>Octets Aléatoire</a><br/>";
$count = file_get_contents($randomsourcecount);
echo "<br/>Le Site A Générer ::::::: " . $count . " Octet -:- Source Aléatoire :::::: ".$randomsourceinfo. " -:- <a href='stats.php'>Les Statistiques</a>";
}
if ($_SERVER["HTTP_HOST"] == $freedomaines[5])
{
echo "<title>Color Modem In My World</title>";
echo '<h1>Color Modem In My World At Vilande</h1><form enctype="multipart/form-data" action="proc.php" method="post">Please Select Video To Process ::<input type="file" name="userfile"/><br/>Select Standard From Country In My World :: <select name="country" id="country"><optgroup label="Normal System"><option value="bt">BLE TOU</option><option value="ph">Phélÿn</option><option value="eu">Eurack</option></optgroup><optgroup label="Andean System"><option value="mo">Moênne</option><option value="in">Indie</option><option value="so">Solainie</option><option value="mv">Movenie</option><option value="js">Joséro</option><option value="ln">Luana</option></optgroup><optgroup label="VHS Zone"><option value="ns">Normal System</option><option value="as">Andean System</option></optgroup></select><br/>Select Mode For Process :: <select name="mode" id="mode"><option value="modem">Modulate And Demodulate</option><option value="mod">Modulate Only</option><option value="demod">Demodulate Only</option><option value="multi">Multiplex (Modulate In Second, And Demodulate In First)</option></select><br/><input type="submit" value="Process Now!"></br></form>';
}
if ($_SERVER["HTTP_HOST"] == $freedomaines[6])
{
echo "<title>Random Fonts</title>";
$fonts = scandir("fonts");
$nbf = count($fonts);
$attrf = rand(0,$nbf);
echo "<style>@font-face{font-family:aRandomFont;src:url(\"fonts/$fonts[$attrf]\");}</style>";
echo "<font size='6' face=\"aRandomFont\">".basename($fonts[$attrf],".ttf")."<br/>";
for ($c = 32;$c<=118;$c++)
{
echo chr($c);
}
echo "</fonts>";
}
if ($_SERVER["HTTP_HOST"] == $freedomaines[7])
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
if ($_SERVER["HTTP_HOST"] == $freedomaines[8])
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
readfile("/tmp/".$pdf.".html");
}
else
{
echo "<title>pdf2htmlEX</title>";
echo "<form enctype='multipart/form-data' action='.' method='post'>Please Select PDF :: <input type='file' name='pdffile' accept='application/pdf'/><br/><input type='submit' value='Submit'/><br/></from>";
}
}
?>
