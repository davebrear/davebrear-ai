---
title: "Semantic Search"
type: atom
tags:
  - knowledge-management
  - search
  - semantic-search
---

The AI was already doing this. It would connect notes conceptually without being asked, just because they happened to be in the context window. "This note makes the same argument as that one." [[the-ai-surfaces-connections-you-missed|The AI surfaces connections I missed]]. I hadn't planned for it. Total accident.

But it could only work across whatever was loaded in the session. My note "Shadow AI Follows the Shadow IT Pattern" would never surface from a [[keyword-search]] for "enterprise security blocking AI adoption." Same concept, zero word overlap.

That's when I built vector search. Take what the AI was doing accidentally in-session and make it work across the whole vault. Embeddings, cosine similarity, the works. Turned out to be the missing piece that made [[keyword-search]], [[metadata-search]], and [[the-link-graph]] all more powerful. Three search modalities became four, but the result was more than additive.
