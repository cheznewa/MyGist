<?php
$machid = hex2bin(file_get_contents("/etc/machine-id",null,null,0,6));
if (ord($machid[0]) <= 50)
$subsys = "BLE TOU";
if (ord($machid[0]) > 50 && ord($machid[0]) <= 80)
$subsys = "Phélÿn";
if (ord($machid[0]) > 80 && ord($machid[0]) <= 150)
$subsys = "Moênne";
if (ord($machid[0]) > 150 && ord($machid[0]) <= 180)
$subsys = "Indih";
if (ord($machid[0]) > 180 && ord($machid[0]) <= 200)
$subsys = "Solainie";
if (ord($machid[0]) > 200 && ord($machid[0]) <= 220)
$subsys = "Movénie";
if (ord($machid[0]) > 220 && ord($machid[0]) <= 250)
$subsys = "Joséro";
if (ord($machid[0]) > 250 && ord($machid[0]) <= 255)
$subsys = "Luana";
$x = ord($machid[1]);
$y = ord($machid[2]);
echo "Sous-Systèm :: $subsys\nCartier X :: $x\nCartier Y :: $y\n";