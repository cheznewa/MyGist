<?php
$note = [1,3,4,5,7,8,9,0];
while (false !== ($o = fgetc(STDIN)))
{
$gray = intval((ord($o) / 256)*64);
echo $note[intval($gray/8)].$note[intval($gray%8)];
}
