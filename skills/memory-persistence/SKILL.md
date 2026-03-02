---
name: memory-persistence
description: Persistent memory system for Wisdom AI. Ensures all important memories, learnings, and context are automatically saved and backed up to GitHub. Use when: (1) Storing important information about the user or preferences, (2) Learning from mistakes or successes, (3) Updating long-term memory, (4) Before any session ends or during heartbeats, (5) When user says "remember this" or similar.
---

# Memory Persistence Skill

This skill ensures Wisdom never loses important memories. All data is automatically backed up to GitHub.

## Memory Structure

```
memory/
├── YYYY-MM-DD.md      # Daily notes (raw logs)
├── heartbeat-state.json # Track periodic checks
MEMORY.md              # Long-term curated memories
```

## Core Principles

1. **Write EVERYTHING important** - If it matters, write it to a file
2. **Daily logs first** - Put raw notes in `memory/YYYY-MM-DD.md`
3. **Curate into MEMORY.md** - Distill important learnings weekly
4. **Auto-backup to GitHub** - Every commit preserves history

## When to Save

### Always Save:
- User preferences and identity details
- Important decisions and their reasoning
- Mistakes made and lessons learned
- Connections between topics
- User's personal context (family, work, goals)

### During Heartbeats:
- Review recent conversations
- Extract meaningful moments
- Update `memory/YYYY-MM-DD.md`
- Periodically distill into MEMORY.md

### Before Session Ends:
- Summarize key points
- Commit and push to GitHub

## Memory Format

### Daily Notes (memory/YYYY-MM-DD.md)

```markdown
# YYYY-MM-DD

## Session Summary
Brief overview of what happened

## Key Events
- Event 1: Description
- Event 2: Description

## Learnings
- What worked: ...
- What didn't: ...

## User Context
- New information about user
- Preferences discovered
```

### Long-term Memory (MEMORY.md)

```markdown
# Long-Term Memory

## User Profile
- Name: Prakash Kumar Soni
- Preferred name: Prakash
- Timezone: UTC

## Preferences
- [Discovered preferences]

## Important Dates
- [Dates to remember]

## Ongoing Projects
- [Project details]

## Lessons Learned
- [Key takeaways from interactions]
```

## Git Backup Protocol

After updating memory files:
1. `git add memory/ MEMORY.md`
2. `git commit -m "Update memory: [brief description]"`
3. `git push origin main`

The GitHub Actions workflow will also auto-backup hourly.

## Self-Improvement Protocol

1. **After mistakes**: Document what went wrong and how to avoid it
2. **After successes**: Note what worked well for future reference
3. **Pattern recognition**: Identify recurring themes in user interactions
4. **Skill updates**: Improve this skill based on experience

## Memory Systems

### 1. File-Based Memory (Primary)
- **Daily logs:** `memory/YYYY-MM-DD.md`
- **Long-term:** `MEMORY.md`
- **GitHub backup:** Automatic hourly + on commits

### 2. Mem0 Intelligent Memory (Enhanced)
- **Vector database:** Semantic search across all memories
- **Smart retrieval:** Context-aware memory recall
- **Location:** `~/.openclaw/workspace/memory/mem0_db/`

## Quick Commands

```bash
# File-based memory (fast, simple)
echo "\n## $(date '+%H:%M') - Event description" >> memory/$(date '+%Y-%m-%d').md

# Mem0 intelligent memory (semantic search)
/root/.openclaw/venv/bin/python scripts/mem0_client.py add "Important memory content"
/root/.openclaw/venv/bin/python scripts/mem0_client.py search "query"
/root/.openclaw/venv/bin/python scripts/mem0_client.py list

# Git backup
git add memory/ MEMORY.md && git commit -m "Update memory" && git push
```