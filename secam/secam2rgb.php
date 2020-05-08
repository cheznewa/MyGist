<?php
$m = 0;
$l = 0;
$v = 0;
$u = true;
$one = 0;
$two = 0;
$line = $argv[1];
$yc = array_fill(0,$line,0);
$uc = array_fill(0,$line,0);
$vc = array_fill(0,$line,0);
$b = array_fill(0,$line,0);
$final = array_fill(0,3,0);
function yuv2rgb($color)
{
$rgb = array_fill(0,3,0);
$rgb[0] = abs($color[0] + 1.4075 * ($color[2] - 128));
$rgb[1] = abs($color[0] - 0.3455 * ($color[1] - 128) - (0.7169 * ($color[2] - 128)));
$rgb[2] = abs($color[0] + 1.7790 * ($color[1] - 128));
return $rgb;
}
while ($u)
{
for ($r = 0;$r < $line;$r++){$b[$r] = fgetc(STDIN);}
for ($n = 0;$n < $line;$n++)
{
switch ($m % 2)
{
case 0:
$one = ord($b[$n]);
break;
case 1:
$two = ord($b[$n]);
break;
}
$subcarr = $two - $one;
$carrier = $m % 2 ? ord($b[$n]) - $subcarr : ord($b[$n]);
switch ($l % 2)
{
case 0:
$u = 256*($subcarr/128);
$uc[$n] = $u;
break;
case 1:
$v = 256*($subcarr/128);
$vc[$n] = $v;
break;
}
$y = 256*($carrier/128);
$yc[$n] = $y;
$m = $m + 1;
}
for ($x = 0;$x < $line;$x++)
{ 
$final = yuv2rgb([$yc[$x],$uc[$x],$vc[$x]]);
if ($final[0] > 256){$final[0]=255-$final[0];}
if ($final[1] > 256){$final[1]=255-$final[1];}
if ($final[2] > 256){$final[2]=255-$final[2];}
echo chr($final[0]).chr($final[1]).chr($final[2]);
}
$l = $l + 1;
if (feof(STDIN)){$u = false;}
}