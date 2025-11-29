"""Main entry point for the FastMCP Todo Server."""

from fastmcp import FastMCP
import database
import tools

# Initialize the MCP server
mcp = FastMCP("Todo Management Server")

# Register all tools
tools.register_tools(mcp)

if __name__ == "__main__":
    # Initialize database on startup
    database.init_database()
    
    # Run the server
    mcp.run(transport="http", port=8000)
