<?php
$m = 0;
$line = $argv[1];
$final = array_fill(0,3,0);
function rgb2yuv($color)
{
$yuv = array_fill(0,3,0);
$yuv[0] = $color[0] *  .299000 + $color[1] *  .587000 + $color[2] *  .114000;
$yuv[1] = $color[0] * -.168736 + $color[1] * -.331264 + $color[2] *  .500000 + 128;
$yuv[2] = $color[0] *  .500000 + $color[1] * -.418688 + $color[2] * -.081312 + 128;
return $yuv;
}
while ($o = fread(STDIN,3))
{
$final = rgb2yuv([ord($o[0]),ord($o[1]),ord($o[2])]);
$y = ($final[0] / 256)*128;
switch (intval($m/$line) % 2)
{
case 0:
$p = $m % 2 ? (($final[1]/256)*128) + $y : $y;
break;
case 1:
$p = $m % 2 ? (($final[2]/256)*128) + $y : $y;
break;
}
echo chr($p);
$m = $m + 1;
}