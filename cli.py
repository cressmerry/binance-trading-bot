import typer
import logging
from rich import print
from rich.console import Console
from rich.table import Table
from typing import Optional
from bot.orders import execute_order
from bot.logging_config import setup_logging

app = typer.Typer(help="Binance Futures Testnet Trading Bot CLI")
console = Console()

setup_logging()
logger = logging.getLogger("trading_bot")

@app.command()
def place_order(
    symbol: str = typer.Option(..., prompt="Trading Symbol", help="Trading symbol (e.g., BTCUSDT)"),
    side: str = typer.Option(..., prompt="Order Side (BUY/SELL)", help="Order side (BUY or SELL)"),
    order_type: str = typer.Option(..., prompt="Order Type (MARKET/LIMIT/STOP_LOSS)", help="Order type (MARKET, LIMIT, STOP_LOSS)"),
    quantity: float = typer.Option(..., prompt="Quantity", help="Quantity to trade"),
    price: Optional[float] = typer.Option(None, help="Price for LIMIT orders"),
    stop_price: Optional[float] = typer.Option(None, help="Stop Price for STOP orders"),
):
    console.print(f"[bold blue]Starting Order Process for {symbol}...[/bold blue]")
    
    try:
        table = Table(title="Order Request Summary")
        table.add_column("Parameter", style="cyan")
        table.add_column("Value", style="magenta")
        table.add_row("Symbol", symbol)
        table.add_row("Side", side)
        table.add_row("Type", order_type)
        table.add_row("Quantity", str(quantity))
        
        if order_type.upper() == "LIMIT":
            table.add_row("Price", str(price))
        
        if stop_price:
            table.add_row("Stop Price", str(stop_price))

        console.print(table)

        if not typer.confirm("Do you want to proceed with this order?"):
            console.print("[yellow]Order cancelled by user.[/yellow]")
            raise typer.Abort()

        console.print("[blue]Sending order to Binance...[/blue]")
        response = execute_order(symbol, side, order_type, quantity, price, stop_price)
        
        console.print("[bold green]Order Placed Successfully![/bold green]")
        
        result_table = Table(title="Order Result")
        result_table.add_column("Field", style="cyan")
        result_table.add_column("Value", style="green")
        
        result_table.add_row("Order ID", str(response.get('orderId')))
        result_table.add_row("Status", str(response.get('status')))
        result_table.add_row("Executed Qty", str(response.get('executedQty', '0')))
        result_table.add_row("Avg Price", str(response.get('avgPrice', '0')))
        result_table.add_row("Type", str(response.get('type')))
        result_table.add_row("Side", str(response.get('side')))
        
        console.print(result_table)
        logger.info(f"Order executed: {response}")

    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {e}")
        logger.error(f"CLI Error: {e}")
        raise typer.Exit(code=1)

if __name__ == "__main__":
    app()
