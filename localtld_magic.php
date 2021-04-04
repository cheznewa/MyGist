<?php
// Je Vais Faire De La Magie Avec ::::::::::::::: https://github.com/jweslley/localtld
// Ou Fois Installer, Faite La Commande :::::: LOCALTLD=free _browser_
// Pour Commencé :::::::::::::::: [freelinks.free](http://freelinks.free)
// Et Accrochez-Vous !
// Mettez Ce Fichier Sur Votre Serveur Local Et Rennomé En index.php
// Si Ca Ne Marche Pas, Vous Devrait Vous-Même Télécharger Les Fichier Qui Manque à L'apelle.
$freedomaines = ["newanotremaitre.free","timeanddatebletou.free","logicemu.free","jslinux.free","randomlike.free","colormodem.free","randomfonts.free","pagerankcalc.free","pdf2htmlex.free","lhvtools.free","cestpassorcier.free","dexsilicium.free","logicemu2luxar.free","titeuf.free","codelyoko.free","kidpaddle.free"];
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
echo "<title>Newa Notre Maitre - Site Officiel</title><style>body{background-color:#00288c;color:white;}</style><h1>Bonjour Tout Le Monde, C'est Newa Notre Maitre !</h1>Je Suis Un Grand Oiseau, Et Je Joue De La Flute Des Andes, Passionné De Culture Amerindienne (En Interne), Je Suis Sur L'ordinateur Depuis Pas Mal De Temps.";
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
echo "<body><noscript>Please Enable Javascript!</noscript></body>";
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
echo "<title>pdf2htmlEX</title>";
readfile("/tmp/".$pdf.".html");
}
else
{
echo "<title>pdf2htmlEX</title>";
echo "<form enctype='multipart/form-data' action='.' method='post'>Please Select PDF :: <input type='file' name='pdffile' accept='application/pdf'/><br/><input type='submit' value='Submit'/><br/></from>";
}
}
if ($_SERVER["HTTP_HOST"] == $freedomaines[9])
{
echo "<title>Les Outils En Ligne Du Hollandais Volant</title>";
echo base64_decode("CTxoMj5FbmNvZGFnZSwgZMOpY29kYWdlPC9oMj4KCTxkaXYgY2xhc3M9ImJsb2MiIGRhdGEtZGVzY3JpcHRpb249InFyY29kZSBmbGFzaGNvZGUgY3LDqWVyIGltYWdlIj4KCQk8YSBocmVmPSJxcmNvZGUvIj4KCQkJPGltZyBzcmM9InFyY29kZS9pY29uLnBuZyIgYWx0PSJpY29uIi8+CgkJCUNyw6llciB1bjxici8+UVItQ29kZQoJCTwvYT4KCTwvZGl2PgoJPGRpdiBjbGFzcz0iYmxvYyIgZGF0YS1kZXNjcmlwdGlvbj0idW4gcXJjb2RlIHFyLWNvZGUgZmxhc2hjb2RlIGTDqWNvZGVyIGZsYXNoZWQgd2ViY2FtIHBob3RvIj4KCQk8YSBocmVmPSJycXJjb2RlLyI+CgkJCTxpbWcgc3JjPSJycXJjb2RlL2ljb24ucG5nIiBhbHQ9Imljb24iLz4KCQkJRMOpY29kZXIgdW48YnIvPlFSLUNvZGUKCQk8L2E+Cgk8L2Rpdj4KCTxkaXYgY2xhc3M9ImJsb2MiIGRhdGEtZGVzY3JpcHRpb249ImNvbnZlcnRpc3NldXIgY29udmVyc2lvbiBiYXNlNjQgYmFzZXMiPgoJCTxhIGhyZWY9ImJhc2U2NC8iPgoJCQk8aW1nIHNyYz0iYmFzZTY0L2ljb24ucG5nIiBhbHQ9Imljb24iLz4KCQkJRW4vZMOpY29kZXI8YnIvPmR1IGJhc2U2NAoJCTwvYT4KCTwvZGl2PgoJPGRpdiBjbGFzcz0iYmxvYyIgZGF0YS1kZXNjcmlwdGlvbj0iY2hpZmZyZW1lbnQgY29kYWdlIGVuY29kYWdlIGTDqWNvZGFnZSBkZSBjw6lzYXIgY2VzYXIgdmlnZW7DqHJlIj4KCQk8YSBocmVmPSJjZXNhci8iPgoJCQk8aW1nIHNyYz0iY2VzYXIvaWNvbi5wbmciIGFsdD0iaWNvbiIvPgoJCQlDaGlmZnJlbWVudDxici8+ZGUgQ8Opc2FyCgkJPC9hPgoJPC9kaXY+Cgk8ZGl2IGNsYXNzPSJibG9jIiBkYXRhLWRlc2NyaXB0aW9uPSJjaGFyYWN0ZXIgY2FyYWN0w6hyZSBlbmNvZGFnZSB1dGY4IHV0Zi04IHV0ZiA4IHVuaWNvZGUgZW1vamkgY29kZSI+CgkJPGEgaHJlZj0iY2hhcmNvZGUvIj4KCQkJPGltZyBzcmM9ImNoYXJjb2RlL2ljb24ucG5nIiBhbHQ9Imljb24iLz4KCQkJRW5jb2RhZ2UgZOKAmXVuPGJyLz5jYXJhY3TDqHJlCgkJPC9hPgoJPC9kaXY+Cgk8aDI+Q29udmVydGlzc2V1cnMgbnVtw6lyaXF1ZTwvaDI+Cgk8ZGl2IGNsYXNzPSJibG9jIiBkYXRhLWRlc2NyaXB0aW9uPSJtYXRow6ltYXRpcXVlIGJhc2VzIGNvbnZlcnRpc3NldXIgZW50cmUgYmluYWlyZSBoZXhhZMOpY2ltYWwgb2N0YWwgZMOpY2ltYWwiPgoJCTxhIGhyZWY9ImJhc2VzLyI+CgkJCTxpbWcgc3JjPSJiYXNlcy9pY29uLnBuZyIgYWx0PSJpY29uIi8+CgkJCUNvbnZlcnNpb25zIGVudHJlIGJhc2VzCgkJPC9hPgoJPC9kaXY+Cgk8ZGl2IGNsYXNzPSJibG9jIiBkYXRhLWRlc2NyaXB0aW9uPSJjb252ZXJ0aXNzZXVyIGQndW5pdMOpcyB1bml0w6lzIG1hdGjDqW1hdGlxdWUgcGh5c2lxdWUiPgoJCTxhIGhyZWY9InVuaXRlcy8iPgoJCQk8aW1nIHNyYz0idW5pdGVzL2ljb24ucG5nIiBhbHQ9Imljb24iLz4KCQkJQ29udmVydGlzc2V1cjxici8+ZOKAmXVuaXTDqXMKCQk8L2E+Cgk8L2Rpdj4KCTxkaXYgY2xhc3M9ImJsb2MiIGRhdGEtZGVzY3JpcHRpb249ImNvbnZlcnRpc3NldXIgbWF0aMOpbWF0aXF1ZXMgdW5pdMOpcyBudW3DqXJpcXVlIG9jdGVjdCBraWxvb2N0ZXQgbcOpZ2FvY3RldCI+CgkJPGEgaHJlZj0ibW8tbWlvLyI+CgkJCTxpbWcgc3JjPSJtby1taW8vaWNvbi5wbmciIGFsdD0iaWNvbiIvPgoJCQlVbml0w6lzIG51bcOpcmlxdWVzCgkJPC9hPgoJPC9kaXY+Cgk8aDI+R8OpbsOpcmF0ZXVycyBlbiB0b3V0IGdlbnJlPC9oMj4KCTxkaXYgY2xhc3M9ImJsb2MiIGRhdGEtZGVzY3JpcHRpb249ImfDqW7DqXJhdGV1ciBnw6luw6lyZXIgdW4gbm9tIGFsw6lhdG9pcmUgbWF0aMOpbWF0aXF1ZXMiPgoJCTxhIGhyZWY9InJhbmRvbS8iPgoJCQk8aW1nIHNyYz0icmFuZG9tL2ljb24ucG5nIiBhbHQ9Imljb24iLz4KCQkJR8OpbsOpcmF0ZXVyIGRlPGJyLz5ub21icmUmbmJzcDthbMOpYXRvaXJlCgkJPC9hPgoJPC9kaXY+Cgk8ZGl2IGNsYXNzPSJibG9jIiBkYXRhLWRlc2NyaXB0aW9uPSJnw6luw6lyYXRldXIgZGUgYmxhYmxhIHRyb24gaW5zdWx0b3Ryb24iPgoJCTxhIGhyZWY9InRyb24vIj4KCQkJPGltZyBzcmM9InRyb24vaWNvbi5wbmciIGFsdD0iaWNvbiIvPgoJCQlHw6luw6lyYXRldXI8YnIvPmRlIGJsYWJsYQoJCTwvYT4KCTwvZGl2PgoJPGRpdiBjbGFzcz0iYmxvYyIgZGF0YS1kZXNjcmlwdGlvbj0iZ8OpbsOpcmF0ZXVyIGfDqW7DqXJlciB1bmUgdkNhcmQgY29udGFjdCI+CgkJPGEgaHJlZj0idmNhcmQvIj4KCQkJPGltZyBzcmM9InZjYXJkL2ljb24ucG5nIiBhbHQ9Imljb24iLz4KCQkJR8OpbsOpcmF0ZXVyPGJyLz5kZSZuYnNwO3ZDYXJkCgkJPC9hPgoJPC9kaXY+Cgk8ZGl2IGNsYXNzPSJibG9jIiBkYXRhLWRlc2NyaXB0aW9uPSJyZXNzb3VyY2UgZGUgZmF1eCB0ZXh0ZSBsb3JlbSBpcHN1bSBnw6luw6lyYXRldXIiPgoJCTxhIGhyZWY9Imlwc3VtLyI+CgkJCTxpbWcgc3JjPSJpcHN1bS9pY29uLnBuZyIgYWx0PSJpY29uIi8+CgkJCUfDqW7DqXJhdGV1ciBkZTxici8+ZmF1eC10ZXh0ZQoJCTwvYT4KCTwvZGl2PgoJPGRpdiBjbGFzcz0iYmxvYyIgZGF0YS1kZXNjcmlwdGlvbj0iZ8OpbsOpcmF0ZXVyIG1hdGjDqW1hdGlxdWUgZ8OpbsOpcmVyIHVuIGNhcnLDqSBtYWdpcXVlIG5vbWJyZXMiPgoJCTxhIGhyZWY9Im1hZ2ljLyI+CgkJCTxpbWcgc3JjPSJtYWdpYy9pY29uLnBuZyIgYWx0PSJpY29uIi8+CgkJCUfDqW7DqXJhdGV1cjxici8+Y2FycsOpLW1hZ2lxdWUKCQk8L2E+Cgk8L2Rpdj4KCTxkaXYgY2xhc3M9ImJsb2MiIGRhdGEtZGVzY3JpcHRpb249ImfDqW7DqXJhdGV1ciBkZSB0b25hbGl0w6lzIHTDqWzDqXBob25lIG11c2lxdWUgc29uIGR0bWYgbXVzaXF1ZSI+CgkJPGEgaHJlZj0iZHRtZi8iPgoJCQk8aW1nIHNyYz0iZHRtZi9pY29uLnBuZyIgYWx0PSJpY29uIi8+CgkJCUfDqW7DqXJhdGV1cjxici8+ZGUgdG9uYWxpdMOpcwoJCTwvYT4KCTwvZGl2PgoJPGRpdiBjbGFzcz0iYmxvYyIgZGF0YS1kZXNjcmlwdGlvbj0iZ8OpbsOpcmF0ZXVyIGfDqW7DqXJlciB1biBndWlkIHVuaXF1ZSBpZCI+CgkJPGEgaHJlZj0iZ3VpZC8iPgoJCQk8aW1nIHNyYz0iZ3VpZC9pY29uLnBuZyIgYWx0PSJpY29uIi8+CgkJCUfDqW7DqXJhdGV1cjxici8+ZGUgR1VJRAoJCTwvYT4KCTwvZGl2PgoJPGRpdiBjbGFzcz0iYmxvYyIgZGF0YS1kZXNjcmlwdGlvbj0iZ8OpbsOpcmF0ZXVyIG1vdHMgbGFuZ3VlcyBsZXR0cmVzIHZvY2FidWxhaXJlIGZha2Ugd29yZHMgaW52ZW50ZXIiPgoJCTxhIGhyZWY9ImZha2Utd29yZHMvIj4KCQkJPGltZyBzcmM9ImZha2Utd29yZHMvaWNvbi5wbmciIGFsdD0iaWNvbiIvPgoJCQlHw6luw6lyYXRldXI8YnIvPmRlcyBtb3RzCgkJPC9hPgoJPC9kaXY+Cgk8aDI+UGhvdG9zICZhbXA7IGNvdWxldXJzPC9oMj4KCTxkaXYgY2xhc3M9ImJsb2MiIGRhdGEtZGVzY3JpcHRpb249IndlYmNhbSBwcmVuZHJlIHVuIHBob3RvIj4KCQk8YSBocmVmPSJ3ZWJjYW0vIj4KCQkJPGltZyBzcmM9IndlYmNhbS9pY29uLnBuZyIgYWx0PSJpY29uIi8+CgkJCVByZW5kcmUgdW5lIHBob3RvCgkJPC9hPgoJPC9kaXY+Cgk8ZGl2IGNsYXNzPSJibG9jIiBkYXRhLWRlc2NyaXB0aW9uPSJzw6lsZWN0ZXVyIGRlIGNvdWxldXJzIGh0bWwgaHNsIHJnYiBjb2xvciBwaWNrZXIiPgoJCTxhIGhyZWY9ImNvbG9yLyI+CgkJCTxpbWcgc3JjPSJjb2xvci9pY29uLnBuZyIgYWx0PSJpY29uIi8+CgkJCVPDqWxlY3RldXI8YnIvPmRlIGNvdWxldXIKCQk8L2E+Cgk8L2Rpdj4KCTxkaXYgY2xhc3M9ImJsb2MiIGRhdGEtZGVzY3JpcHRpb249InJldG91Y2hlciB1bmUgaW1hZ2UgcGhvdG8gZWZmZXRzIGpwZyBwbmciPgoJCTxhIGhyZWY9InRvc2hvcC8iPgoJCQk8aW1nIHNyYz0idG9zaG9wL2ljb24ucG5nIiBhbHQ9Imljb24iLz4KCQkJUmV0b3VjaGVyPGJyPnVuZSBpbWFnZQoJCTwvYT4KCTwvZGl2PgoJPGRpdiBjbGFzcz0iYmxvYyIgZGF0YS1kZXNjcmlwdGlvbj0icGhvdG8gdHJhbnNwYXJlbmNlIGFscGhhIHN1cHByaW1lciByZXRvdWNoZSBnaWYgcG5nIj4KCQk8YSBocmVmPSJhbHBoYS8iPgoJCQk8aW1nIHNyYz0iYWxwaGEvaWNvbi5wbmciIGFsdD0iaWNvbiIvPgoJCQlTdXBwcmltZXIgbGEgdHJhbnNwYXJlbmNlPGJyLz5k4oCZdW5lIGltYWdlCgkJPC9hPgoJPC9kaXY+Cgk8ZGl2IGNsYXNzPSJibG9jIiBkYXRhLWRlc2NyaXB0aW9uPSJjb252ZXJ0aXNzZXVyIGNhbGN1bGVyIGNvdWxldXJzIGRlcyByw6lzaXN0b3JzIHLDqXNpc3RhbmNlcyBwaHlzaXF1ZSBpbmZvcm1hdGlxdWUiPgoJCTxhIGhyZWY9InJlc2lzdG9yLyI+CgkJCTxpbWcgc3JjPSJyZXNpc3Rvci9pY29uLnBuZyIgYWx0PSJpY29uIi8+CgkJCUNvdWxldXJzIGRlczxici8+csOpc2lzdG9ycwoJCTwvYT4KCTwvZGl2PgoJPGgyPkRhdGVzICZhbXA7IGhldXJlczwvaDI+Cgk8ZGl2IGNsYXNzPSJibG9jIiBkYXRhLWRlc2NyaXB0aW9uPSJtYXRow6ltYXRpcXVlIGFkZGl0aW9ubmVyIGRlcyBkYXRlcyBjYWxlbmRyaWVyIj4KCQk8YSBocmVmPSJkYXRlcy8iPgoJCQk8aW1nIHNyYz0iZGF0ZXMvaWNvbi5wbmciIGFsdD0iaWNvbiIvPgoJCQlBZGRpdGlvbm5lcjxici8+ZGVzIGRhdGVzCgkJPC9hPgoJPC9kaXY+Cgk8ZGl2IGNsYXNzPSJibG9jIiBkYXRhLWRlc2NyaXB0aW9uPSJjYWxlbmRyaWVyIGR1IG1vaXMgam91cnMgYW5uw6llIGRhdGVzIj4KCQk8YSBocmVmPSJjYWxlbmRhci8iPgoJCQk8aW1nIHNyYz0iY2FsZW5kYXIvaWNvbi5wbmciIGFsdD0iaWNvbiIvPgoJCQlDYWxlbmRyaWVyPGJyLz5kdSBtb2lzCgkJPC9hPgoJPC9kaXY+Cgk8ZGl2IGNsYXNzPSJibG9jIiBkYXRhLWRlc2NyaXB0aW9uPSJnw6luw6lyYXRldXIgbWludXRldXIgYXZlYyBhbGFybWUgc29uIG11c2lxdWUgZmljaGllcnMiPgoJCTxhIGhyZWY9InRpbWVyLyI+CgkJCTxpbWcgc3JjPSJ0aW1lci9pY29uLnBuZyIgYWx0PSJpY29uIi8+CgkJCU1pbnV0ZXVyPGJyLz5hdmVjIGFsYXJtZQoJCTwvYT4KCTwvZGl2PgoJPGRpdiBjbGFzcz0iYmxvYyIgZGF0YS1kZXNjcmlwdGlvbj0iYXZleiB2b3VzIDFHcyBnaWdhc2Vjb25kZSB0ZW1wcyB1bml0w6kiPgoJCTxhIGhyZWY9ImdpZ2Etc2Vjb25kLyI+CgkJCTxpbWcgc3JjPSJnaWdhLXNlY29uZC9pY29uLnBuZyIgYWx0PSJpY29uIi8+CgkJCUF2ZXotdm91czxici8+MSZuYnNwO0dzJm5ic3A7PwoJCTwvYT4KCTwvZGl2PgoJPGRpdiBjbGFzcz0iYmxvYyIgZGF0YS1kZXNjcmlwdGlvbj0iaGV1cmUgZGF0ZSBwbGFuw6h0ZSBtYXJzIGp1cGl0ZXIgc3lzdMOobWUgc29sYWlyZSBjYWxlbmRyaWVyIj4KCQk8YSBocmVmPSJwbGFuZXRzLXRpbWUvIj4KCQkJPGltZyBzcmM9InBsYW5ldHMtdGltZS9pY29uLnBuZyIgYWx0PSJpY29uIi8+CgkJCVF1ZWxsZSBoZXVyZTxici8+c3VyIE1hcnMmbmJzcDs/CgkJPC9hPgoJPC9kaXY+Cgk8ZGl2IGNsYXNzPSJibG9jIiBkYXRhLWRlc2NyaXB0aW9uPSJoZXVyZSBkYXRlIHBsYW7DqHRlIG1hcnMganVwaXRlciBzeXN0w6htZSBzb2xhaXJlIGNhbGVuZHJpZXIiPgoJCTxhIGhyZWY9ImRheS8iPgoJCQk8aW1nIHNyYz0iZGF5L2ljb24ucG5nIiBhbHQ9Imljb24iLz4KCQkJUXVlbCBqb3VyIMOpdGFpdC1pbCBsZSDigKYgPwoJCTwvYT4KCTwvZGl2PgoJPGRpdiBjbGFzcz0iYmxvYyIgZGF0YS1kZXNjcmlwdGlvbj0iaGV1cmUgam91ciBkYXRlIHByb2dyZXNzaW9uIGFubsOpZSB0ZW1wcyBob3Jsb2dlIHBvdXJjZW50YWdlIj4KCQk8YSBocmVmPSJwcm9ncmVzc2lvbi1jYWxlbmRhci8iPgoJCQk8aW1nIHNyYz0icHJvZ3Jlc3Npb24tY2FsZW5kYXIvaWNvbi5wbmciIGFsdD0iaWNvbiIvPgoJCQlM4oCZaG9ybG9nZSBlbjxici8+cG91cmNlbnRhZ2UKCQk8L2E+Cgk8L2Rpdj4KCTxoMj5Qcm9ncmFtbWF0aW9uPC9oMj4KCTxkaXYgY2xhc3M9ImJsb2MiIGRhdGEtZGVzY3JpcHRpb249ImNhbGN1bGVyIHVuZSBjaGVja3N1bSBpbmZvcm1hdGlxdWUgZmljaGllciBpbWFnZSBtZDUgc2hhMSBzaGEiPgoJCTxhIGhyZWY9ImNoZWNrc3VtLyI+CgkJCTxpbWcgc3JjPSJjaGVja3N1bS9pY29uLnBuZyIgYWx0PSJpY29uIi8+CgkJCUNhbGN1bGVyIHVuZTxici8+Y2hlY2tzdW0KCQk8L2E+Cgk8L2Rpdj4KCTxkaXYgY2xhc3M9ImJsb2MiIGRhdGEtZGVzY3JpcHRpb249ImfDqW7DqXJhdGV1ciBpbWFnZXIgdW5lIHJlZ2V4IGluZm9ybWF0aXF1ZSI+CgkJPGEgaHJlZj0icmVnZXgvIj4KCQkJPGltZyBzcmM9InJlZ2V4L2ljb24ucG5nIiBhbHQ9Imljb24iLz4KCQkJSW1hZ2VyPGJyLz51bmUgUmVnZXgKCQk8L2E+Cgk8L2Rpdj4KCTxkaXYgY2xhc3M9ImJsb2MiIGRhdGEtZGVzY3JpcHRpb249ImNhbGN1bGVyIHVuIGNobW9kIG1vZGUgdW5peCBsaW51eCA3Nzcgcnd4cnd4cnd4Ij4KCQk8YSBocmVmPSJjaG1vZC8iPgoJCQk8aW1nIHNyYz0iY2htb2QvaWNvbi5wbmciIGFsdD0iaWNvbiIvPgoJCQlDYWxjdWxlcjxicj51biBjaG1vZAoJCTwvYT4KCTwvZGl2PgoJPGRpdiBjbGFzcz0iYmxvYyIgZGF0YS1kZXNjcmlwdGlvbj0iaW5mb3JtYXRpcXVlIHRhYmxlIGRlcyBjYXJhY3TDqHJlcyBnw6luw6lyYXRldXIgY2hhcm1hcCBjaGFyYWN0ZXIgdW5pY29kZSI+CgkJPGEgaHJlZj0iY2hhcm1hcC8iPgoJCQk8aW1nIHNyYz0iY2hhcm1hcC9pY29uLnBuZyIgYWx0PSJpY29uIi8+CgkJCVRhYmxlIGRlczxici8+Y2FyYWN0w6hyZXMKCQk8L2E+Cgk8L2Rpdj4KCTxkaXYgY2xhc3M9ImJsb2MiIGRhdGEtZGVzY3JpcHRpb249InZhbGlkYXRldXIgZW1haWwgdmFsaWRlciB2w6lyaWZpZXIgdW5lIGFkcmVzc2UgbWFpbCI+CgkJPGEgaHJlZj0icmZjLXZhbGlkLyI+CgkJCTxpbWcgc3JjPSJyZmMtdmFsaWQvaWNvbi5wbmciIGFsdD0iaWNvbiIvPgoJCQlWYWxpZGVyIHVuZSBlbWFpbAoJCTwvYT4KCTwvZGl2PgoJPGgyPkpldXg8L2gyPgoJPGRpdiBjbGFzcz0iYmxvYyIgZGF0YS1kZXNjcmlwdGlvbj0iam91ZXIgw6AgMjA0OCBqZXV4IGluZm9ybWF0aXF1ZSI+CgkJPGEgaHJlZj0iMjA0OC8iPgoJCQk8aW1nIHNyYz0iMjA0OC9pY29uLnBuZyIgYWx0PSJpY29uIi8+CgkJCUpvdWVyIMOgPGJyPjIwNDgKCQk8L2E+Cgk8L2Rpdj4KCTxkaXYgY2xhc3M9ImJsb2MiIGRhdGEtZGVzY3JpcHRpb249ImpvdWVyIMOgIHRldHJpcyB0w6l0cmlzIGpldXggaW5mb3JtYXRpcXVlIj4KCQk8YSBocmVmPSJ0ZXRyaXMvIj4KCQkJPGltZyBzcmM9InRldHJpcy9pY29uLnBuZyIgYWx0PSJpY29uIi8+CgkJCUpvdWVyIMOgPGJyPlRldHJpcwoJCTwvYT4KCTwvZGl2PgoJPGRpdiBjbGFzcz0iYmxvYyIgZGF0YS1kZXNjcmlwdGlvbj0iY2hpbWllIHRhYmxlYXUgcMOpcmlvZGlxdWUgbWVuZGVsw6lpw6h2IGpldXgiPgoJCTxhIGhyZWY9InBlcmlvZGljLyI+CgkJCTxpbWcgc3JjPSJwZXJpb2RpYy9pY29uLnBuZyIgYWx0PSJpY29uIi8+CgkJCVRhYmxlYXUgcMOpcmlvZGlxdWUKCQk8L2E+Cgk8L2Rpdj4KCTxoMj5EaXZlcnM8L2gyPgoJPGRpdiBjbGFzcz0iYmxvYyIgZGF0YS1kZXNjcmlwdGlvbj0iaW5mb3JtYXRpb25zIHZvdHJlIG5hdmlnYXRldXIgaW5mb3JtYXRpcXVlIj4KCQk8YSBocmVmPSJicm93c2VyLyI+CgkJCTxpbWcgc3JjPSJicm93c2VyL2ljb24ucG5nIiBhbHQ9Imljb24iLz4KCQkJSW5mb3JtYXRpb25zIGRlPGJyLz52b3RyZSBuYXZpZ2F0ZXVyCgkJPC9hPgoJPC9kaXY+Cgk8ZGl2IGNsYXNzPSJibG9jIiBkYXRhLWRlc2NyaXB0aW9uPSJzcGVlZHRlc3QgdGVzdCBkZSBjb25uZXhpb24gYWRzbCBmaWJyZSI+CgkJPGEgaHJlZj0ic3BlZWR0ZXN0LyI+CgkJCTxpbWcgc3JjPSJzcGVlZHRlc3QvaWNvbi5wbmciIGFsdD0iaWNvbiIvPgoJCQlUZXN0ZXI8YnIvPnZvdHJlIGNvbm5leGlvbgoJCTwvYT4KCTwvZGl2PgoJPCEtLQk8ZGl2IGNsYXNzPSJibG9jIj4KCQk8YSBocmVmPSJkbC8iPgoJCQk8aW1nIHNyYz0iZGwvaWNvbi5wbmciIGFsdD0iaWNvbiIvPgoJCQlUw6lsw6ljaGFyZ2VyPGJyLz51bmUgcGFnZQoJCTwvYT4KCTwvZGl2Pi0tPgoJPGRpdiBjbGFzcz0iYmxvYyIgZGF0YS1kZXNjcmlwdGlvbj0idHJhY2VyIHVuIGdyYXBoaXF1ZSBtYXRow6ltYXRpcXVlIGfDqW7DqXJhdGV1ciI+CgkJPGEgaHJlZj0iZ3JhcGgvIj4KCQkJPGltZyBzcmM9ImdyYXBoL2ljb24ucG5nIiBhbHQ9Imljb24iLz4KCQkJVHJhY2VyPGJyPnVuIGdyYXBoaXF1ZQoJCTwvYT4KCTwvZGl2PgoJPGRpdiBjbGFzcz0iYmxvYyIgZGF0YS1kZXNjcmlwdGlvbj0iZm9uY3Rpb25zIHRyaWdvbm9tZXRyaWUgdHJpZ29ub23DqXRyaXF1ZXMgbWF0aMOpbWF0aXF1ZSBncmFwaGlxdWUgc2ludXMgY29zaW51cyI+CgkJPGEgaHJlZj0idHJpZ29ub21ldHJpZS8iPgoJCQk8aW1nIHNyYz0idHJpZ29ub21ldHJpZS9pY29uLnBuZyIgYWx0PSJpY29uIi8+CgkJCUxlcyBmb25jdGlvbnM8YnI+dHJpZ29ub23DqXRyaXF1ZXMKCQk8L2E+Cgk8L2Rpdj4KCTxkaXYgY2xhc3M9ImJsb2MiIGRhdGEtZGVzY3JpcHRpb249IlByb2R1Y3Rpb24gw6lsZWN0cmlxdWUgw6luZXJnaWUgZW4gRnJhbmNlIGNvbnNvbW1hdGlvbiDDqWxlY3RyaWNpdMOpIHN0YXRpc3RpcXVlcyI+CgkJPGEgaHJlZj0iY29uc28tZW4tZnJhbmNlLyI+CgkJCTxpbWcgc3JjPSJjb25zby1lbi1mcmFuY2UvaWNvbi5wbmciIGFsdD0iaWNvbiIvPgoJCQlQcm9kdWN0aW9uIMOpbGVjdHJpcXVlPGJyPmVuIEZyYW5jZQoJCTwvYT4KCTwvZGl2PgoJPGRpdiBjbGFzcz0iYmxvYyIgZGF0YS1kZXNjcmlwdGlvbj0iUGFydGFnZXIgZGVzIGTDqXBlbnNlcyBzaGFyZSBjb3N0cyBhcmdlbnQiPgoJCTxhIGhyZWY9InBheS1iaWxsLyI+CgkJCTxpbWcgc3JjPSJwYXktYmlsbC9pY29uLnBuZyIgYWx0PSJpY29uIi8+CgkJCVBhcnRhZ2VyIGRlczxicj5kw6lwZW5zZXMgZOKAmWFtaXMKCQk8L2E+Cgk8L2Rpdj4KCTxkaXYgY2xhc3M9ImJsb2MiIGRhdGEtZGVzY3JpcHRpb249Ik11ciBkZSBub3Rlcywgbm90ZXBhZCwgcG9zdC1pdCwgbm90ZXMiPgoJCTxhIGhyZWY9Im5vdGVzLXdhbGwvIj4KCQkJPGltZyBzcmM9Im5vdGVzLXdhbGwvaWNvbi5wbmciIGFsdD0iaWNvbiIvPgoJCQlVbiBtdXI8YnIvPmRlIG5vdGVzCgkJPC9hPgoJPC9kaXY+Cgk8ZGl2IGNsYXNzPSJibG9jIiBkYXRhLWRlc2NyaXB0aW9uPSJNdXIgZGUgbm90ZXMsIG5vdGVwYWQsIHBvc3QtaXQsIG5vdGVzIj4KCQk8YSBocmVmPSJwb3N0LWl0LyI+CgkJCTxpbWcgc3JjPSJwb3N0LWl0L2ljb24ucG5nIiBhbHQ9Imljb24iLz4KCQkJVW4gYmxvYyBub3RlPGJyPmVuIHBvc3QtaXQKCQk8L2E+Cgk8L2Rpdj4KCTxkaXYgY2xhc3M9ImJsb2MiIGRhdGEtZGVzY3JpcHRpb249InlvdXR1YmUgcnNzIGF0b20gZmx1eCI+CgkJPGEgaHJlZj0ieW91dHViZS1yc3MvIj4KCQkJPGltZyBzcmM9InlvdXR1YmUtcnNzL2ljb24ucG5nIiBhbHQ9Imljb24iLz4KCQkJUsOpY3Vww6lyZXIgdW4gZmx1eCBSU1MgWW91dHViZQoJCTwvYT4KCTwvZGl2PgoJPGRpdiBjbGFzcz0iYmxvYyIgZGF0YS1kZXNjcmlwdGlvbj0idHJvdSBub2lyIGJsYWNrIGhvbGUgaGF3a2luZyByYWRpYXRpb24gbWFzc2Ugw6luZXJnaWUiPgoJCTxhIGhyZWY9ImJsYWNraG9sZS8iPgoJCQk8aW1nIHNyYz0iYmxhY2tob2xlL2ljb24ucG5nIiBhbHQ9Imljb24iLz4KCQkJQ2FsY3VsYXRldXIgZGUgdHJvdSBub2lyCgkJPC9hPgoJPC9kaXY+Cgk8aDI+w4ljcmFucyBkZSB2ZWlsbGU8L2gyPgoJPGRpdiBjbGFzcz0iYmxvYyIgZGF0YS1kZXNjcmlwdGlvbj0icXVlbGxlIGNvdWxldXIgZXN0IGlsIGltYWdlcyI+CgkJPGEgaHJlZj0iY29sb3Itc2Vjb25kLyI+CgkJCTxpbWcgc3JjPSJjb2xvci1zZWNvbmQvaWNvbi5wbmciIGFsdD0iaWNvbiIvPgoJCQlRdWVsbGUgY291bGV1cjxici8+ZXN0LWlsJm5ic3A7PwoJCTwvYT4KCTwvZGl2PgoJPGRpdiBjbGFzcz0iYmxvYyIgZGF0YS1kZXNjcmlwdGlvbj0ibWF0cml4IGNvZGUgcmFpbiBwbHVpZSBqYXBvbmFpcyI+CgkJPGEgaHJlZj0ibWF0cml4LyI+CgkJCTxpbWcgc3JjPSJtYXRyaXgvaWNvbi5wbmciIGFsdD0iaWNvbiIvPgoJCQlNYXRyaXg8YnIvPmNvZGUgcmFpbgoJCTwvYT4KCTwvZGl2Pgo="); // Copied Just The List (Because Too Loong) ::::::::::::::: https://github.com/timovn/MyWebTools/blob/master/index.php
}
if ($_SERVER["HTTP_HOST"] == $freedomaines[10])
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
if ($_SERVER["HTTP_HOST"] == $freedomaines[11])
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
if ($_SERVER["HTTP_HOST"] == $freedomaines[12])
{
echo "<head><title>LogicEmu - Online Logic Simulator</title></head>";
echo "<body><noscript>Please Enable Javascript!</noscript>";
echo "<script src=\"logicemu.js\"></script>";
echo "<script src=\"main.js\"></script>";
echo "<script src=\"circuits_help.js\"></script>";
echo "<script src=\"circuits_articles.js\"></script>";
echo "<script src=\"circuits_main.js\"></script>";
echo "<script src=\"footer.js\"></script>";
echo "<script type='text/javascript'>var c = origtext.replace(\"\\\"[^\\\"]*\\\"\",'');var icd = (c.split('I')).length-1;var ic = (c.split('i')).length-1;\n";
echo "var logici = 0;var logici = logici + (c.split('a')).length-1;var logici = logici + (c.split('e')).length-1;var logici = logici + (c.split('o')).length-1;var logici = logici + (c.split('h')).length-1;var logici = logici + (c.split('z')).length-1;\n";
echo "var logicinv = 0;var logicinv = logicinv + (c.split('A')).length-1;var logicinv = logicinv + (c.split('E')).length-1;var logicinv = logicinv + (c.split('O')).length-1;var logicinv = logicinv + (c.split('H')).length-1;var logicinv = logicinv + (c.split('Z')).length-1;\n";
echo "var inputi = 0;var inputi = inputi + (c.split('^')).length-1;var inputi = inputi + (c.split('v')).length-1;var inputi = inputi + (c.split('<')).length-1;var inputi = inputi + (c.split('>')).length-1;\n";
echo "var inputinv = 0;var inputinv = inputinv + (c.split('m')).length-1;var inputinv = inputinv + (c.split('w')).length-1;var inputinv = inputinv + (c.split('[')).length-1;var inputinv = inputinv + (c.split(']')).length-1;\n";
echo "var led = 0;var led = led + (c.split('l')).length-1;var led = led + (c.split('L')).length-1;\n";
echo "var memory = 0;var memory = memory + (c.split('b')).length-1;var memory = memory + (c.split('B')).length-1;\n";
echo "var kinetic = (c.split('K')).length-1;var alu = (c.split('U')).length-1;var termi = (c.split('T')).length-1;var matrix = (c.split('D')).length-1;var quartz = (c.split('t')).length-1;\n";
echo "var switchy = 0;var switchy = switchy + (c.split('s')).length-1;var switchy = switchy + (c.split('\\S')).length-1;var switchy = switchy + (c.split('p')).length-1;var switchy = switchy + (c.split('P')).length-1;\n";
echo "var pist = Math.abs((((alu%11) + (logici - logicinv)) * Math.floor(ic/(icd+1))) + (termi%3) + ((switchy*2)+(led*3)) + (matrix%7) + (quartz%5) + (inputi - inputinv) + (memory % 17) - kinetic)%16;\n";
echo "var tracks = ['LUXAR__Stephane_Marty__01_Birth.mp3','LUXAR__Stephane_Marty__02_First_steps.mp3','LUXAR__Stephane_Marty__03_Curiosity.mp3','LUXAR__Stephane_Marty__04_Process.mp3','LUXAR__Stephane_Marty__05_Free_will.mp3','LUXAR__Stephane_Marty__06_Scar.mp3','LUXAR__Stephane_Marty__07_Loneliness.mp3','LUXAR__Stephane_Marty__08_Explorer.mp3','LUXAR__Stephane_Marty__09_Chase.mp3','LUXAR__Stephane_Marty__10_Revolution.mp3','LUXAR__Stephane_Marty__11_Blooming.mp3','LUXAR__Stephane_Marty__12_Torment.mp3','LUXAR__Stephane_Marty__13_Awareness.mp3','LUXAR__Stephane_Marty__14_Self-confidence.mp3','LUXAR__Stephane_Marty__15_Ambition.mp3','LUXAR__Stephane_Marty__16_Responsability.mp3'];\n";
echo "document.write(\"<audio autoplay hidden loop><source src='\"+tracks[pist]+\"'></audio>\");</script>";
echo "<script src=\"editor.js\"></script></body>";
}
if ($_SERVER["HTTP_HOST"] == $freedomaines[13])
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
if ($_SERVER["HTTP_HOST"] == $freedomaines[14])
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
if ($_SERVER["HTTP_HOST"] == $freedomaines[15])
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
?>
