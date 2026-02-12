from typing import Optional

def validate_symbol(symbol: str) -> str:
    if not symbol or not isinstance(symbol, str):
        raise ValueError("Symbol must be a non-empty string.")
    return symbol.upper()

def validate_quantity(quantity: float) -> float:
    if quantity <= 0:
        raise ValueError("Quantity must be greater than 0.")
    return quantity

def validate_price(price: Optional[float], order_type: str) -> Optional[float]:
    if order_type.upper() == "LIMIT":
        if price is None or price <= 0:
            raise ValueError("Price is required and must be greater than 0 for LIMIT orders.")
    return price

def validate_stop_price(stop_price: Optional[float], order_type: str) -> Optional[float]:
    if order_type.upper() in ["STOP_MARKET", "STOP_LOSS", "TAKE_PROFIT", "TAKE_PROFIT_MARKET"]:
        if stop_price is None or stop_price <= 0:
            raise ValueError("Stop Price is required and must be greater than 0 for Stop orders.")
    return stop_price

def validate_side(side: str) -> str:
    if side.upper() not in ["BUY", "SELL"]:
        raise ValueError("Side must be either BUY or SELL.")
    return side.upper()

def validate_order_type(order_type: str) -> str:
    if order_type.upper() not in ["MARKET", "LIMIT", "STOP_MARKET", "STOP_LOSS", "TAKE_PROFIT", "TAKE_PROFIT_MARKET"]:
        raise ValueError("Order type must be MARKET, LIMIT, STOP_MARKET, STOP_LOSS, TAKE_PROFIT, or TAKE_PROFIT_MARKET.")
    return order_type.upper()
