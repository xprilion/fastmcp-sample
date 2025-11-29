# Todo Management MCP Server

A minimal FastMCP server for managing todos over the Model Context Protocol.

## Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Initialize the database:**
   ```bash
   python setup_db.py
   ```

3. **Run the server:**
   ```bash
   python main.py
   ```

The server will start on `http://localhost:8000`.

## Available Tools

- `create_todo(title, description=None)` - Create a new todo item
- `list_todos(completed=None)` - List all todos (optionally filter by completion)
- `get_todo(todo_id)` - Get a specific todo by ID
- `update_todo(todo_id, title=None, description=None, completed=None)` - Update a todo
- `delete_todo(todo_id)` - Delete a todo by ID

## Project Structure

- `main.py` - Server entry point
- `database.py` - SQLite database operations
- `models.py` - Data models
- `tools.py` - MCP tool definitions
- `setup_db.py` - Database initialization script
- `todos.db` - SQLite database (created after setup)

