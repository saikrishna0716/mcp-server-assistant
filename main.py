# server.py
from mcp.server.fastmcp import FastMCP
import os

# Create an MCP server
mcp = FastMCP("Demo")

notes_file = '/Users/saikrishna/Desktop/Github/mcp server/mcp-server-demo/notes.txt'

def ensure_file():
    if not os.path.exists(notes_file):
        with open(notes_file,"w") as f:
            f.write("Hello")


# Add Notes
@mcp.tool()
def add_notes(message: str) -> str:

    """Add notes to text file
        Args:
            message (str): text to be added to note file
        Returns:
            str: confirmation that note is added
    """
    ensure_file()
    
    with open(notes_file,"a") as f:
            f.write(message + "\n")

    return 'Note Saved'


# Add an addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return f'Sum of inputs: {a + b}'


# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"