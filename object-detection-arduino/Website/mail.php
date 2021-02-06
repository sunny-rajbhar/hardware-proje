<?php

require 'phpmailer/PHPMailerAutoload.php';

$mail = new PHPMailer();
$mail->isSMTP();
$mail->SMTPAuth = true;
$mail->SMTPSecure = "ssl";
$mail->Host = "smtp.gmail.com";
$mail->Port = 465;
$mail->isHTML();
$mail->Username = "your@email.com";
$mail->Password = "youremailpass";
$mail->SetFrom('your@email.com', 'Arduino');

$mail->Subject = "test email";

$mail->Body = "this is our body";

$mail->AddAddress('your@email.com');

if ($mail->send())
echo "mail is sent";
else
echo "somthing wronng";
?>