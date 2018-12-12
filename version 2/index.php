<?

// Gets anything supposed to be displayed as a stock and returns it as result data
if(!empty($_GET['stocks']))
{
    $data=escapeshellarg(str_replace(' ', '', $_GET['stocks']));
    // Execute the python script with the JSON data
    $directory = dirname(__FILE__);
    $command = "python3 $directory/interface.py $data";
    $result = shell_exec($command);
    // Decode the result
    $resultData = json_decode($result, true);
}

// Includes the main template php file to display the page
include "main.tpl.php";
?>