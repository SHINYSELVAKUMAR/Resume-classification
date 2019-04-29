<?php
$con = new mysqli( "localhost", "root", " ", "job");    
$reset = (int) $_GET[ "reset" ];
 // either 1 or 0 ( true and false )   
  $username = "user1"; 
  // the user who's notifications we will be loading    
  if( $reset === 1 )
  	{   
  		$sql = "SELECT * FROM `notify` WHERE `user_id`='" . $username . "' ORDER BY `time` DESC LIMIT 10;"; 
         setcookie( "loadedNotifications", "10", time() + 86400, "/" ); 
   // store the cookie holding the amount of loaded notifications  
   }  
   else
   {   
   	$loadedNots=(int) $_COOKIE[ "loadedNotifications" ]; 
   	// get the amount of previously loaded notifications   
   	$sql = "SELECT * FROM `notify` WHERE `user_id`='" . $username . "' ORDER BY `time` DESC LIMIT " . $loadedNots . " 10;"; 
   	  $loadedNots = (string)( $loadedNots + 10 ); 
   	 // calculate how many notifications have been loaded after query   
   	 setcookie( "loadedNotifications", $loadedNots, time() + 86400, "/" ); 
   	 // update cookie with new value  
   	 }    
   	 $result = $con->query( $sql );   
   	  $notifications = array(); 
   	  // declare an array to store the fetched notifications  
   	    if( $result->num_rows > 0 )
   	    {    
   	    while( $row = $result->fetch_assoc() )
   	    {    
   	    $notifications[] = array( "id" => $row[ "notifyid" ],  "entityID" => $row[ "entityID" ], "read" => $row[ "read" ], "text" => "" );   
   	    }  
   	    }   
   	    else
   	    {   // no more notifications  
   	    }    /*  * now we need to find the activity that relates to the notification  * and create a text message that will be displayed to the user  * containing the users who are responsible for that particular activity  */    
   	    for( $i = 0; $i < count( $notifications ); $i++ )
   	    {   
   	    $sql = ""; 
   	    // reset query string each time loop runs     
   	     // use different code for each type of notification ( ie. comments or ratings )  
   	    	 // other cases to suit your needs   
   	    }  
   	   }    
   	    	 echo( json_encode( $notifications ) ); // convert array to JSON text  
   	    	 ?>

   