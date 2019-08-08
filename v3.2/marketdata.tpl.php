<?php
    $directory = dirname(__FILE__);

    $command = "/home/nicrev2/opt/python-3.7.1/bin/python3 $directory/interface.py 'marketdata'";
    $result = shell_exec($command);

    // Decode the result
    $marketData = json_decode($result, true);
?>
<?php if (!empty($marketData)):?>
    <div class ="stock-market-list">
        <?php
            $marketList = explode(",","DIA,SPY,QQQ");
        ?>
        <?php foreach ($marketList as $marketIndex):?>
        <div class ="stock-market-box">
            <?php
                $market = "";
                if ($marketData[$marketIndex]['symbol'] == "DIA")
                {
                    $market = "Dow Jones";
                }
                else if ($marketData[$marketIndex]['symbol'] == "SPY")
                {
                    $market = "S&P 500";
                }
                else
                {
                    $market = "Nasdaq 100";
                }
            ?>
            <?=$market?><br><?=$marketData[$marketIndex]['change']?>
        </div>
        <?php endforeach ?>
    </div>
<?php endif?>
