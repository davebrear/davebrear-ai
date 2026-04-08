---
title: "How I Turn Scattered Ideas into Finished Writing (with AI)"
type: article
date: 2026-02-22
summary: "Geothermal thinking, linked notes, and why the process matters more than the tool."
source_url: ""
atoms:
  - "[[the-blue-lagoon-analogy]]"
  - "[[zettelkasten-as-thinking-system]]"
  - "[[one-idea-per-note]]"
  - "[[compound-interest-on-thinking]]"
  - "[[links-do-the-work]]"
  - "[[ai-as-infrastructure-for-thinking]]"
  - "[[the-ai-surfaces-connections-you-missed]]"
  - "[[think-alone-first]]"
  - "[[the-bullet-draft-method]]"
  - "[[the-two-paths-converge]]"
  - "[[the-writing-is-a-byproduct]]"
  - "[[ai-expands-not-compresses]]"
  - "[[echo-chamber-steering]]"
  - "[[ai-outputs-are-inputs]]"
  - "[[firewall-your-thinking]]"
  - "[[authorship-lives-in-judgement]]"
  - "[[ai-makes-thinking-harder-not-easier]]"
  - "[[deliberate-incompleteness]]"
  - "[[ai-as-co-thinker]]"
  - "[[ai-as-persistent-collaborator]]"
  - "[[ai-value-is-in-the-process]]"
  - "[[markdown-as-universal-format]]"
tags:
  - ai
  - zettelkasten
  - obsidian
  - writing
---

I just got back from a week in Iceland. The raw natural landscape floors you. Volcanic rock, glacial water, silence you can feel in your chest.

Then you visit the Blue Lagoon. It's stunning. But it's not entirely natural. The water is a byproduct of a geothermal power plant, pumped up from underground. Humans built the infrastructure. The minerals, the heat, the silica: that's all coming from the earth. You can't tell where nature ends and engineering begins. The result is better than either alone.

A week offline, away from the relentless pace of this space, gave me room to think about hybrids like this. Specifically, about my own thinking process. People have been asking me how I use Claude Code as a knowledge worker, not as a developer, and I've been giving them a very underwhelming demonstration. I talked with it in a terminal window, and good things happened. Which is way less impressive to demo than you are even imagining.

The problem is that the value isn't in the tool. It's in the process around it. Watching someone type into a terminal tells you nothing about why the output is good. This post is my attempt to document how I actually think and work, in a way that explains it better to those people. The thinking is the geothermal source. The AI is the infrastructure. The output is the lagoon.

This one's longer and more in the weeds than my previous posts. Grab a coffee as I explain my process end to end in detail.

## It starts with a slip box

A view I often hear: AI is making us stupid. That has not been my experience, so I have to wonder, am I engaging with AI in a meaningfully different way?

The answer, I think, starts not with the AI but with how I take notes.

Late last year I read Sonke Ahrens' *How to Take Smart Notes*. It introduced me to the Zettelkasten method, developed by the German sociologist Niklas Luhmann. Over his career, Luhmann published 70 books and nearly 400 academic articles. His secret wasn't discipline or genius. It turns out that it was actually a simple box known as a Zettelkasten.

Zettelkasten means "slip box" in German. Literally a wooden box filled with index-card-sized notes, each carrying a single idea, with hand-written reference numbers linking one card to another. The method is deceptively simple: one idea per note, linked to related notes. Don't organise by category. Let structure emerge from the connections.

Serendipity is the point. Unexpected connections between ideas surface naturally as the network grows. Over time, the network becomes a thinking partner. A conversation with your past self.

The cognitive benefits are real. Externalising ideas into small, focused notes reduces working memory load. You stop trying to hold the full argument in your head and let the network hold it for you. Linking forces you to articulate *why* two ideas relate, which deepens understanding. And because the notes accumulate over time, you build compound interest on your thinking. Today's half-formed thought becomes next month's breakthrough connection.

Ahrens himself makes the point that digital tools are what unlock this method for modern use. Thankfully we don't need a wooden box. A new generation of note-taking apps are built around the same principles as Luhmann's slip box: small focused notes, linked together, with structure emerging from the connections.

