<?php

$conn = mysqli_connect('localhost','root','sun1234','agv');

//mysqli_select_db($conn,'agv');

$sql="SELECT * From p_details";

$record=mysqli_query($conn,$sql);

?>

<html>
<head>
<title>Welcome!</title>
<meta charset="utf-8">
</head>
<body>
<form action="p3.php" method="post">

<?php
while($a=mysqli_fetch_assoc($record)){
if(isset($_POST[$a['P_No']])) 
{

$z=$_POST[$a['Time']];
/*$b=$_POST['2'];
$c=$_POST['3'];
$d=$_POST['4'];
$e=$_POST['5'];
$f=$_POST['6'];
$g=$_POST['7'];
$h=$_POST['8'];
$i=$_POST['9'];
$j=$_POST['10'];	
$k=$_POST['11'];
*/

$l = $a['Time'];
echo $l;
echo $z;
echo "<br>";
$sql1 = "INSERT INTO 't_table' (t2) VALUES (6)";
$re=mysqli_query($conn,$sql1);
}
}
$sql2 = "INSERT INTO t_table (t3) VALUES ($l)";
$re=mysqli_query($conn,$sql2);
?>
</form>
</body>
</html>