<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
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
                <input type='text' name='stocks' placeholder="Enter stock symbols here" value='<?=str_replace(' ', '', $_GET['stocks'])?>'>
                <input type='submit' value='Submit'>
                <br>
                <span style = 'font-size: 11px;'>Get multiple stocks by separating them with commas.</span>
            </form>   
        </div>
        <?php
            include "marketdata.tpl.php";
        ?>
        <?php
            include "stockresults.tpl.php";
        ?>
    </div>
    <div class="footer"><span style = 'font-size: 12px;'><a href="https://iexcloud.io">Data provided by IEX Cloud</a></span></div>
</body>
</html>