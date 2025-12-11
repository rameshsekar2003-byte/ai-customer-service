import sys # Puthusa import panrom
from mcp.server.fastmcp import FastMCP

# 1. Create Server
mcp = FastMCP("weather_server")

# 2. Define Tool
@mcp.tool()
def get_weather(city: str) -> str:
    """Get the current weather for a specific city."""
    # Screen-la theriyurathukaga oru print poduvom (DEBUG)
    print(f"Request received for city: {city}", file=sys.stderr) 
    return f"The weather in {city} is Sunny, 25°C"

# 3. Run Server
if __name__ == "__main__":
    # Server start aagarathukku munadi oru message
    print("✅ Server is running! Waiting for AI to ask about weather...", file=sys.stderr)
    mcp.run()