The key concept is a visible chain of thought. You can see how one idea leads to the next, follow the links, and watch an argument form across a network of connected notes. Same principles as Luhmann (atomic notes, emergent structure, connections over categories) but the friction is gone. Searching, linking, and traversing the network happens in seconds instead of minutes.

I started using this approach to capture thinking and ideas: reading highlights, half-baked concepts, threads I wanted to develop. The collection grew over time.

Then something unexpected happened. I stopped struggling to write. Not because writing got easier, but because by the time I sat down to write, the thinking was already done. It was sitting in the links.

## AI takes it further

I've written before about my first week with Claude Code. The tool was immediately impressive, but the real breakthrough wasn't the tool itself. It was using Claude not as a chatbot but as an agent that reads my files directly. This is where the Zettelkasten method and AI become more than the sum of their parts.

To be clear, the digital Zettelkasten on its own was already transformative. Traversing the links, re-reading notes, holding the chain of reasoning in your head. That's not a burden. It's the workout. Each time you walk the network you strengthen the thinking. The notes are the weights.

But there's a ceiling to what you can lift alone. As the network grows, so does the effort of holding the full picture in your head at once. AI changes the ceiling. Point it at a starting note and it follows the links. It walks the chain, reading each connected note, absorbing the full context. In seconds it has the complete thought network loaded. Something that would take me twenty minutes of clicking and re-reading.

But it goes beyond reading faster. It surfaces connections I missed. It challenges assumptions I'd glossed over. It can say "this note about X seems related to that note about Y" when I'd never have made the link myself. The network gets richer through collaboration.

## My tools

This workflow is tool-agnostic. Substitute whatever fits your stack. Here's mine:

I use **Obsidian** for note creation and linking. It's the thinking environment. Obsidian uses wiki-links (double brackets) to connect notes, and renders the connections as a navigable graph so you can literally see your chains of thought. All files are local, portable, plain markdown. Which turns out to be the ideal interchangeable file format in the AI age. No vendor lock-in, and every major AI reads markdown natively.

**Claude Code** is the AI collaborator. It reads my vault directly and works with me in the terminal.

A small **Python script** traverses wiki-links from any starting note, feeding Claude the full chain of connected ideas.

That's it. No plugins, no integrations, no complicated setup. Obsidian provides the structure. Claude provides the leverage. The script bridges them.

## The workflow in practice

This is the part most people skip when they hear "AI-assisted writing." They open a chat window and ask AI to generate something from nothing. That's using AI to compress. The workflow below uses AI to expand.

### 1. Think alone first

Open your note-taking tool. Create a new note with a single idea. One sentence or a short paragraph. Don't worry about where it fits. Just capture it.

When a second idea relates to the first, create another note and link them. In a single initial sitting, expel whatever ideas you have into viewable chains of thought. Get them out of your head and into the network.

Revisit and add to these chains over days or weeks. No outline, no structure, just ideas linked to other ideas. The links are doing the work: each one forces you to articulate a relationship between two thoughts.

Resist the urge to involve AI here. This is your thinking, raw and unmediated. You'll know there's enough when you can see a chain of 5-10 connected notes on a topic.

### 2. Load the context

Point your AI at the starting note and ask it to follow the links. Give it an explicit instruction: *"Read this note and every note it links to. Build a picture of the full argument."*

The AI walks the chain you've built, reading each connected note, absorbing the full context. It's not getting a cold prompt. It's getting your actual thought process, with all the connections and reasoning embedded in the structure.

Ask the AI to summarise what it sees. This is your first check on whether the chain holds together.

### 3. Expand and connect

Ask the AI: *"What's underdeveloped? What assumptions am I making? What's missing?"*

Flesh out thin ideas. Ask it to expand a specific note with questions or counter-arguments. Ask it to surface connections to other areas: *"Does this relate to anything else you've seen in my notes?"*

