<?php
$note = [1,3,4,5,7,8,9,0];
while (false !== ($o = fgetc(STDIN)))
{
$c = ord($o)*2;
$div = intval($c / 64);
$mod = intval($c % 64);
echo $note[$div];
$div = intval($mod / 8);
echo $note[$div];
$mod = intval($mod % 8);
echo $note[$mod];
}