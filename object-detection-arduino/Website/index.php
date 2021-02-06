<?php 
    // Start MySQL connection
    include('dbconnect.php'); 
?>
<!DOCTYPE html>
<html>

<head>

	<meta charset="utf-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<meta name="keywords" content="footer, basic, centered, links" />

	<title>ABSS</title>

	<link rel="stylesheet" href="css/demo.css">
	<link rel="stylesheet" href="css/footer-basic-centered.css">

</head>

	<body>

		<header>
			<h1><b>Arduino Based Security System</b></h1>
			<h2>Arduino Motion Logs</h2>
		<center>
		<table border="0" cellspacing="0" cellpadding="4" align="center">
			<tr>
				  <td class="table_titles">ID</td>
				  <td class="table_titles">Date and Time</td>
				  <td class="table_titles">Motion</td>
				</tr>
	  	<?php
		  // Retrieve all records and display them
		  $result = $dbh->query("SELECT * FROM motion ORDER BY id ASC");
	  
		  // Used for row color toggle
		  $oddrow = true;
	  
		  // process every record
		  while( $row = mysqli_fetch_array($result) )
		  {
			  if ($oddrow) 
			  { 
				  $css_class=' class="table_cells_odd"'; 
			  }
			  else
			  { 
				  $css_class=' class="table_cells_even"'; 
			  }
	  
			  $oddrow = !$oddrow;
	  
			  echo '<tr>';
			  echo '   <td'.$css_class.'>'.$row["id"].'</td>';
			  echo '   <td'.$css_class.'>'.$row["event"].'</td>';
			  echo '   <td'.$css_class.'>'.$row["motion"].'</td>';
			  echo '</tr>';
		  }
	  	?>
		  </table>
		</center>
		</header>
		<!-- The content of your page would go here. -->

		<footer class="footer-basic-centered">

			<p class="footer-company-motto">To Create Secure Future</p>

			<p class="footer-links">
				<a href="#">Sunny</a>
				·
				<a href="#">Ahmed</a>
				·
				<a href="#">Sadik</a>
				
			</p>

			<p class="footer-company-name">Saturny Community &copy; 2018</p>

		</footer>

	</body>

</html>
