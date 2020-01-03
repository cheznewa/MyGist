<?php
$note = [1,3,4,5,7,8,9,0];
while ($o = fread(STDIN,2))
{
$gray = 4*((8*array_search($o[0],$note))+array_search($o[1],$note));
echo chr($gray);
}
