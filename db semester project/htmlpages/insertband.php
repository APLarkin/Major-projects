<?php
	//Connect to database
	$conn = new mysqli("localhost","msm","pass123","PostHardcore");
	// Check connection
	if ($conn->connect_error) {
		die("Connection failed: " . $conn->connect_error);
	}
	//Get post data
	$band = $_POST["bandname"];
	$vocals = $_POST["leadvocals"];
	$guitar = $_POST["leadguitar"];
	$rhythm = $_POST["rhythm"];
	$bassist = $_POST["bassist"];
	$percussion = $_POST["percussion"];
	$other = $_POST["other"];
	$label = $_POST["labelname"];
	//construct query
	$query = "INSERT INTO Band VALUES (".$band.",".$vocals.",".$guitar.",".$rhythm.",".$bassist.",".$percussion.",".$other.",".$label.");";
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
		echo $page_data_top."<center><div>Successfully recorded the data</div></center>".$page_data_bottom;
	}
	else{
		echo $page_data_top."<center><div>Error recording data to the database.</div></center>".$page_data_bottom;
	}
	
	$conn->close();
?>