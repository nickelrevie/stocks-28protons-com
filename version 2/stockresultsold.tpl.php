<? if (!empty($resultData)):?>
    <div class ="stock-list">
    <? foreach ($resultData as $section):?>
        <dl>
            <dt>
                <?=$section['company']?> (<?=$section['symbol']?>)
            </dt>
            <dd>
                <span class = "price"><?=$section['latestPrice']?></span> <?=$section['change']?>
            </dd>
            <? if((strcmp($section['marketPhase'],"market")) != 0):?>
            <? date_default_timezone_set('America/New_York')?>
            <dd>
                <?=$section['extendedQuote']?> <span class = "market-phase"><?=$section['marketPhase']?> price as of <?=date('H:i', $section['extendedPriceTime']/1000)?> EST.</span>
            </dd>
            <? endif?>
        </dl>
    <? endforeach ?>
    </div>
<?endif?>