<html>
<head>
    <meta name="viewport" content="width=500px, initial-scale=1, user-scalable=yes">
    <meta http-equiv="content-type" content="text/html;charset=utf-8" />
    <link type="text/css" rel="stylesheet" href="page.css"/>
    <title>28Protons: Stock API Project</title>
</head>
<body>
    <div class = "header">
        <h1>Stocks</h1>
    </div>
    <div class = "body-div">
        <div class = "form-div">
            <form method = "get">
                Enter Stock Symbols: 
                <input type='text' name='stocks' value='<?=str_replace(' ', '', $_GET['stocks'])?>'>
                <input type='submit' value='Submit'>
                <br>
                <span style = 'font-size: 11px;'>Get multiple stocks by separating them with commas.</span>
            </form>   
        </div>
        <?
            include "marketdata.tpl.php";
        ?>
        <?  
            include "stockresults.tpl.php";
        ?>
    </div>
    <div class="footer"><span style = 'font-size: 12px;'>Data provided for free by <a href = 'https://iextrading.com/developer'>IEX</a>. View <a href = 'https://iextrading.com/api-exhibit-a/'>IEX’s Terms of Use</a>.</span></div>
</body>
</html>