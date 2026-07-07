import sys
from fastmcp import FastMCP

# 1. Initialize our localized MCP microservice instance
mcp = FastMCP("My First Local MCP Utility")

# 2. CREATE A STATIC RESOURCE (Information the AI can read as context)
@mcp.resource("system://info")
def get_system_manifest() -> dict:
    """Provides internal configuration details about this local machine environment."""
    return {
        "server_status": "Operational",
        "supported_features": ["character_counting", "safe_division"],
        "environment": "Local Prototype Development Workspace"
    }

# 3. CREATE A TOOL (An action function the LLM can actively choose to run)
@mcp.tool
def analyze_text_complexity(text: str) -> str:
    """
    Analyzes a given string of text, providing the total character count 
    and checking if it contains certain engineering safety flags.
    """
    # Write logs directly to standard error so they don't break the communication pipe
    sys.stderr.write(f"[MCP LOG] Running analyze_text_complexity tool on text payload.\n")
    
    char_count = len(text)
    contains_urgent = "URGENT" in text.upper()
    
    return (
        f"--- Text Analysis Complete ---\n"
        f"Total Characters: {char_count}\n"
        f"Contains High-Priority Safety Flags: {contains_urgent}"
    )

# 4. CREATE ANOTHER TOOL (A safe mathematical function)
@mcp.tool
def safe_divide_numbers(numerator: float, denominator: float) -> str:
    """Performs a calculation to divide a numerator by a denominator safely without crashing."""
    sys.stderr.write(f"[MCP LOG] Running safe_divide_numbers tool on parameters.\n")
    
    if denominator == 0:
        return "Operational Error: Division by zero parameters intercepted by the tool layer."
        
    result = numerator / denominator
    return f"The final calculation quotient is: {result:.4f}"

if __name__ == "__main__":
    # Runs the server using the standard input/output transport loop
    mcp.run()