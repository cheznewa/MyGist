<?php
// Je Vais Faire De La Magie Avec ::::::::::::::: https://github.com/jweslley/localtld
// Ou Fois Installer, Faite La Commande :::::: LOCALTLD=free _browser_
// Pour Commencé :::::::::::::::: [freelinks.free](http://freelinks.free)
// Et Accrochez-Vous !
// Mettez Ce Fichier Sur Votre Serveur Et Rennomé En index.php
$freedomaines = ["newanotremaitre.free","timeanddatebletou.free","logicemu.free","jslinux.free"];
if ($_SERVER["HTTP_HOST"] == "freelinks.free")
{
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
echo "<script src=\"editor.js?\"></script>";
echo "<script src=\"logicemu.js\"></script>";
echo "<script src=\"main.js\"></script>";
echo "<script src=\"circuits_help.js\"></script>";
echo "<script src=\"circuits_articles.js\"></script>";
echo "<script src=\"circuits_main.js\"></script>";
echo "<script src=\"footer.js\"></script>";
}
if ($_SERVER["HTTP_HOST"] == $freedomaines[3])
{
echo "<style>.term{font-family:monospace;color:white;background-color:black;}.termReverse{color:black;background-color:white;}</style>";
echo "<body onload=\"start()\">";
echo "<script src=\"term.js\"></script>";
echo "<script src=\"jslinux.js\"></script>";
echo "<script src=\"utils.js\"></script>";
echo "<script src=\"cpux86-ta.js\"></script>";
}
?>
