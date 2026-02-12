import os
from binance.client import Client
from binance.exceptions import BinanceAPIException
from dotenv import load_dotenv
import logging

load_dotenv()

logger = logging.getLogger("trading_bot")

class BinanceClient:
    def __init__(self):
        self.api_key = os.getenv("BINANCE_TESTNET_API_KEY")
        self.api_secret = os.getenv("BINANCE_TESTNET_API_SECRET")

        if not self.api_key or not self.api_secret:
            logger.error("API credentials missing in .env file.")
            raise ValueError("API credentials (BINANCE_TESTNET_API_KEY, BINANCE_TESTNET_API_SECRET) must be set in .env file.")

        logger.info("Initializing Binance Client for Testnet...")
        self.client = Client(self.api_key, self.api_secret, testnet=True)
        logger.info("Binance Client initialized successfully.")

    def get_account_info(self):
        try:
            return self.client.futures_account()
        except BinanceAPIException as e:
            logger.error(f"Failed to fetch account info: {e}")
            raise

    def place_order(self, symbol, side, order_type, quantity, price=None, stop_price=None):
        try:
            params = {
                "symbol": symbol,
                "side": side,
                "type": order_type,
                "quantity": quantity,
            }
            if order_type == "LIMIT":
                params["price"] = price
                params["timeInForce"] = "GTC"
            
            if stop_price:
                params["stopPrice"] = stop_price
                if params["type"] == "STOP_LOSS":
                    params["type"] = "STOP_MARKET" 


            logger.info(f"Sending order request: {params}")
            order = self.client.futures_create_order(**params)
            logger.info(f"Order placed successfully: {order}")
            return order

        except BinanceAPIException as e:
            logger.error(f"Binance API Error: {e.status_code} - {e.message}")
            raise
        except Exception as e:
            logger.error(f"Unexpected error placing order: {str(e)}")
            raise
