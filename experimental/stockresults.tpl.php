<?php if (!empty($resultData)):?>
    <div class ="stock-list">
    <?php
        $array = explode(",",strtoupper(str_replace(' ', '', $_GET['stocks'])));
    ?>
    <?php foreach ($array as $stock):?>
        <dl>
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
    <?php endforeach ?>
    </div>
<?php endif?>