"""Data models for the todo application."""

from typing import Optional
from dataclasses import dataclass


@dataclass
class Todo:
    """Todo item model."""
    id: int
    title: str
    description: Optional[str]
    completed: bool
    created_at: str
    updated_at: str
    
    def to_dict(self) -> dict:
        """Convert todo to dictionary."""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "completed": bool(self.completed),
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }

