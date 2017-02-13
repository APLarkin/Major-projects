<?php
	//Connect to database
	$conn = new mysqli("localhost","msm","pass123","PostHardcore");
	// Check connection
	if ($conn->connect_error) {
		die("Connection failed: " . $conn->connect_error);
	}
	//Get post data
	$label = $_POST["labelname"];
	if(!empty($_POST["upbandname"]))
	{
		$name = $_POST["uplabelname"];
	}
	else{
		$name = $conn->query("select LabelName from Label where LabelName=".$label.";");
	}
	if(!empty($_POST["upbandname"]))
	{
		$type = $_POST["uplabeltype"];
	}
	else{
		$type = $conn->query("select LabelType from Label where LabelName=".$label.";");
	}
	//construct query
	$query = "update Label set LabelName=".$name.",LabelType=".$type.");";
	
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