# How to Use This as Your Own Vault

This repo isn't just something to read. It's something to fork, extend, and make your own. Here's how to experience the Zettelkasten method in under 10 minutes using my thinking as a starting point.

## 1. Fork and clone

Fork this repo on GitHub, then clone it locally:

```
git clone https://github.com/YOUR-USERNAME/davebrear-ai.git
cd davebrear-ai
```

## 2. Point your AI at it

Open Claude Code (or any AI that reads local files) in the repo directory:

```
claude
```

Claude will read the CLAUDE.md file automatically and understand the vault structure.

## 3. Explore the network

Ask your AI to explore. Try:

- "Read the atom on ai-outputs-are-inputs and follow its links."
- "What are the stub notes in this vault? Which ones have open questions?"
- "Show me the graph around three-levels-of-ai-usage."

This is what it feels like to traverse a thought network. The AI walks the links, loads connected ideas, and builds a picture of the argument across multiple notes.

## 4. Write your first atom

Pick a stub note (look for notes with open questions or "I don't have an answer here"). Read it. Think about it. Then write your own atom in response.

Create a new file in `03. Atomic Notes/`:

```markdown
---
title: "Your Note Title"
type: atom
tags:
  - your-tags
---

Your thinking here. Write in first person. One idea per note.

Link to existing notes: I disagree with Dave's take on [[firewall-your-thinking]] because...

Or extend an idea: Building on [[compound-interest-on-thinking]], I've noticed that...
```

That's it. You've just added a node to the network.

## 5. Link it

The magic is in the links. Every `[[wiki-link]]` you add creates a connection in the graph. Link to Dave's atoms, link to your own, link to things that don't exist yet (they'll become notes later).

Ask your AI: "What existing notes in this vault relate to what I just wrote?" It will suggest connections you might not have seen.

## 6. Keep going

Add more atoms over days and weeks. Create your own MOC when you have 5-10 atoms on a topic. Write an output (a blog post, a presentation, an email) assembled from your atoms.

The system grows from use, not from planning. If it looks messy, that's fine. Structure emerges from the connections.

## Stub notes to get you started

These are deliberately unfinished atoms with open questions. They're invitations to think:

- `what-happens-when-everyone-has-a-second-brain.md` - the competitive advantage question
- `the-governance-gap.md` - enterprise DLP and context ownership
- `where-does-the-human-end-and-the-ai-begin.md` - authorship and AI influence
- `the-credential-problem.md` - static credentials vs dynamic capability
- `can-a-second-brain-be-shared.md` - personal vaults vs collaborative knowledge

Pick one. Disagree with it. Extend it. Answer the question I couldn't. That's how a Zettelkasten grows.
