<?php

// Output the header of the page. We're brute forcing it by writing the html here

$header = "<h1>Stocks</h1>";
$header .= '<form method = "get">';
$header .=  "Enter Stock Symbols: ";
$header .= '<input type="text" name="stocks" value="' . $stocks . '"> ';
$header .= '<input type="submit" value="Submit"><br>';
$header .= "<span style = 'font-size: 11px;'>Get multiple stocks by separating them with commas.</span></form>";
$header .= "<p><span style = 'font-size: 12px;'>Data provided for free by <a href = 'https://iextrading.com/developer'>IEX</a>. View <a href = 'https://iextrading.com/api-exhibit-a/'>IEX’s Terms of Use</a>.</span></p>";
echo($header);

/**
 * If stocks isn't in the get request, do something else
 */
if(!empty($_GET['stocks']))
{
    $stocks = $_GET['stocks'];

    // Make sure the information we get has no spaces and is escaped.
    $stocks = str_replace(' ', '', $stocks);
    $data=escapeshellarg($stocks);

    // Execute the python script while passing in the JSON data
    $directory = dirname(__FILE__);
    $command = "python3 $directory/interface.py $data";
    $result = shell_exec($command);

    // Decode the result
    $resultData = json_decode($result, true);

    // Manipulate the output json and display it in a rough format that looks readable.
    $output .= "<p><dl>";
    $first = false;
    foreach ($resultData as $section)
    {
        if ($first == true)
        {
            $output .= "<br>";
        }
        if (sizeOf($resultData > 1 && $first == false))
        {
            $first = true;
        }
        $output .= "<dt>" . $section['symbol'] . " - " . $section['company'] . "</dt>";
        $output .= "<dd>Real Time Price: " . $section['iexRealtimePrice'] . "</dd>";
        $output .= "<dd>Open: " . $section['open'] . "</dd>";
        $output .= "<dd>Close: " . $section['close'] . "</dd>";
        $output .= "<dd>52 Week High: " . $section['week52High'] . "</dd>";
        $output .= "<dd>52 Week Low: " . $section['week52Low'] . "</dd>";
    }
    $output .= "</dl></p>";

    echo ($output);
}
else
{
    //Do something else, like display the average market data or something. Tackle for future version
}

// Stop executing code
exit();
?>