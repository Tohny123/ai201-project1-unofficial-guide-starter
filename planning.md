# Project 1 Planning: The Unofficial Guide

> Write this document before you write any pipeline code.
> Your spec and architecture diagram are what you'll use to direct AI tools (Claude, Copilot, etc.) to generate your implementation — the more specific they are, the more useful the generated code will be.
> Update the Retrieval Approach and Chunking Strategy sections if you change your approach during implementation.
> Update this file before starting any stretch features.

---

## Domain

<!-- What domain did you choose? Why is this knowledge valuable and hard to find through official channels? -->

I chose Wikipedia articles on the Windows OS. This is because the information contained shares similar format, is open to use, and can be easily verified 

This domain is particularly useful since technical information about the Windows OS is very esoteric and it can be hard to parse large articles in order to find specific information, especially technical information

## Documents

<!-- List your specific sources: URLs, subreddit names, forum threads, or file descriptions.
     Aim for at least 10 sources that together cover different subtopics or perspectives within your domain. -->



| # | Source | Description | URL or location |
|---|--------|-------------|-----------------|
| 1 | Windows NT| Wiki Article on the NT Kernel | https://en.wikipedia.org/wiki/Windows_NT | 
| 2 | Windows 9x | Wiki Article on the 9x Kernel (dos based) | https://en.wikipedia.org/wiki/Windows_9x |
| 3 | MS-DOS | Wiki article on MS DOS | https://en.wikipedia.org/wiki/MS-DOS |
| 4 | Windows 1.0 | Wiki article on windows 1.0 | https://en.wikipedia.org/wiki/Windows_1.0 | 
| 5 | Windows 3.1 | Wiki article on windows 3.1 | https://en.wikipedia.org/wiki/Windows_3.1 | 
| 6 | Windows 95 | Wiki article on windows 95 | https://en.wikipedia.org/wiki/Windows_95 | 
| 7 | Windows XP | Wiki article on windows xp | https://en.wikipedia.org/wiki/Windows_XP | 
| 8 | Windows 7 | Wiki article on windows 7 | https://en.wikipedia.org/wiki/Windows_7 |  
| 9 | Windows 10 | Wiki article on windows 10 | https://en.wikipedia.org/wiki/Windows_10 |  
| 10 | Windows 11 | Wiki article on windows 11 | https://en.wikipedia.org/wiki/Windows_11 |

---

## Chunking Strategy

<!-- How will you split documents into chunks?
     State your chunk size (in tokens or characters), overlap size, and explain why those
     numbers fit the structure of your documents.
     A review-heavy corpus warrants different chunking than a long FAQ. -->

**Chunk size:**
I will go with chunks that are either between 256 or 1024 chars long, this is because Wikipedia articles tend to be very verbose, with large paragraphs describing the topics. 

**Overlap:**
I will try and go for a 32-64 token overlap, this is to capture any missing context between toekns 

**Reasoning:**
I want to have a chunk size that is not too long (in order not to flood the context window) but not to small (missing context)

---

## Retrieval Approach

<!-- Which embedding model are you using (e.g., all-MiniLM-L6-v2 via sentence-transformers)?
     How many chunks will you retrieve per query (top-k)?
     If you were deploying this for real users and cost wasn't a constraint, what tradeoffs
     would you weigh in choosing a different embedding model — context length, multilingual
     support, accuracy on domain-specific text, latency? -->

**Embedding model:**
ChromaDB Default Embedding Model

**Top-k:**
TopK: 20 to start off with, changing it depending on output quality

**Production tradeoff reflection:**
Realistically, the data retrieved is going to mostly be articles, I would be okay with a lower top K since the information retrieved should be accurate and detailed to any user queries
A too large top K would give irrelevant information to the LLM, reducing the output quality of the system
I would also try and focus on specific domains (like wikipedia and official support articles) to further improve output quality
Different embedding models trade efficiency for accuracy, and vice versa, I would test each embedding model to see which one I liked the best 

## Evaluation Plan

<!-- List your 5 test questions with their expected correct answers.
     Questions should be specific enough that you can judge whether the system's response
     is right or wrong. "What are good dining halls?" is too vague.
     "What do students say about wait times at [dining hall name] during lunch?" is testable. -->

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 | What version of Windows was contraversial due to its implementation of AI? | "Windows 11" + other information |
| 2 | Why was Windows 9x so important in the context of its release? | information relating to start menu, UI, internet, and more|
| 3 | What is the difference between Windows 9x and Windows NT? | the kernels differ due to its architectures (ms dos vs custom monolithic) |
| 4 | Which version of Windows introduced the start menu? | windows 95 |
| 5 | Why was Windows 7 more positively recieved than vista? | stability, performance, focus on user experience |

---

## Anticipated Challenges

<!-- What could go wrong? Name at least two specific risks with reasoning.
     Consider: noisy or inconsistent documents, missing source attribution, off-topic
     retrieval, chunks that split key information across boundaries. -->

1. I expect the model to get the incorrect context occasionally, and give incorrect answers

2. I expect the model to give useless information or halicinate information that doesn't exist

---

## Architecture

<!-- Draw a diagram of your pipeline showing the five stages:
     Document Ingestion → Chunking → Embedding + Vector Store → Retrieval → Generation
     Label each stage with the tool or library you're using.
     You can use ASCII art, a Mermaid diagram, or embed a sketch as an image.
     You'll use this diagram as context when prompting AI tools to implement each stage. -->

### Document ingestion:
I will download the files and store them locally in the "data" directory, I will download all of the articles using https://wikitext.eluni.co/ as .md files

### Chunking:
This will be done via a basic python script that creates a bunch of objects that cary the information in each chunk
| attribute | type |
|---|----------|
|*text*| actual content from text|
|*article*|article name all lowercased and underscore spaces (ex: windows_11)|
|*chunk_id*|article name + chunk list value (ex: windows_11.001)|

### Embedding:
This will be done through the use of the Gemini embedding model 2

### Vector Store:
https://www.trychroma.com/products/chromadb
I will use ChromaDB to store these embeddings

### Generation:
I will then use Google Gemini to create my final RAG model 


---

## AI Tool Plan

<!-- For each part of the pipeline below, describe:
     - Which AI tool you plan to use (Claude, Copilot, ChatGPT, etc.)
     - What you'll give it as input (which sections of this planning.md, which requirements)
     - What you expect it to produce
     - How you'll verify the output matches your spec

     "I'll use AI to help me code" is not a plan.
     "I'll give Claude my Chunking Strategy section and ask it to implement chunk_text()
     with my specified chunk size and overlap" is a plan. -->

I plan to use the Chat features of all 3 of these agents, and ask questions and request code chunks from there. I prefer this workflow over using agentic coding, as I feel like it allows me to pause and analyze the functionallity of the code better than if I just "let the AI do it all for me"
I will ask it for specific code chunks, and ask it for support regarding compiler bugs, api issues, and other issues
I expect it to produce not just useful code, but also a converation I can learn from, so my skills don't atrophy 


**Milestone 3 — Ingestion and chunking:**

**Milestone 4 — Embedding and retrieval:**

**Milestone 5 — Generation and interface:**
