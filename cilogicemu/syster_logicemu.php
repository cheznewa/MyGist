<?php
echo "s s s s s s s s s s s s s s s s s s s s s s s s \n| | | | | | | | | | | | | | | | | | | | | | | |I1";
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
echo $mat[$m] > 32 ? "* " : "v ";
}
echo "\n";
for ($m = 0;$m < 24;$m++)
{
echo $mat[$m] > 32 ? "* " : "E<";
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
echo $mat[$m] > 32 ? "* " : "v ";
}
echo "\n";
for ($m = 0;$m < 24;$m++)
{
echo $mat[$m] > 32 ? "* " : "e<";
}
}
echo "\n                  | | | | | | | | | | | | | | |\n                  v v v v v v v v v v v v v v v\n                  l l l l l l l l l l l l l l l";
echo "\n\n";
echo "s s s s s s s s s s s s s s s s s s s s s s s s \n| | | | | | | | | | | | | | | | | | | | | | | |I2";
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
echo $mat[$m] > 32 ? "* " : "v ";
}
echo "\n";
for ($m = 0;$m < 24;$m++)
{
echo $mat[$m] > 32 ? "* " : "E<";
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
echo $mat[$m] > 32 ? "* " : "v ";
}
echo "\n";
for ($m = 0;$m < 24;$m++)
{
echo $mat[$m] > 32 ? "* " : "e<";
}
}
echo "\n                  | | | | | | | | | | | | | | |\n                  v v v v v v v v v v v v v v v\n                  l l l l l l l l l l l l l l l";
if ($argv[3] == "1")
{
$t = "c";
}
if ($argv[3] == "2")
{
$t = "C";
}
$id = bin2hex(fread(STDIN,32));
echo "\n0\"Nagravision Syster ID : " . $id ."\n";
echo $argv[4] ? $t." ssssssssssssssssssssssss\n| ||||||||||||||||||||||||\n| 012345678901234567890123                                \n| 000000000011111111112222                                \n| ========================================================\n| 012345678901234567890123        012345678901234567890123\n| 000000000011111111112222        000000000011111111112222\n| vvvvvvvvvvvvvvvvvvvvvvvv        vvvvvvvvvvvvvvvvvvvvvvvv\n| ######################i1        ######################i2\nv vvvvvvvv vvvvvvv                vvvvvvvv vvvvvvv\nl llllllll lllllll                llllllll lllllll" :
                $t." ssssssssssssssssssssssss\n| ||||||||||||||||||||||||\n| 012345678901234567890123                                \n| 000000000011111111112222                                \n| ========================================================\n| 012345678901234567890123        012345678901234567890123\n| 000000000011111111112222        000000000011111111112222\n| vvvvvvvvvvvvvvvvvvvvvvvv        vvvvvvvvvvvvvvvvvvvvvvvv\n| ######################i1        ######################i1\nv vvvvvvvv vvvvvvv                vvvvvvvv vvvvvvv\nl llllllll lllllll                llllllll lllllll";
