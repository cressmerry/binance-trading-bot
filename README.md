# Binance Futures Testnet Trading Bot

A Python CLI application to place orders on Binance Futures Testnet.

## Features
- Place **MARKET** and **LIMIT** orders.
- Supports **BUY** (Long) and **SELL** (Short) sides.
- Interactive CLI with validation.
- Logs requests and responses to `trading_bot.log`.

## Setup

1. **Clone the repository** (or unzip the folder).
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Configure Environment**:
   - Copy `.env.example` to `.env`:
     ```bash
     cp .env.example .env
     ```
   - Edit `.env` and add your **Binance Futures Testnet** API Key and Secret.
     - Get keys from: [https://testnet.binancefuture.com/en/futures](https://testnet.binancefuture.com/en/futures) (Log in -> API Key)

## Usage

Run the CLI from the `trading_bot` directory.

### Place a Market Order
Buy 0.005 BTC at market price (must be > 100 USDT):
```bash
python cli.py --symbol BTCUSDT --side BUY --order-type MARKET --quantity 0.005
```

### Place a Limit Order
Sell 0.005 BTC at $90,000 (must be close to current market price):
```bash
python cli.py --symbol BTCUSDT --side SELL --order-type LIMIT --quantity 0.005 --price 90000
```

### Place a Take-Profit Order
Trigger a Market Sell when price rises to $100,000:
```bash
python cli.py --symbol BTCUSDT --side SELL --order-type TAKE_PROFIT_MARKET --quantity 0.005 --stop-price 100000
```

### Help
```bash
python cli.py --help
```

## Structure
- `bot/`: Core logic (Client, Orders, Validators, Logging)
- `cli.py`: Entry point
- `trading_bot.log`: Log file (created after running)

## Assumptions
- User has valid Binance Futures Testnet keys.
- Network connection to Binance API is available.
- Symbol `BTCUSDT` is used for examples, but any valid futures symbol works.
