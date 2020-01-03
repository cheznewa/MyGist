<?php
$fs = fopen($argv[1],"wb");
$fps = intval($argv[2]);
$sample = intval($argv[3]);
$size = $argv[4];
$note = [1,3,4,5,7,8,9,0];
$q = $sample/$fps;
$siza = explode("x",$size);
$p = $q/intval($siza[1]);
while ($o = fread(STDIN,(intval($siza[0])+$p)*2))
{
for ($n = 0;$n < intval($siza[0]);$n++)
{
$gray = 4*((8*array_search($o[($n*2)],$note))+array_search($o[($n*2)+1],$note));
echo chr($gray);
}
for ($n = intval($siza[0]);$n < intval($siza[0])+intval($p);$n++)
{
$d = 4*((8*array_search($o[$n*2],$note))+array_search($o[($n*2)+1],$note));
fwrite($fs,chr($d));
}
}