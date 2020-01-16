<?php
$a = strval(sprintf("%08b",intval($argv[3])));
$ac = str_replace("0","c",$a);
$as = str_replace("1","C",$ac);
$as = strrev($as);
$b = strval(sprintf("%08b",intval($argv[4])));
$bc = str_replace("0","c",$b);
$bs = str_replace("1","C",$bc);
$bs = strrev($bs);
echo " s s s s s s s s s s s s s s s s s s s s s s s s \n | | | | | | | | | | | | | | | | | | | | | | | |";
for ($l = 0;$l < intval($argv[1]);$l++)
{
echo "\n";
$mat = array_fill(0,32,null);
for ($a = 0;$a < 24;$a++)
{
$mat[$a] = ord(fgetc(STDIN));
}
for ($m = 0;$m < 24;$m++)
{
echo $mat[$m] > 32 ? " ." : " v";
}
echo "\n";
for ($m = 0;$m < 24;$m++)
{
echo $mat[$m] > 32 ? " ." : ">E";
}
}
for ($l = 0;$l < intval($argv[2]);$l++)
{
echo "\n";
$mat = array_fill(0,32,null);
for ($a = 0;$a < 24;$a++)
{
$mat[$a] = ord(fgetc(STDIN));
}
for ($m = 0;$m < 24;$m++)
{
echo $mat[$m] > 32 ? " ." : " v";
}
echo "\n";
for ($m = 0;$m < 24;$m++)
{
echo $mat[$m] > 32 ? " ." : ">e";
}
}
echo "\n | | | | | | | | | | | | | | | | | | | | | | | |".$as.$bs."\n v v v v v v v v v v v v v v v v v v v v v v v vvvvvvvvvvvvvvvvv\n l l l l l l l l l l l l l l l l l l l l l l l lllllllllllllllllI";
$id = bin2hex(fread(STDIN,32));
echo "\n0\"VideoCrypt ID : " . $id ."\n";
echo "ssssssssssssssssssssssss\nvvvvvvvvvvvvvvvvvvvvvvvv\n##########################################\n#########################################i\nvvvvvvvvvvvvvvvvvvvvvvvv vvvvvvvv vvvvvvvv\nTTTTTTTTTTTTTTTTTTTTTTTT TTTTTTTT TTTTTTTT";
