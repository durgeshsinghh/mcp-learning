import random
from fastmcp import FastMCP

# Create app
mcp = FastMCP(name="demo-server")


# 
@mcp.tool
def roll_dice(n_dice: int = 1) -> list[int]:
    """Roll dice and return results"""
    if n_dice < 1:
        raise ValueError("n_dice must be >= 1")
    return [random.randint(1, 6) for _ in range(n_dice)]


# ➕ Tool 2: Add Numbers
@mcp.tool
def add_numbers(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# 🚀 Entry point (IMPORTANT for cloud)
if __name__ == "__main__":
    mcp.run(transport="stdio")