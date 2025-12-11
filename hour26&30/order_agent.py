from mcp.server.fastmcp import FastMCP
import sqlite3

# 1. Create the MCP Server
mcp = FastMCP("order_agent")

# 2. Define the Tool
@mcp.tool()
def get_order_status(order_id: str) -> str:
    """Get the status and delivery date for a specific order ID."""
    
    # Connect to the database
    # Ovvoru vaatiyum connect panni close panrom (Stateless)
    conn = sqlite3.connect('orders.db')
    cursor = conn.cursor()
    
    # Search for the order using Parameterized Query (Safety First! 🛡️)
    cursor.execute("SELECT status, delivery_date FROM orders WHERE order_id = ?", (order_id,))
    result = cursor.fetchone()
    
    conn.close()
    
    # Handle Result
    if result:
        status, delivery_date = result
        return f"Order {order_id} is currently {status}. Expected delivery: {delivery_date}"
    else:
        return f"Order {order_id} not found. Please check the Order ID."

# 3. Run Server
if __name__ == "__main__":
    mcp.run()