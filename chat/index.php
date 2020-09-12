<?php
session_start ();
function loginForm() {
    echo '
	<div class="form-group">
		<div id="loginform">
			<form action="index.php" method="post">
			<h1>XChat</h1><hr/>
				<b><label for="name" style="font-size:25">Inserte Su Nombre</label></b></br>
                <i><label for="name" style="font-size:12">(Inserte como quiere que se le dirijan )</label></i>
				<input type="text" name="name" id="name" class="form-control" placeholder="Insertar Nombre"/>
				<input type="submit" class="btn btn-default" name="enter" id="enter" value="Enviar" />
			</form>
		</div>
	</div>
   ';
}
 
if (isset ( $_POST ['enter'] )) {
    if ($_POST ['name'] != "") {
        $_SESSION ['name'] = stripslashes ( htmlspecialchars ( $_POST ['name'] ) );
        $cb = fopen ( "logs.html", 'a' );
        fwrite ( $cb, "<div class='msgln'><i>El usuario " . $_SESSION ['name'] . " se ha unido al chat.</i><br></div>" );
        fclose ( $cb );
    } else {
        echo '<span class="error">Porfavor Introduzca Un Nombre</span>';
    }
}
 
if (isset ( $_GET ['logout'] )) {
    $cb = fopen ( "logs.html", 'a' );
    fwrite ( $cb, "<div class='msgln'><i>El usuario " . $_SESSION ['name'] . " ha salido del chat.</i><br></div>" );
    fclose ( $cb );
    session_destroy ();
    header ( "Location: index.php" );
}
?>
<!DOCTYPE html>
<html>
<head>
	<title>CleanChat</title>
	<link rel="stylesheet" href="css/style.css">
	<link rel="stylesheet" href="bootstrap/css/bootstrap.min.css">
	<script type="text/javascript" src="js/jquery.min.js"></script>
</head>
<body>
<?php
	if (! isset ( $_SESSION ['name'] )) {
	loginForm ();
	} else {
?>
<div id="wrapper">
	<div id="menu">
	<h1>XCha</h1><hr/>
		<p class="welcome"><b>Bienvenid@ - <a><?php echo $_SESSION['name']; ?></a></b></p>
		<p class="logout"><a id="exit" href="#" class="btn btn-default">Salir del Chat</a></p>
	<div style="clear: both"></div>
	</div>
	<div id="chatbox">
	<?php
		if (file_exists ( "logs.html" ) && filesize ( "logs.html" ) > 0) {
		$handle = fopen ( "logs.html", "r" );
		$contents = fread ( $handle, filesize ( "logs.html" ) );
		fclose ( $handle );
		echo $contents;
		}
	?>
	</div>
<form name="message" action="">
	<input name="usermsg" class="form-control" type="text" id="usermsg" placeholder="Escriba un mensaje..." />
	<input name="submitmsg" class="btn btn-default" type="submit" id="submitmsg" value="Enviar" />
</form>
</div>
<script type="text/javascript">
$(document).ready(function(){
});
$(document).ready(function(){
    $("#exit").click(function(){
        var exit = confirm("Estas seguro de que quieres salir de la página?");
        if(exit==true){window.location = 'index.php?logout=true';}     
    });
});
$("#submitmsg").click(function(){
        var clientmsg = $("#usermsg").val();
        $.post("post.php", {text: clientmsg});             
        $("#usermsg").attr("value", "");
        loadLog;
    return false;
});
function loadLog(){    
    var oldscrollHeight = $("#chatbox").attr("scrollHeight") - 20;
    $.ajax({
        url: "logs.html",
        cache: false,
        success: function(html){       
            $("#chatbox").html(html);       
            var newscrollHeight = $("#chatbox").attr("scrollHeight") - 20;
            if(newscrollHeight > oldscrollHeight){
                $("#chatbox").animate({ scrollTop: newscrollHeight }, 'normal');
            }              
        },
    });
}
setInterval (loadLog, 2500);
</script>
<?php
}
?>
</body>
</html>