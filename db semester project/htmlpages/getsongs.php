<?php
	//Connect to database
	$conn = new mysqli("localhost","msm","pass123","PostHardcore");
	// Check connection
	if ($conn->connect_error) {
		die("Connection failed: " . $conn->connect_error);
	}
	//Get post data
	$album = $_POST["albumname"];
	//Get songs, band, and year produced.
	$query = "select SongTitle from Song where AlbumTitle=".$album.";";
	$songs = $conn->query($query);
	
	$query = "select BandName from Song where AlbumTitle=".$album.";";
	$band = $conn->query($query);
	$query = "select YearProduced from Album where AlbumTitle=".$album.";";
	$year = $conn->query($query);
	//Get label.
	$query = "select LabelName from Album where AlbumTitle=".$album.";";
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
		echo $page_data_top."<center><div>Tracks on this album: ".$songs."</div>\n<div>Produced by: ".$band."</div>\n<div>Sponsored by: ".$label."</div>\n<div>Released: ".$year."</div></center>".$page_data_bottom;
	}
	else{
		echo $page_data_top."<center><div>Error getting data from the database.</div></center>".$page_data_bottom;
	}
	
	$conn->close();
?>