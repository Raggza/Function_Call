import requests
import json


def get_market_info_token(tokenSymbol: str, actionType: str, interval: str = "7 days"):
    symbol_to_id = {
        "btc": "bitcoin",
        "eth": "ethereum",
        "ltc": "litecoin",
        "xrp": "ripple",
        "ada": "cardano",
        "dot": "polkadot",
        "link": "chainlink",
        "uni": "uniswap",
        "aave": "aave",
        "sol": "solana",
        "matic": "matic-network",
        "avax": "avalanche-2",
        "atom": "cosmos",
        "fil": "filecoin",
        "theta": "theta-token",
        "vet": "vechain",
        "eos": "eos",
        "trx": "tron",
        "xlm": "stellar",
        "neo": "neo",
        "algo": "algorand",
        "dash": "dash",
        "zec": "zcash",
        "xtz": "tezos",
        "xmr": "monero",
        "bsv": "bitcoin-cash-sv",
        "iota": "iota",
        "doge": "dogecoin",
        "bch": "bitcoin-cash",
        "zil": "zilliqa",
        "ont": "ontology",
        "bat": "basic-attention-token",
        "zrx": "0x",
        "icx": "icon",
        "omg": "omisego",
        "enj": "enjincoin",
        "qtum": "qtum",
        "waves": "waves",
        "ksm": "kusama",
        "ren": "republic-protocol",
        "btt": "bittorrent-2",
        "hbar": "hedera-hashgraph",
    }
    if tokenSymbol not in symbol_to_id:
        return "not supported token symbol"

    token_id = symbol_to_id[tokenSymbol]

    url = f"https://api.coingecko.com/api/v3/simple/price?ids={token_id}&vs_currencies=usd&include_market_cap=true&include_24hr_vol=true&include_24hr_change=true&include_last_updated_at=true"
    response = requests.get(url)
    data = response.json()

    result = {}
    if actionType.lower() == "market cap":
        result["market_cap"] = data[token_id]["usd_market_cap"]
    elif actionType.lower() == "volume":
        result["volume"] = data[token_id]["usd_24h_vol"]
    elif actionType.lower() == "price":
        result["price"] = data[token_id]["usd"]
    elif actionType.lower() == "fdv":
        # CoinGecko API does not provide FDV directly, you might need to calculate it or fetch from another endpoint if available
        result["fdv"] = "FDV data not directly available"
    else:
        return json.dumps(
            "Invalid action type provided. Valid options are 'market cap', 'volume', 'price', 'fdv'."
        )

    return json.dumps(result)


