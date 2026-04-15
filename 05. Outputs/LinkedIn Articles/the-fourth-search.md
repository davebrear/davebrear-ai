---
title: "The Fourth Search: Semantic Search Is the Capstone, Not the Foundation"
type: article
date: 2026-03-02
summary: "I had three ways to search my second brain. Adding a fourth made the first three better."
source_url: ""
atoms:
  - "[[the-context-bottleneck]]"
  - "[[context-is-the-differentiator]]"
  - "[[four-modalities-of-search]]"
  - "[[keyword-search]]"
  - "[[metadata-search]]"
  - "[[the-link-graph]]"
  - "[[semantic-search]]"
  - "[[chaining-search-modalities]]"
  - "[[the-flywheel]]"
  - "[[human-judgement-vs-machine-understanding]]"
  - "[[thinking-residue]]"
  - "[[build-systems-people-think-inside]]"
  - "[[the-best-knowledge-layer-is-a-working-environment]]"
  - "[[the-ai-surfaces-connections-you-missed]]"
  - "[[optimising-context-for-ai]]"
  - "[[the-context-layer]]"
  - "[[compound-interest-on-thinking]]"
  - "[[links-do-the-work]]"
tags:
  - ai
  - knowledge-management
  - semantic-search
  - chain-of-cognition
---

*I had three ways to search my second brain. Adding a fourth made the first three better.*

Two months ago I started building a personal knowledge system. Not a bookmarking tool, not a document archive. A working environment. 500 notes and counting. I think inside it every day: developing arguments, connecting dots, capturing reasoning before it fades.

The vault started as a purely human system. Then I pointed Claude Code at it and everything changed. An AI that could read my files, remember my conventions, and build on previous work. That article was about the collaboration model. This one is about what happens next: once you have hundreds of notes of genuine thinking, how do you actually find the right context at the right time?

That's a retrieval problem. And it turns out retrieval has more dimensions than I expected.

## The context bottleneck

The most capable AI model in the world starts every conversation knowing nothing about you. Intelligence has scaled dramatically. Memory hasn't. Every new chat window is amnesia.

The people getting outsized value from AI aren't the ones using the smartest model. They're the ones who solved the context problem: building a persistent knowledge layer outside any single AI tool. Your notes, your structure, your thinking, accumulated over time, accessible on demand.

The best knowledge layer isn't a database you build for retrieval. It's a working environment you think inside. The notes aren't archived for later lookup. They're written as part of the thinking process. Retrieval is a byproduct of the thinking, not the purpose of it.

Which raises a practical question. At 500 notes averaging 2,000 tokens each, you're looking at a million tokens of raw content. That exceeds even the largest context windows before any conversation happens. How do you get the right 5-10 notes in front of the AI without burning the entire context window on everything else?

## Three modalities grew organically

Two things happened in parallel as my vault grew. The raw material (structured metadata, wiki-links between notes) accumulated naturally from daily use. I was thinking inside the system, not designing a retrieval layer. But the tooling to make that material queryable was deliberate engineering. The system taught me what it needed, then I built the machinery to unlock it.

**Metadata came first, before any search existed.** I wasn't thinking about retrieval. I was thinking about organisation. Every note got structured properties from the start: type, related project, status. This was human indexing, using the note app's built-in tools (filters, views, sorted tables) to keep 50, then 100, then 200 notes navigable. I was designing for my own eyes, not for a search algorithm. This was '2025 Dave' thinking, which in hindsight paid off in 2026 by becoming the foundation of everything.

**Keyword search arrived when I started working with an AI collaborator.** The problem wasn't that I couldn't find things. The problem was tokens. Structured properties are great for human navigation but expensive when an LLM has to ingest an entire file just to read them. I built keyword search to narrow the target before the AI ever saw the content. Find the files that mention "FIDO2", feed only those to the model. A targeting mechanism. Then I indexed the metadata separately, so structural queries ("all meetings for this project in the last month") could be answered without the AI touching a single file. The filing system I'd built for human navigation turned out to be a powerful structured query layer.

**The link graph emerged last, from the act of thinking.** When you link one note to another, you're making a deliberate assertion: these two ideas are connected. Over hundreds of notes, these links build into a web of relationships. The practical value was immediate: starting from a single note, I could traverse outward and load an entire chain of reasoning into the AI's context window in one step. A project note links to meeting notes, which link to related ideas, which link to other projects. One starting point, and the full context unfolds.

Then the AI started suggesting connections I'd missed. "This note makes the same argument as that one. Should they be linked?" More links meant richer traversals, which meant richer context, which meant the AI spotted more connections. A flywheel.

But one with a ceiling. The AI could only reason across whatever notes happened to be loaded in the session. It couldn't search the whole vault by concept. The capability was there, bottlenecked by the context window.

## Semantic search: the missing dimension

