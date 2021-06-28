assets_querys = [
    {
        "asset": "BTC",
        "entry_point": { "xpath": "//a[contains(@href,'/currencies/bitcoin/')]"},
        "statistics": {
            "xpath": {
                "bit_coin_price": "//*[@class='sc-16r8icm-0 dvhdfY']/div[1]/div[1]/table/tbody/tr[1]/td",
                "price_change": "//*[@class='sc-16r8icm-0 dvhdfY']/div[1]/div[1]/table/tbody/tr[2]/td/span",
                "low_24h": "//*[@class='sc-16r8icm-0 dvhdfY']/div[1]/div[1]/table/tbody/tr[3]/td/div[1]",
                "high_24h": "//*[@class='sc-16r8icm-0 dvhdfY']/div[1]/div[1]/table/tbody/tr[3]/td/div[2]",
                "trading_volume": "//*[@class='sc-16r8icm-0 dvhdfY']/div[1]/div[1]/table/tbody/tr[4]/td/span",
                "volume": "//*[@class='sc-16r8icm-0 dvhdfY']/div[1]/div[1]/table/tbody/tr[5]/td",
                "market_dominance": "//*[@class='sc-16r8icm-0 dvhdfY']/div[1]/div[1]/table/tbody/tr[6]/td",
                "market_rank": "//*[@class='sc-16r8icm-0 dvhdfY']/div[1]/div[1]/table/tbody/tr[7]/td",
                "circulating_supply": "//*[@class='sc-16r8icm-0 dvhdfY']/div/div[3]/div[3]/table/tbody/tr[1]/td",
                "total_supply": "//*[@class='sc-16r8icm-0 dvhdfY']/div/div[3]/div[3]/table/tbody/tr[2]/td",
                "max_supply": "//*[@class='sc-16r8icm-0 dvhdfY']/div/div[3]/div[3]/table/tbody/tr[3]/td"
            }
        },
        "buttons": {
            "xpath": {
                "cookie_button": "//*[@id='cmc-cookie-policy-banner']/div[2]",
                "show_more_button": "//*[@class='sc-16r8icm-0 jIZLYs container___E9axz']/*[@class='x0o17e-0 dDXPcp']"
            }
        }
    }
]
