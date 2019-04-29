<?php 
define('DB_HOST', 'localhost'); 
define('DB_NAME', 'practice'); 
define('DB_USER','root'); 
define('DB_PASSWORD',''); 

$con=mysql_connect(DB_HOST,DB_USER,DB_PASSWORD) or die("Failed to connect to MySQL: " . mysql_error()); 
$db=mysql_select_db(DB_NAME,$con) or die("Failed to connect to MySQL: " . mysql_error()); 
function NewUser() 

{ 
	$fullname = $_POST['name']; 
	$userName = $_POST['user']; 
	$email = $_POST['email']; 
	$password = $_POST['pass']; 
	$query = "INSERT INTO websiteusers (fullname,userName,email,pass) VALUES ('$fullname','$userName','$email','$password')"; 
	$data = mysql_query ($query)or die(mysql_error()); 
	if($data) 
	{ 
	echo "YOUR REGISTRATION IS COMPLETED..."; 
	} 
}
	 function SignUp() 
	 { 
	 	if(!empty($_POST['user'])) 
	 	//checking the 'user' name which is from Sign-Up.html, is it empty or have some text 
	 		{ 
	 			$query = mysql_query("SELECT * FROM websiteusers WHERE userName = '$_POST[user]' AND pass = '$_POST[pass]'") or die(mysql_error()); 
	 			if(!$row = mysql_fetch_array($query) or die(mysql_error())) 
	 				{ 
	 					newuser(); 
	 				} 
	 				else 
	 				{ 
	 					echo "SORRY...YOU ARE ALREADY REGISTERED USER..."; 
	 				} 
	 		} 
	 } 
	 			if(isset($_POST['submit'])) 
	 				{ 
	 					SignUp(); 
	 				}
	 		?>

