"""MCP tool definitions for todo management."""

from typing import Optional, List, Dict, Any
from fastmcp import FastMCP
import database


def register_tools(mcp: FastMCP):
    """Register all todo management tools with the MCP server."""
    
    @mcp.tool
    def create_todo(title: str, description: Optional[str] = None) -> Dict[str, Any]:
        """
        Create a new todo item.
        
        Args:
            title: The title of the todo item (required)
            description: Optional description for the todo item
        
        Returns:
            The created todo item
        """
        return database.create_todo(title, description)
    
    @mcp.tool
    def list_todos(completed: Optional[bool] = None) -> List[Dict[str, Any]]:
        """
        List all todo items, optionally filtered by completion status.
        
        Args:
            completed: Optional filter - True for completed, False for incomplete, None for all
        
        Returns:
            List of todo items
        """
        return database.get_all_todos(completed)
    
    @mcp.tool
    def get_todo(todo_id: int) -> Optional[Dict[str, Any]]:
        """
        Get a specific todo item by ID.
        
        Args:
            todo_id: The ID of the todo item to retrieve
        
        Returns:
            The todo item if found, None otherwise
        """
        return database.get_todo_by_id(todo_id)
    
    @mcp.tool
    def update_todo(
        todo_id: int,
        title: Optional[str] = None,
        description: Optional[str] = None,
        completed: Optional[bool] = None
    ) -> Optional[Dict[str, Any]]:
        """
        Update a todo item. You can update any combination of title, description, or completion status.
        
        Args:
            todo_id: The ID of the todo item to update
            title: Optional new title
            description: Optional new description
            completed: Optional completion status (True for completed, False for incomplete)
        
        Returns:
            The updated todo item if found, None otherwise
        """
        return database.update_todo(todo_id, title, description, completed)
    
    @mcp.tool
    def delete_todo(todo_id: int) -> Dict[str, Any]:
        """
        Delete a todo item by ID.
        
        Args:
            todo_id: The ID of the todo item to delete
        
        Returns:
            A dictionary indicating success or failure
        """
        deleted = database.delete_todo(todo_id)
        return {
            "success": deleted,
            "message": "Todo deleted successfully" if deleted else "Todo not found"
        }

