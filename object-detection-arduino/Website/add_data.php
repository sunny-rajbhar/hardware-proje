<?php
    // Connect to MySQL
	include("dbconnect.php");
	require 'phpmailer/PHPMailerAutoload.php';

	$SQL = "INSERT INTO mydb.motion (motion) VALUES ('".$_GET["motionornot"]."')";
	$dbh->query($SQL);

	$mail = new PHPMailer();
	$mail->isSMTP();
	$mail->SMTPAuth = true;
	$mail->SMTPSecure = "ssl";
	$mail->Host = "smtp.gmail.com";
	$mail->Port = 465;
	$mail->isHTML();
	$mail->Username = "saturny4@gmail.com";
	$mail->Password = "saturny@123";
	$mail->SetFrom('saturny4@gmail.com', 'Arduino');

	$mail->Subject = "Alert Email";

	$mail->Body = "Intruder is Detected...! <br /> <br /> <a href='http://192.168.43.185/arduino/index.php'>See Full Logs</a> ";

	$mail->AddAddress('saturny4@gmail.com');

	if ($mail->send())
	echo "mail is sent";
	else
	echo "somthing wronng";
?>
