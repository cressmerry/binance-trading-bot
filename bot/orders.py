import logging
from .client import BinanceClient
from .validators import validate_symbol, validate_side, validate_order_type, validate_quantity, validate_price, validate_stop_price

logger = logging.getLogger("trading_bot")

def execute_order(symbol: str, side: str, order_type: str, quantity: float, price: float = None, stop_price: float = None):
    try:
        logger.info("Validating order inputs...")
        symbol = validate_symbol(symbol)
        side = validate_side(side)
        order_type = validate_order_type(order_type)
        quantity = validate_quantity(quantity)
        if order_type == "LIMIT":
            price = validate_price(price, order_type)
        
        stop_price = validate_stop_price(stop_price, order_type)
        
        client = BinanceClient()

        response = client.place_order(symbol, side, order_type, quantity, price, stop_price)
        
        return response

    except ValueError as ve:
        logger.error(f"Validation Error: {ve}")
        raise
    except Exception as e:
        logger.error(f"Order Execution Failed: {e}")
        raise
