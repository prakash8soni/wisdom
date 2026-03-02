#!/usr/bin/env python3
"""
Mem0 Memory Integration for Wisdom AI
Provides persistent, intelligent memory storage and retrieval
"""

import os
import json
from datetime import datetime
from mem0 import Memory

# Configuration
MEMORY_DIR = os.path.expanduser("~/.openclaw/workspace/memory")
MEMORY_DB = os.path.join(MEMORY_DIR, "mem0_db")

# Simple configuration without external dependencies
config = {
    "version": "v1.1",
}

# Try to initialize with full config, fall back to simple mode
try:
    m = Memory.from_config(config)
    print("✓ Mem0 initialized with full features")
except Exception as e:
    print(f"Note: Full mem0 features require additional setup: {e}")
    print("Using file-based memory as primary (mem0 will use OpenAI if configured)")
    m = None

def add_memory(content, user_id="prakash", metadata=None):
    """Add a new memory"""
    if not m:
        return None
    
    if metadata is None:
        metadata = {
            "timestamp": datetime.utcnow().isoformat(),
            "source": "wisdom_ai"
        }
    
    result = m.add(content, user_id=user_id, metadata=metadata)
    return result

def search_memory(query, user_id="prakash", limit=5):
    """Search memories"""
    if not m:
        return []
    
    results = m.search(query, user_id=user_id, limit=limit)
    return results

def get_all_memories(user_id="prakash"):
    """Get all memories for a user"""
    if not m:
        return []
    
    memories = m.get_all(user_id=user_id)
    return memories

def delete_memory(memory_id):
    """Delete a specific memory"""
    if not m:
        return False
    
    m.delete(memory_id)
    return True

def update_memory(memory_id, content):
    """Update a specific memory"""
    if not m:
        return None
    
    result = m.update(memory_id, content)
    return result

# CLI interface
if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python mem0_client.py <command> [args]")
        print("Commands: add, search, list, delete")
        sys.exit(1)
    
    command = sys.argv[1]
    
    if command == "add":
        if len(sys.argv) < 3:
            print("Usage: python mem0_client.py add <content>")
            sys.exit(1)
        content = " ".join(sys.argv[2:])
        result = add_memory(content)
        print(f"Added memory: {result}")
    
    elif command == "search":
        if len(sys.argv) < 3:
            print("Usage: python mem0_client.py search <query>")
            sys.exit(1)
        query = " ".join(sys.argv[2:])
        results = search_memory(query)
        for r in results:
            print(f"- {r['memory']}")
    
    elif command == "list":
        memories = get_all_memories()
        for mem in memories:
            print(f"[{mem.get('id', 'unknown')}] {mem.get('memory', 'no content')}")
    
    elif command == "delete":
        if len(sys.argv) < 3:
            print("Usage: python mem0_client.py delete <memory_id>")
            sys.exit(1)
        memory_id = sys.argv[2]
        delete_memory(memory_id)
        print(f"Deleted memory: {memory_id}")
    
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)