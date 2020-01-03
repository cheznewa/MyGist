<?php
$note = [1,3,4,5,7,8,9,0];
while ($o = fread(STDIN,3))
{
$deca = (array_search($o[0],$note)) * 64;
$decb = (array_search($o[1],$note)) * 8;
$decc = (array_search($o[2],$note));
$c = intval(($deca + $decb + $decc) / 2);
echo chr($c);
}