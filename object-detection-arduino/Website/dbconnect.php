<?php
$MyUsername = "root";       // mysql username
$MyPassword = "";       // mysql password
$MyHostname = "localhost";       // Your Host  // localhost if you have own local server or root server normally
$Database = "mydb";       // Name of your database
$dbh = mysqli_connect($MyHostname , $MyUsername, $MyPassword, $Database);
if (!$dbh) {
    die("Connection failed: " . mysqli_connect_error());
}
?>

