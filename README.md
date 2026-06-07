# The Unofficial Guide — Project 1

> **How to use this template:**
> Complete each section *after* you've built and tested the corresponding part of your system.
> Do not write placeholder text — if a section isn't done yet, leave it blank and come back.
> Every section below is required for submission. One-liners will not receive full credit.

---

## Domain

<!-- What topic or category of knowledge does your system cover?
     Why is this knowledge valuable, and why is it hard to find through official channels?
     Example: "Student reviews of CS professors at [university] — useful because official
     course descriptions don't reflect teaching style, exam difficulty, or workload." -->
I chose Wikipedia articles on the Windows OS. This is because the information contained shares similar format, is open to use, and can be easily verified 

This domain is particularly useful since technical information about the Windows OS is very esoteric and it can be hard to parse large articles in order to find specific information, especially technical information


---

## Document Sources

<!-- List every source you collected documents from.
     Be specific: include URLs, subreddit names, forum thread titles, or file names.
     Aim for variety — sources that together cover different subtopics or perspectives. -->

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

<!-- Describe your chunking approach with enough specificity that someone else could reproduce it.
     Include:
     - Chunk size (characters or tokens) and why that size fits your documents
     - Overlap size and why (or why not) you used overlap
     - Any preprocessing you did before chunking (e.g., stripping HTML, removing headers)
     - What your final chunk count was across all documents -->

**Chunk size:**
I Went with a 512 chunk size, this is because it gave me a good balance of detail and precision with my responses, giving pretty good output from my model 

**Overlap:**
I went with a 64 character overlap, which should be around a sentence 

**Reasoning:**
I want to have a chunk size that is not too long (in order not to flood the context window) but not to small (missing context)

**Preprocessing:**
I downloaded the articles using a website that converted them to .md files, I then went through and manually cleaned up some of the frivilous things that tha download included, such as the "further reading" section 

---

## Embedding Model

<!-- Name the embedding model you used and explain your choice.
     Then answer: if you were deploying this system for real users and cost wasn't a constraint,
     what tradeoffs would you weigh in choosing a different model?
     Consider: context length limits, multilingual support, accuracy on domain-specific text,
     latency, and local vs. API-hosted. -->

**Model used:**
ChromaDB Default Embedding Model


**Production tradeoff reflection:**
Realistically, the data retrieved is going to mostly be articles, I would be okay with a lower top K since the information retrieved should be accurate and detailed to any user queries
A too large top K would give irrelevant information to the LLM, reducing the output quality of the system
I would also try and focus on specific domains (like wikipedia and official support articles) to further improve output quality
Different embedding models trade efficiency for accuracy, and vice versa, I would test each embedding model to see which one I liked the best 

---

## Grounded Generation

<!-- Explain how your system enforces grounding — how does it prevent the LLM from answering
     beyond the retrieved documents?
     Describe both your system prompt (what instruction you gave the model) and any structural
     choices (e.g., how you formatted the context, whether you filtered low-relevance chunks).
     Do not just say "I told it to use the documents" — show the actual instruction or explain
     the mechanism. -->

**System prompt grounding instruction:**
"You are a Chatbot that helps people with their questions on Microsoft Windows, \n" \
"You are given a few short passages from Wikipedia articles with potentially relevant information, use this information in you response, but do not mention that you have been given this text"

**How source attribution is surfaced in the response:**
Occasionally, the LLM would state that it referenced information from the text, It would also directly quote the given text in many cases 

---

## Evaluation Report

<!-- Run your 5 test questions from planning.md through your system and record the results.
     Be honest — a partially accurate or inaccurate result that you explain well is more
     valuable than a suspiciously perfect result. -->

| # | Question | Expected answer | System response (summarized) | Retrieval quality | Response accuracy |
|---|----------|-----------------|------------------------------|-------------------|-------------------|
| 1 | What version of Windows was contraversial due to its implementation of AI? | "Windows 11" + other information | LLM Responded with correct answer, however it mentioned that the information retrieved by the DB was incorrect | Off-Target | Partially accurate |
| 2 | Why was Windows 9x so important in the context of its release? | information relating to start menu, UI, internet, and more| Correctly summarized information pertaining to all of these factors, plus more info that was mentioned in the article | Relevant | Accurate |
| 3 | What is the difference between Windows 9x and Windows NT? | the kernels differ due to its architectures (ms dos vs custom monolithic) | A table was presented with all of the relevant information | Relevant | Accurate |
| 4 | Which version of Windows introduced the start menu? | windows 95 | The start menu was introduced with Windows 95 | Relevant | Accurate |
| 5 | Why was Windows 7 more positively recieved than vista? | stability, performance, focus on user experience | A table was presented showing the information provided | Relevant | Accurate |

**Retrieval quality:** Relevant / Partially relevant / Off-target  
**Response accuracy:** Accurate / Partially accurate / Inaccurate

---

## Failure Case Analysis

<!-- Identify at least one question where retrieval or generation did not work as expected.
     Write a specific explanation of *why* it failed, tied to a part of the pipeline.

     "The answer was wrong" is not an explanation.

     "The relevant information was split across a chunk boundary, so retrieval returned
     only half the context — the model didn't have enough to answer correctly" is an explanation.

     "The embedding model treated the professor's nickname as out-of-vocabulary and returned
     results from an unrelated review" is an explanation. -->

**Question that failed:**
What version of Windows was contraversial due to its implementation of AI?

**What the system returned:**
Information from other, irrelevant versions of Windows, like Windows 1.0

**Root cause (tied to a specific pipeline stage):**
Document ingestion did not have enough information to accurately generate the desired output

**What you would change to fix it:**
Find more relevant sources that are up to date, and contain more information about the nitty-gritty of the OS

---

## Spec Reflection

<!-- Reflect on how planning.md shaped your implementation.
     Answer both questions with at least 2–3 sentences each. -->

**One way the spec helped you during implementation:**
The spec helped me refine what I should do for each step, as well as my approach going into this project 


**One way your implementation diverged from the spec, and why:**
I had to use different models that what I intended, this was due to speed of development, technical issues (like rate limiting) and ease of use 


---

## AI Usage

<!-- Describe at least 2 specific instances where you used an AI tool during this project.
     For each: what did you give the AI as input, what did it produce, and what did you
     change, override, or direct differently?

     "I used Claude to help me code" is not sufficient.
     "I gave Claude my Chunking Strategy section from planning.md and asked it to implement
     chunk_text(). It returned a function using a fixed character split. I overrode the
     chunk size from 500 to 200 because my documents are short reviews, not long guides." -->

**Instance 1**

- *What I gave the AI:*
how would you use openrouter to make an api call to the google gemini api? and, since I am making a chatbot, what would be the preferred format for uploading the previous conversation history? 

- *What it produced:*
Some sample code that helped me understand how I should give the conversation history to the LLM, as well as a sample API request to the LLM

- *What I changed or overrode:*
I changed the actual API request code (to better match my architecture), and I used the information provided by the LLM as a jumping-off point to further develop my code

**Instance 2**

- *What I gave the AI:*
give me a simple chat interface in a single python file, i want these things:
a chatbot window that shows up in the cli
when a chat is given, that chat (+ the conversation history) calls a function (which is contained in a different file) called "chat" (you do not have to write this function)
the output of this chat function is then printed to the terminal

- *What it produced:*
A simple CLI that did mostly what I suggested, I only had to make a few changes, (like listening to the ctrl+c SIGINT, and what the "history" variable should store)

- *What I changed or overrode:*
Like I said earlier, I added functionallity, and changed some of the code to better facillitate the connection between the LLM and my code