Watch for the echo chamber. AI tends to confirm existing ideas in an effort to please. Actively steer it toward challenge mode: *"What's wrong with this argument? What am I not seeing?"*

Create new notes for any ideas worth keeping. Link them into the network. You're not writing yet. You're stress-testing.

### 4. Bullet draft

Ask the AI: *"Based on everything you've read, propose a linear outline for this piece. What's the narrative arc?"*

It translates the network of linked notes into a structured sequence of bullet points. Almost always wrong on the first pass. That's fine. The bullets are scaffolding, not scripture. Print it, mark it up, move things around. This is where the network starts to evolve into a story.

### 5. Shape the story

This is the heaviest editing phase, and it's almost entirely human.

Go through the bullets. What's the actual argument? What's the opening that earns the next paragraph? What needs to go, even if it's clever? Craft the story beats: the sequence, emphasis, and arc that make the piece yours.

Use the AI to test alternatives: *"What if this section comes first?" "What if we drop this point entirely?" "Give me three different ways to open this."*

The narrative direction is yours. The story you want to tell isn't something you can delegate.

### 6. Write the thing

Two paths depending on the piece and your preference.

**Path A:** Write the prose yourself. Use AI for phrasing suggestions, structural feedback, and fact-checking as you go.

**Path B:** Feed the AI examples of your previous writing. Ask it to draft calibrated to your voice. Then edit collaboratively, line by line, until it reads as yours.

Here's the thing most people don't expect though: the two paths converge. If the upstream thinking is solid (phases 1 through 5 did their job), the quality of the final piece depends far less on who typed the first sentence than you'd think. The argument is already built. The structure is already tested. The voice is already established in the examples you fed it. What remains is craft at the sentence level, and that's where collaborative editing earns its keep.

Either path ends the same way. You read every line and ask: would I say this? Does this sound like me? Could I defend this idea in conversation? If the answer is no, you rewrite it. If the answer is yes, it doesn't matter whether you or the AI typed it first.

When you're done, feed the final version back to the AI alongside its draft. Ask it to note the differences so it calibrates better next time. Each round of this tightens the loop. The AI learns your preferences. You learn where to push back. The gap between Path A and Path B narrows until the distinction stops mattering.

## I'm not the only one doing this

Nate B Jones talks about what he calls "Cognitive Choreography": the idea that most people use AI to *compress* information. Rewrite the email faster. Do the requirements in 10 minutes. Repurpose a deck in half an hour. But the real value, he argues, is in using AI to *expand* thinking. To give your brain more time on the things that really matter.

His output is prolific, and if you read the comments it's a mixture of "wow, so much insight" and accusations of slop. But the truth is that AI is a force multiplier here. It's letting him do the research, structure his thoughts, and deliver output that wouldn't have been possible a year ago.

Others are building "second brain" systems along similar lines. The pattern is emerging independently across knowledge workers who've figured out the same thing: AI's value isn't in the output. It's in the thinking process.

## Why this matters

The obvious question: why not just ask AI to write the blog post?

Because the writing isn't the point. The thinking is. And the thinking happens before a single sentence gets drafted. By the time I'm "writing," the hard work is done. I'm translating a well-tested argument into prose.

The AI never sees a blank page. It sees a web of interconnected thoughts that I built over days. That's why the output sounds like me and not like a chatbot. The raw material was always human.

There's a principle baked into every phase of this workflow: AI outputs are inputs, not finished thinking. The separation between AI's contribution and your own isn't bolted on as an afterthought. It's built into the structure of the process.

Luhmann understood something that's easy to forget in the age of generative AI. The value isn't in the output. It's in the process of making connections. His index cards weren't a filing system. They were a thinking system. The writing was a byproduct.

AI doesn't replace that process. It accelerates it. And if you've already built the habit of thinking in atomic, linked notes, you'll find that AI has something meaningful to work with. Instead of generating from a void.

Back to Iceland. The Blue Lagoon works because the heat was always there, underground. The engineering just gave it somewhere to go.

That's what this workflow feels like. The thinking was always mine. The AI just gave it infrastructure.

*This post was developed using the workflow it describes.*