The ceiling on the flywheel told me what was missing. The AI was already doing semantic matching informally during conversations, spotting conceptual connections across whatever notes were loaded. But it could only reason over what was in the session. It couldn't search the whole vault by concept. The capability was there, bottlenecked by the context window.

The answer was semantic search: vector embeddings that represent meaning as numerical coordinates and compare them mathematically, finding conceptual overlap even when the vocabulary is completely different. I had a note called "Shadow AI Follows the Shadow IT Pattern." A keyword search for "enterprise security blocking AI adoption" would never find it. The words don't match. But the concepts are the same. Semantic search closes that gap and makes it vault-wide.

I was already building this over the weekend, when Nate B Jones published his OpenBrain video. His system also uses vector embeddings via MCP to give AI tools persistent, searchable memory. It was validating to see someone arrive at the same conclusion from a different starting point. His architecture is clean, his protocol choice is right, and the core insight (that AI memory should live outside any single model) matches what I'd found through use. The difference is where you start. OpenBrain starts with semantic search as the foundation. My system grew three other modalities first, and semantic search became the capstone that made all of them more powerful.

## Four modalities, compounded

| Modality     | What it finds      | Source of truth               | How it works                                     |
| ------------ | ------------------ | ----------------------------- | ------------------------------------------------ |
| **Keyword**  | What you said      | The words in the file         | Text search across files                         |
| **Metadata** | What you filed     | The structure you assigned    | Properties index                                 |
| **Graph**    | What you connected | The links you chose to create | Link web (think spider diagram, not folder tree) |
| **Semantic** | What you meant     | The concepts in the content   | Vector database                                  |

Each answers a different question. Each draws on a different source of truth. No single modality is sufficient. Each one fails in a way the others compensate for.

Keyword finds "FIDO2" instantly but misses a note about "passwordless hardware token authentication" that's exactly what you need. Semantic finds it. Semantic finds conceptually related notes but returns false positives. Keyword confirms or rejects. Metadata shows every meeting for a project but can't tell you which meetings keep circling back to the same unresolved question. Semantic clusters them by theme. Graph shows everything linked to a project but can't surface a note in a different project exploring the same idea under a different name. Semantic bridges the gap.

But here's where it gets interesting. The modalities don't just coexist. They chain.

**Keyword to Semantic.** Find a specific note by exact term, then ask "what else in my vault is conceptually related to this?" Precision first, then discovery.

**Semantic to Metadata.** Broad concept search returns 15 notes about AI adoption. Filter by type: just the meeting notes. Just the ideas. Just a specific project. The concept search casts a wide net. The metadata search sorts the catch.

**Graph to Semantic.** This is the most interesting composition. Start at a project note. Traverse the link graph: these are the notes I deliberately connected. Now run a semantic search for the same concepts. Compare the two result sets. The notes that semantic finds but graph doesn't are potential blind spots: connections I should have made but didn't. The notes that graph has but semantic doesn't are places where my judgment goes beyond what an embedding model can detect.

That gap, between what I connected and what the machine thinks is connected, is a structured view of your own blind spots. Semantic finds it, graph doesn't? Probably a link I should create. Graph has it, semantic doesn't? I know something the model doesn't. Both agree? High confidence. Neither finds it? It probably doesn't exist.

Three of the four modalities index things the machine can derive: words, properties, concepts. The graph indexes something only a human can create: deliberate judgment about how ideas relate. When an AI compares graph results against semantic results, it's comparing human understanding against machine understanding. **The delta between those two is the highest-signal space to operate in. This is where "second brain" stops being a metaphor and starts being architecture.**

## Why this matters beyond my vault

There are two ways to build a knowledge system. You can design a retrieval layer and populate it with information. Or you can build a working environment where people actually think, and let the retrieval capabilities grow from the work itself.

Most enterprise AI knowledge initiatives start with the first approach. Pick a vector database, ingest documents, build a search interface. The result is a system people query but don't work inside. The knowledge is static. Nobody is developing ideas in it, connecting concepts across it, or building a web of links that represents their judgment about how things relate. Single-modality retrieval over inert content.

The richest retrieval modalities grow from two things in combination. People doing real work inside the system: the metadata I query today exists because I was filing notes for my own navigation from day one. The link graph exists because I was connecting ideas as part of my thinking process. These are thinking residue. And deliberate engineering to make that residue queryable: the search tools, the indexer, the traversal engine, the embedding pipeline. Neither is sufficient alone. Rich content without tooling is a pile of notes. Tooling without rich content is an empty search box.

Semantic search completes the picture. It's the one modality that doesn't require the user to have done anything deliberate. It works on the raw content regardless of how well it was filed or linked. That's why it's the perfect complement to the modalities that grow from use. It covers the gaps that even disciplined knowledge work inevitably leaves.

The question for enterprises isn't "should we add AI search?" It's "are we building systems where people think and work, or just systems where people store things?"

I had three ways to search my second brain. The fourth didn't just add a capability. It multiplied three.
