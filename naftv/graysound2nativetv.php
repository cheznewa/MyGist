<?php
$fs = fopen($argv[1],"rb");
$fps = intval($argv[2]);
$sample = intval($argv[3]);
$size = $argv[4];
$note = [1,3,4,5,7,8,9,0];
$q = $sample/$fps;
$siza = explode("x",$size);
$p = $q/intval($siza[1]);
while ($o = fread(STDIN,intval($siza[0])))
{
for ($n = 0;$n < intval($siza[0]);$n++)
{
$gray = intval((ord($o[$n]) / 256)*64);
echo $note[intval($gray/8)].$note[intval($gray%8)];
}
$e = fread($fs,intval($p));
for ($n = 0;$n < intval($p);$n++)
{
$r = intval((ord($e[$n]) / 256)*64);
echo $note[intval($r/8)].$note[intval($r%8)];
}
}
