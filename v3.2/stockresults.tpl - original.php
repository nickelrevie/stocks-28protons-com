<?php if (!empty($resultData)):?>
    <div class ="stock-list">
    <?php
        $array = explode(",",strtoupper(str_replace(' ', '', $_GET['stocks'])));
    ?>
    <?php foreach ($array as $stock):?>
        <?php if (!empty($resultData[$stock]['company'])):?>
            <dl class='stock-entry' onmouseover="addClass(this,'stock-highlight');" onmouseout="removeClass(this, 'stock-highlight');">
                <dt>
                    <?=$resultData[$stock]['company']?> (<?=$resultData[$stock]['symbol']?>)
                </dt>
                <dd>
                    <span class = "price"><?=$resultData[$stock]['latestPrice']?></span> <?=$resultData[$stock]['change']?>
                </dd>
                <?php if((strcmp($resultData[$stock]['marketPhase'],"market")) != 0):?>
                <?php date_default_timezone_set('America/New_York')?>
                <dd>
                    <?=$resultData[$stock]['extendedQuote']?> <span class = "market-phase"><?=$resultData[$stock]['marketPhase']?> price as of <?=date('H:i', $resultData[$stock]['extendedPriceTime']/1000)?> EST.</span>
                </dd>
                <?php endif?>
            </dl>
        <?php else:?>
            <dl>
                <dt>
                    <?=$stock?> not found
                </dt>
            </dl>
        <?php endif?>
    <?php endforeach ?>
    <script type ="text/javascript" src="stockresults.tpl.js"></script>
    </div>
<?php endif?>