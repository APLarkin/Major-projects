<?php
	//Connect to database
	$conn = new mysqli("localhost","msm","pass123","PostHardcore");
	// Check connection
	if ($conn->connect_error) {
		die("Connection failed: " . $conn->connect_error);
	}
	//Get post data
	$song = $_POST["songname"];
	if(!empty($_POST["upbandname"]))
	{
		$band = $_POST["upbandname"];
	}
	else{
		$band = $conn->query("select BandName from Songs where SongTitle=".$song.";");
	}
	if(!empty($_POST["upalbumtitle"]))
	{
		$album = $_POST["upalbumtitle"];
	}
	else{
		$album = $conn->query("select AlbumTitle from Songs where SongTitle=".$song.";");
	}
	if(!empty($_POST["upsongtitle"]))
	{
		$title = $_POST["upsongtitle"];
	}
	else{
		$title = $conn->query("select SongTitle from Songs where SongTitle=".$song.";");
	}
	if(!empty($_POST["upyear"]))
	{
		$year = $_POST["upyear"];
	}
	else{
		$year = $conn->query("select YearProduced from Songs where SongTitle=".$song.";");
	}
	//construct query
	$query = "INSERT INTO Songs VALUES (".$title.",".$album.",".$band.",".$year.")";
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