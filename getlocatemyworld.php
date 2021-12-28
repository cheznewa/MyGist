<?php
$machid = hex2bin(file_get_contents("/etc/machine-id",null,null,0,18));
if (ord($machid[0]) <= 50)
{
$subsys = "BLE TOU";
$x = intval((ord($machid[7])*pow(256,3))+(ord($machid[1])*pow(256,2))+(ord($machid[3])*pow(256,1))+ord($machid[5]));
$y = intval((ord($machid[8])*pow(256,3))+(ord($machid[2])*pow(256,2))+(ord($machid[4])*pow(256,1))+ord($machid[6]));
}
if (ord($machid[0]) > 50 && ord($machid[0]) <= 80)
{
$subsys = "Phélÿn";
$x = intval(((ord($machid[7])*pow(256,3))+(ord($machid[1])*pow(256,2))+(ord($machid[3])*pow(256,1))+ord($machid[5]))/3);
$y = intval(((ord($machid[8])*pow(256,3))+(ord($machid[2])*pow(256,2))+(ord($machid[4])*pow(256,1))+ord($machid[6]))/3);
}
if (ord($machid[0]) > 80 && ord($machid[0]) <= 150)
{
$subsys = "Moênne";
$x = intval((ord($machid[7])*pow(256,3))+(ord($machid[1])*pow(256,2))+(ord($machid[3])*pow(256,1))+ord($machid[5]));
$y = intval((ord($machid[8])*pow(256,3))+(ord($machid[2])*pow(256,2))+(ord($machid[4])*pow(256,1))+ord($machid[6]));
}
if (ord($machid[0]) > 150 && ord($machid[0]) <= 180)
{
$subsys = "Indih";
$x = intval(((ord($machid[7])*pow(256,3))+(ord($machid[1])*pow(256,2))+(ord($machid[3])*pow(256,1))+ord($machid[5]))/4);
$y = intval(((ord($machid[8])*pow(256,3))+(ord($machid[2])*pow(256,2))+(ord($machid[4])*pow(256,1))+ord($machid[6]))/4);
}
if (ord($machid[0]) > 180 && ord($machid[0]) <= 200)
{
$subsys = "Solainie";
$x = intval(((ord($machid[7])*pow(256,3))+(ord($machid[1])*pow(256,2))+(ord($machid[3])*pow(256,1))+ord($machid[5]))/2);
$y = intval(((ord($machid[8])*pow(256,3))+(ord($machid[2])*pow(256,2))+(ord($machid[4])*pow(256,1))+ord($machid[6]))/2);
}
if (ord($machid[0]) > 200 && ord($machid[0]) <= 220)
{
$subsys = "Movénie";
$x = intval(((ord($machid[7])*pow(256,3))+(ord($machid[1])*pow(256,2))+(ord($machid[3])*pow(256,1))+ord($machid[5]))/5);
$y = intval(((ord($machid[8])*pow(256,3))+(ord($machid[2])*pow(256,2))+(ord($machid[4])*pow(256,1))+ord($machid[6]))/5);
}
if (ord($machid[0]) > 220 && ord($machid[0]) <= 250)
{
$subsys = "Joséro";
$x = intval(((ord($machid[7])*pow(256,3))+(ord($machid[1])*pow(256,2))+(ord($machid[3])*pow(256,1))+ord($machid[5]))/3);
$y = intval(((ord($machid[8])*pow(256,3))+(ord($machid[2])*pow(256,2))+(ord($machid[4])*pow(256,1))+ord($machid[6]))/3);
}
if (ord($machid[0]) > 250 && ord($machid[0]) <= 255)
{
$subsys = "Luana";
$x = intval(((ord($machid[7])*pow(256,3))+(ord($machid[1])*pow(256,2))+(ord($machid[3])*pow(256,1))+ord($machid[5]))/4);
$y = intval(((ord($machid[8])*pow(256,3))+(ord($machid[2])*pow(256,2))+(ord($machid[4])*pow(256,1))+ord($machid[6]))/4);
}
echo "Sous-Systèm :: $subsys\nCartier X :: $x\nCartier Y :: $y\n";