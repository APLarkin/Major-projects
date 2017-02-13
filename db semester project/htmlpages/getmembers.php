<?php
	//Connect to database
	$conn = new mysqli("localhost","msm","pass123","PostHardcore");
	// Check connection
	if ($conn->connect_error) {
		die("Connection failed: " . $conn->connect_error);
	}
	//Get post data
	$band = $_POST["bandname"];
	//Get lineup.
	$query = "select LeadSinger, Guitarist, Rhythm, Bassist, Drummer, Other from Band where BandName=".$band.";";
	$members = $conn->query($query);
	
	//Get list of albums.
	$query = "select AlbumTitle, YearProduced from Album where BandName=".$band.";";
	$albums = $conn->query($query);
	//Get label.
	$query = "select LabelName from Band where BandName=".$band.";";
	$label = $conn->query($query);
	
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
		echo $page_data_top."<center><div>The current lineup is: ".$members."</div></center><br/><br/>"."<center><div>Their albums include: ".$albums."</center></div><br/><br/>"."<center><div>Their current label is: ".$label."</center></div><br/><br/>".$page_data_bottom;
		
		}
	else{
		echo "Error getting data from the database."
	}
	
	$conn->close();
?>