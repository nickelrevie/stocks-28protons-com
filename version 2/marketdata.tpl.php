<?
    $directory = dirname(__FILE__);
    $command = "python3 $directory/interface.py 'marketdata'";
    $result = shell_exec($command);
    // Decode the result
    $marketData = json_decode($result, true);
?>
<? if (!empty($marketData)):?>
    <div class ="stock-market-list">
        <?
            $marketList = explode(",","DIA,SPY,QQQ");
        ?>
        <? foreach ($marketList as $marketIndex):?>
        <div class ="stock-market-box">
            <?
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
        <? endforeach ?>
    </div>
<?endif?>
