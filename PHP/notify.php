<?php
	function notify(  $user_id, $entity_id )
	{    
	$con = new mysqli( "localhost", "root", "password", "job");       
	$sql = "SELECT `notificationID` FROM `notify` WHERE `user_id`='" . $user_id . "' AND `entity_id`=" . $entity_id . ";";    
	$result = $con->query( $sql );        
	// if query returned a row, it means the notify exists    i
	f( $result->num_rows > 0 )
	{     
	// update the existing record, set read to false and time to the current time     
	$sql = "UPDATE `notify` SET `read`=0, `time`=NOW() WHERE `user_id`='" . $user_id . "' AND `entity_id`=" . $entity_id . " ;";     
	$con->query( $sql );    
	}    
	else
	{    
	// insert new record with the details    
		$sql = "INSERT INTO `notify`(  `user_id`, `entity_id` ) VALUES( '" . $user_id . "'," . $entity_id. " );";     
		$con->query( $sql );   
	 }   
	$con->close();  
} 

?>
