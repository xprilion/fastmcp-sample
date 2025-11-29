"""Main entry point for the FastMCP Todo Server."""

import os
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
    
    # Get port from environment variable (Cloud Run requirement) or default to 8000
    port = int(os.getenv("PORT", 8000))
    
    # Run the server
    mcp.run(transport="http", port=port)
