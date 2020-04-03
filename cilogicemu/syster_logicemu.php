<?php
echo " s s s s s s s s s s s s s s s\n | | | | | | | | | | | | | | |I1";
for ($l = 0;$l < intval($argv[1]);$l++)
{
echo "\n";
$mat = array_fill(0,32,null);
for ($a = 0;$a < 15;$a++)
{
$mat[$a] = ord(fgetc(STDIN));
}
for ($m = 0;$m < 15;$m++)
{
echo $mat[$m] > 50 ? " ." : " v";
}
echo "\n";
for ($m = 0;$m < 15;$m++)
{
echo $mat[$m] > 50 ? " ." : ">E";
}
}
for ($l = 0;$l < intval($argv[2]);$l++)
{
echo "\n";
$mat = array_fill(0,32,null);
for ($a = 0;$a < 15;$a++)
{
$mat[$a] = ord(fgetc(STDIN));
}
for ($m = 0;$m < 15;$m++)
{
echo $mat[$m] > 50 ? " ." : " v";
}
echo "\n";
for ($m = 0;$m < 15;$m++)
{
echo $mat[$m] > 50 ? " ." : ">e";
}
}
echo "\n | | | | | | | | | | | | | | |\n v v v v v v v v v v v v v v v\n l l l l l l l l l l l l l l l";
if ($argv[4])
{
echo "\n\n";
echo " s s s s s s s s s s s s s s s\n | | | | | | | | | | | | | | |I2";
for ($l = 0;$l < intval($argv[1]);$l++)
{
echo "\n";
$mat = array_fill(0,32,null);
for ($a = 0;$a < 15;$a++)
{
$mat[$a] = ord(fgetc(STDIN));
}
for ($m = 0;$m < 15;$m++)
{
echo $mat[$m] > 50 ? " ." : " v";
}
echo "\n";
for ($m = 0;$m < 15;$m++)
{
echo $mat[$m] > 50 ? " ." : ">E";
}
}
for ($l = 0;$l < intval($argv[2]);$l++)
{
echo "\n";
$mat = array_fill(0,32,null);
for ($a = 0;$a < 15;$a++)
{
$mat[$a] = ord(fgetc(STDIN));
}
for ($m = 0;$m < 15;$m++)
{
echo $mat[$m] > 50 ? " ." : " v";
}
echo "\n";
for ($m = 0;$m < 15;$m++)
{
echo $mat[$m] > 50 ? " ." : ">e";
}
}
echo "\n | | | | | | | | | | | | | | |\n v v v v v v v v v v v v v v v\n l l l l l l l l l l l l l l l";
}
if ($argv[3] == "1")
{
$t = "f";
}
if ($argv[3] == "2")
{
$t = "F";
}
$id = bin2hex(fread(STDIN,32));
echo "\n0\"Nagravision Syster ID : " . $id ."\n";
echo $argv[4] ? $t." T##############\n| |||||||||||||||\n| 012345678901234                                \n| 000000000011111                                \n| ======================================\n| 012345678901234        012345678901234\n| 000000000011111        000000000011111\n| vvvvvvvvvvvvvvv        vvvvvvvvvvvvvvv\n| ###############i1      ###############i2\n| ||||||||  |||||||      ||||||||  |||||||\n| |||||||| F|||||||      |||||||| F|||||||\nv vvvvvvvv vvvvvvvv      vvvvvvvv vvvvvvvv\nl T####### T#######      T####### T#######" :
                $t." T##############\n| |||||||||||||||\n| 012345678901234                                \n| 000000000011111                                \n| ======================================\n| 012345678901234        012345678901234\n| 000000000011111        000000000011111\n| vvvvvvvvvvvvvvv        vvvvvvvvvvvvvvv\n| ###############i1      ###############i1\n| ||||||||  |||||||      ||||||||  |||||||\n| |||||||| F|||||||      |||||||| F|||||||\nv vvvvvvvv vvvvvvvv      vvvvvvvv vvvvvvvv\nl T####### T#######      T####### T#######";
