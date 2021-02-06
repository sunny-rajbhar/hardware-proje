<?php

$conn = mysqli_connect('localhost','root','sun1234');

mysqli_select_db($conn,'agv');

$sql="SELECT * From p_details";

$record=mysqli_query($conn,$sql);

?>

<html>
<head>
<style>
table{
	border-collapse:collapse;
	width:90%;
}

th,td{
	padding:4px;
	text-align:left;
	border-bottom:3px solid#ddd;
}

tr:nth-child(even){background-color:#f2f2f2}

th{
	background-color:#4CAF50;
	color:white;
	
</style>	
<title>Welcome!</title>
<meta charset="utf-8">
</head>
<body>
<form action="p2.php" method="post">

<center>
<caption><h3>Your Selected Products List</h3></caption>
<table width = "600" border="1" cellpadding="1" cellspacing="1">
<tr>
<th> P_No</th>
<th> P_Name </th>
<th> Price</th>
</tr>

<?php
while($a=mysqli_fetch_assoc($record)){
if(isset($_POST[$a['P_No']]) ) 
{
$p = $_POST[$a['P_No']];
echo "<tr>";
echo "<td>".$p."</td>";
echo "<td>".$a['P_Name']."</td>";
echo "<td>".$a['Price']."</td>";
echo "</tr>";
//$sql = "INSERT INTO t_table (P_No, P_Name, Price, Time) VALUES ($p, $a['P_Name], $a['Price'], $a['Time'])";
}
}
	
?>
</center>
</table>
<caption><h3>***Thank You!***</h3></caption>
</form>
</body>
</html>