def get_portfolio(threadId: str):
    db = {
        "u001": {
            "userId": "u001",
            "portfolio": {"USD": 1500.00, "BTC": 0.5, "ETH": 2.0, "LTC": 5.0},
        },
        "u002": {
            "userId": "u002",
            "portfolio": {"USD": 3200.00, "BTC": 0.25, "ETH": 1.5, "XRP": 3000},
        },
        "u003": {
            "userId": "u003",
            "portfolio": {"USD": 2100.00, "BTC": 0.75, "ETH": 2.5, "ADA": 400},
        },
        "u004": {
            "userId": "u004",
            "portfolio": {"USD": 1800.00, "BTC": 0.3, "ETH": 1.0, "DOT": 50},
        },
        "u005": {
            "userId": "u005",
            "portfolio": {"USD": 2500.00, "BTC": 0.2, "ETH": 1.8, "LINK": 100},
        },
        "u006": {
            "userId": "u006",
            "portfolio": {"USD": 1200.00, "BTC": 0.1, "ETH": 0.5, "UNI": 75},
        },
        "u007": {
            "userId": "u007",
            "portfolio": {"USD": 4000.00, "BTC": 0.8, "ETH": 3.0, "AAVE": 20},
        },
        "u008": {
            "userId": "u008",
            "portfolio": {"USD": 2800.00, "BTC": 0.6, "ETH": 2.2, "SOL": 30},
        },
        "u009": {
            "userId": "u009",
            "portfolio": {"USD": 1000.00, "BTC": 0.05, "ETH": 0.8, "MATIC": 500},
        },
        "u010": {
            "userId": "u010",
            "portfolio": {"USD": 3500.00, "BTC": 0.4, "ETH": 2.0, "AVAX": 40},
        },
        "u011": {
            "userId": "u011",
            "portfolio": {"USD": 2200.00, "BTC": 0.15, "ETH": 1.2, "ATOM": 60},
        },
        "u012": {
            "userId": "u012",
            "portfolio": {"USD": 1600.00, "BTC": 0.35, "ETH": 1.5, "FIL": 80},
        },
        "u013": {
            "userId": "u013",
            "portfolio": {"USD": 2900.00, "BTC": 0.7, "ETH": 2.8, "THETA": 200},
        },
        "u014": {
            "userId": "u014",
            "portfolio": {"USD": 1900.00, "BTC": 0.45, "ETH": 1.8, "VET": 10000},
        },
        "u015": {
            "userId": "u015",
            "portfolio": {"USD": 2700.00, "BTC": 0.3, "ETH": 2.2, "EOS": 150},
        },
        "u016": {
            "userId": "u016",
            "portfolio": {"USD": 3800.00, "BTC": 0.9, "ETH": 3.5, "TRX": 20000},
        },
        "u017": {
            "userId": "u017",
            "portfolio": {"USD": 1400.00, "BTC": 0.2, "ETH": 1.0, "XLM": 3000},
        },
        "u018": {
            "userId": "u018",
            "portfolio": {"USD": 2300.00, "BTC": 0.55, "ETH": 2.0, "NEO": 80},
        },
        "u019": {
            "userId": "u019",
            "portfolio": {"USD": 3100.00, "BTC": 0.65, "ETH": 2.5, "ALGO": 500},
        },
        "u020": {
            "userId": "u020",
            "portfolio": {"USD": 2000.00, "BTC": 0.4, "ETH": 1.8, "DASH": 10},
        },
        "u021": {
            "userId": "u021",
            "portfolio": {"USD": 1700.00, "BTC": 0.25, "ETH": 1.2, "ZEC": 15},
        },
        "u022": {
            "userId": "u022",
            "portfolio": {"USD": 2600.00, "BTC": 0.6, "ETH": 2.2, "XTZ": 200},
        },
        "u023": {
            "userId": "u023",
            "portfolio": {"USD": 3300.00, "BTC": 0.8, "ETH": 3.0, "XMR": 5},
        },
        "u024": {
            "userId": "u024",
            "portfolio": {"USD": 1300.00, "BTC": 0.15, "ETH": 0.8, "BSV": 3},
        },
        "u025": {
            "userId": "u025",
            "portfolio": {"USD": 2400.00, "BTC": 0.5, "ETH": 2.0, "IOTA": 1000},
        },
        "u026": {
            "userId": "u026",
            "portfolio": {"USD": 3600.00, "BTC": 0.7, "ETH": 2.8, "DOGE": 50000},
        },
        "u027": {
            "userId": "u027",
            "portfolio": {"USD": 1100.00, "BTC": 0.1, "ETH": 0.5, "BCH": 2},
        },
        "u028": {
            "userId": "u028",
            "portfolio": {"USD": 2800.00, "BTC": 0.6, "ETH": 2.2, "ZIL": 10000},
        },
        "u029": {
            "userId": "u029",
            "portfolio": {"USD": 3900.00, "BTC": 0.85, "ETH": 3.2, "ONT": 500},
        },
        "u030": {
            "userId": "u030",
            "portfolio": {"USD": 1800.00, "BTC": 0.3, "ETH": 1.5, "BAT": 1000},
        },
        "u031": {
            "userId": "u031",
            "portfolio": {"USD": 2500.00, "BTC": 0.55, "ETH": 2.0, "ZRX": 800},
        },
        "u032": {
            "userId": "u032",
            "portfolio": {"USD": 3400.00, "BTC": 0.75, "ETH": 2.8, "ICX": 300},
        },
        "u033": {
            "userId": "u033",
            "portfolio": {"USD": 1200.00, "BTC": 0.2, "ETH": 1.0, "OMG": 100},
        },
        "u034": {
            "userId": "u034",
            "portfolio": {"USD": 2700.00, "BTC": 0.65, "ETH": 2.5, "ENJ": 500},
        },
        "u035": {
            "userId": "u035",
            "portfolio": {"USD": 3800.00, "BTC": 0.9, "ETH": 3.5, "QTUM": 80},
        },
        "u036": {
            "userId": "u036",
            "portfolio": {"USD": 1500.00, "BTC": 0.25, "ETH": 1.2, "WAVES": 50},
        },
        "u037": {
            "userId": "u037",
            "portfolio": {"USD": 2200.00, "BTC": 0.5, "ETH": 2.0, "KSM": 10},
        },
        "u038": {
            "userId": "u038",
            "portfolio": {"USD": 3100.00, "BTC": 0.7, "ETH": 2.8, "REN": 1000},
        },
        "u039": {
            "userId": "u039",
            "portfolio": {"USD": 2000.00, "BTC": 0.35, "ETH": 1.5, "BTT": 100000},
        },
        "u040": {
            "userId": "u040",
            "portfolio": {"USD": 2900.00, "BTC": 0.6, "ETH": 2.2, "HBAR": 5000},
        },
    }
    # Fetch the user data from the simulated database
    if threadId in db:
        user_data = db[threadId]
        return json.dumps(user_data["portfolio"])
    else:
        return json.dumps(
            "threadId not found. you should ask the user for their ThreadID"
        )
