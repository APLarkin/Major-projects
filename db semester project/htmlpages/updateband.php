<?php
	//Connect to database
	$conn = new mysqli("localhost","msm","pass123","PostHardcore");
	// Check connection
	if ($conn->connect_error) {
		die("Connection failed: " . $conn->connect_error);
	}
	//Get post data
	$bandname = $_POST["bandname"];
	//If any fields are left empty, then get the relevant data from the DB.
	if(!empty($_POST["upbandname"]))
	{
		$band = $_POST["upbandname"];
	}
	else{
		$band = $conn->query("select BandName from Band where BandName=".$bandname.";");
	}
	if(!empty($_POST["upleadvocals"]))
	{
		$vocals = $_POST["upleadvocals"];
	}
	else{
		$vocals = $conn->query("select LeadSinger from Band where BandName=".$bandname.";");
	}
	if(!empty($_POST["upleadguitar"]))
	{
		$guitar = $_POST["upleadguitar"];
	}
	else{
		$guitar = $conn->query("select Guitarist from Band where BandName=".$bandname.";");
	}
	if(!empty($_POST["uprhythm"]))
	{
		$rhythm = $_POST["uprhythm"];
	}
	else{
		$rhythm = $conn->query("select Rhythm from Band where BandName=".$bandname.";");
	}
	if(!empty($_POST["upbassist"]))
	{
		$bassist = $_POST["upbassist"];
	}
	else{
		$bassist = $conn->query("select Bassist from Band where BandName=".$bandname.";");
	}
	if(!empty($_POST["uppercussion"]))
	{
		$percussion = $_POST["uppercussion"];
	}
	else{
		$percussion = $conn->query("select Drummer from Band where BandName=".$bandname.";");
	}
	if(!empty($_POST["upother"]))
	{
		$other = $_POST["upother"];
	}
	else{
		$other = $conn->query("select Other from Band where BandName=".$bandname.";");
	}
	if(!empty($_POST["uplabelname"]))
	{
		$label = $_POST["labelname"];
	}
	else{
		$label = $conn->query("select LabelName from Band where BandName=".$bandname.";");
	}
	
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

	//construct query
	$query = "UPDATE Band set BandName=".$band.",LeadSinger=".$vocals.",Guitarist=".$guitar.",Rhythm=".$rhythm.",Bassist=".$bassist.",Drummer=".$percussion.",Other=".$other.",LabelName".$label.");";
	
	//Send query
	if($conn->query($query) === TRUE){
		echo $page_data_top."<center><div>Successfully updated the data</div></center>".$page_data_bottom;
	}
	else{
		echo $page_data_top."<center><div>Error updating data in the database.</div></center>".$page_data_bottom;
	}
	
	$conn->close();
?>