<?php
	//Connect to database
	$conn = new mysqli("localhost","msm","pass123","PostHardcore");
	// Check connection
	if ($conn->connect_error) {
		die("Connection failed: " . $conn->connect_error);
	}
	//Get post data
	$name = $_POST["labelname"];
	$type = $_POST["labeltype"];
	//construct query
	$query = "INSERT INTO Label VALUES (".$name.",".$type.");";
		//Set up page data for formatting.
	$page_data_top = "<!DOCTYPE html>
	<html>
	<body bgcolor=#FF9900>
	<style>
		a:hover {
			text-shadow: 2px 2px #fff;
		}
		a:link {
			text-decoration: none;
		}
		div {
			font-size: 150%;
		}
		ul {
			list-style-type: none;
		}
		</style>";

	$page_data_bottom="<a href=\"hubpage.html\"><div>Back to main</div></a>
		</body>
		</html>";
	
	//Send query
	if($conn->query($query) === TRUE){
		echo $page_data_top."<center><div>Successfully recorded the data</div></center>";
	}
	else{
		echo $page_data_top."<center><div>Error recording data to the database.</div></center>";
	}
	
	$conn->close();
?>