<?php
// https://archive.org/details/Youtube_dislike_count_export_2021-11-18
// zstd -dcq /path/to/dislikes_export_2021_11_18.txt.xz | php getripdislikeyt.php TonIDA11Car
if (11 !== strlen($argv[1]))
{
echo "Une ID De Vidéo A 11 Caractère, C'est Juste Que Ca, Ce Que Je Demande\n";
exit(2);
}
while ($f = fgets(STDIN))
{
$expl = explode("\t",$f);
if ($expl[0] == $argv[1])
{
echo "Téléspectateurs :::: ".intval($expl[2])."\n";
echo "Pouces Haut :::: ".intval($expl[3])."\n";
echo "Pouces Bas :::: ".intval($expl[4])."\n";
echo intval($expl[5]) ? "Vidéo Supprimé :::: Oui\n" : "Vidéo Supprimé :::: Probablement Pas\n";
exit(intval($expl[5]));
}
}
echo "Désolé, Ton ID N'existe Pas :(\n";
exit(3);