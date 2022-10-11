WITH mint_data as (
    SELECT (amount0/1e18) as eth_amount,
           (amount1/1e6) as usdt_amount,
           date_trunc('minute', m.evt_block_time) as day
FROM uniswap_v2."Pair_evt_Mint" m
WHERE m.contract_address = '\x0d4a11d5eeaac28ec3f61d100daf4d40471f1852'
    ),

    burn_data as (
SELECT (amount0/1e18) as eth_amount,
    (amount1/1e6) as usdt_amount,
    date_trunc('minute', evt_block_time) as day
FROM uniswap_v2."Pair_evt_Burn"
WHERE contract_address = '\x0d4a11d5eeaac28ec3f61d100daf4d40471f1852'
    ),

    swap_data AS (
SELECT ("amount0In" - "amount0Out")/1e18 as eth_amount,
    ("amount1In" - "amount1Out")/1e6 as usdt_amount,
    date_trunc('minute', evt_block_time) as day
FROM uniswap_v2."Pair_evt_Swap"
WHERE contract_address = '\x0d4a11d5eeaac28ec3f61d100daf4d40471f1852'
    ),

    mint_grouped AS (
SELECT day, SUM(mint_data.usdt_amount) as usdt_amount , SUM(mint_data.eth_amount) as eth_amount
FROM mint_data
GROUP BY 1
    ),

    burn_grouped AS (
SELECT day, SUM(-1*burn_data.usdt_amount) as usdt_amount, SUM(-1*burn_data.eth_amount) as eth_amount
FROM burn_data
GROUP BY 1
    ),


    swap_grouped AS (
SELECT day, SUM(swap_data.usdt_amount) as usdt_amount, SUM(swap_data.eth_amount) as eth_amount
FROM swap_data
GROUP BY 1
    ),

    usdt_difference AS (
SELECT day, usdt_amount
FROM mint_grouped
UNION
SELECT day, usdt_amount
FROM burn_grouped
UNION
SELECT day, usdt_amount
FROM swap_grouped
    ),

    usdt_time as (
SELECT day, SUM(usdt_amount) OVER (ORDER BY day) as usdt_amt from usdt_difference
    ),

    usdt_with_price as (
SELECT day, usdt_amt * usdt.price as usdt_usd
FROM usdt_time t
    INNER JOIN prices."usd_dac17f958d2ee523a2206206994597c13d831ec7" usdt ON t.day = usdt.minute
    ),

    eth_difference AS (
SELECT day, eth_amount
FROM mint_grouped
UNION
SELECT day, eth_amount
FROM burn_grouped
UNION
SELECT day, eth_amount
FROM swap_grouped
    ),

    eth_time as (
SELECT day, SUM(eth_amount) OVER (ORDER BY day) as eth_amt from eth_difference
    ),

    eth_with_price as (
SELECT day, eth_amt * eth.price as eth_usd
FROM eth_time t
    INNER JOIN prices."layer1_usd_eth" eth ON t.day = eth.minute
    )

SELECT e.day, eth_usd + usdt_usd as pair_usd
FROM eth_with_price e INNER JOIN usdt_with_price a ON e.day = a.day
WHERE e.day >= now() - interval '6 months'