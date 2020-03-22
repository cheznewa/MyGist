<?php
if (!isset($argv[1]))
{
$argv[1] = time();
}
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
echo getdatebt(intval(($argv[1] - 989193600) / 86400))." ".gettimeday(($argv[1] - 18000) % 86400)."\n";
