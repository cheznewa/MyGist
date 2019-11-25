<?php
// Debug De Config
$nbballdef = 30;
$tiragedef = 5;
$time = 150;
// Fin De Config
$numero = 1;
while (false !== ($o = fread(STDIN,$tiragedef)))
{
echo "numero set_text \"N" . $numero ."\"\n";
for ($e = 0;$e < $time;$e++)
{
$p = 1-($e/floatval($time));
$p = str_replace(".",",",strval($p));
echo "time set_fraction \"". $p . "\"\n";
echo "time set_text \"" . strval($time - $e) ."\"\n";
sleep(1);
}
echo "tirage set_text \"";
$nbball = $nbballdef;
$balls = range(1,$nbballdef);
for ($g = 0;$g < $tiragedef;$g++)
{
$tired = intval($nbball*(ord($o[$g])/256));
echo $balls[$tired]." ";
array_splice($balls,$tired,1);
$nbball = $nbball - 1;
}
echo "\"\n";
for ($e = 0;$e < $time;$e++)
{
$p = $e/floatval($time);
$p = str_replace(".",",",strval($p));
echo "time set_fraction \"". $p . "\"\n";
echo "time set_text \"" . strval($e) ."\"\n";
sleep(0.02);
}
$numero = $numero +1;
}