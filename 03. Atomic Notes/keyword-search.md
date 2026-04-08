---
title: "Keyword Search"
type: atom
tags:
  - knowledge-management
  - search
---

Keyword search arrived when I started working with an AI collaborator. The problem wasn't that I couldn't find things. The problem was tokens.

Structured properties are great for human navigation but expensive when an LLM has to ingest an entire file just to read them. Keyword search narrows the target before the AI ever sees the content. Find the files that mention "FIDO2", feed only those to the model. A targeting mechanism that helps solve [[the-context-bottleneck|the context bottleneck]].

Keyword finds exact terms instantly but misses conceptually related content. That's where [[semantic-search|semantic search]] compensates. Together with [[metadata-search]] and [[the-link-graph|the link graph]], they form the [[four-modalities-of-search|four modalities]].
