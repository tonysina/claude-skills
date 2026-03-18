---
name: markdown-fetch
description: >
  Fetches web content as markdown instead of HTML when available, reducing token
  usage by up to 80%. Use when fetching web pages for AI processing, content
  ingestion, summarization, RAG pipelines, or any workflow that reads web content
  into a context window. Triggers on "fetch this page", "get the content from",
  "read this URL", "scrape", "ingest this site", web_fetch calls for AI
  consumption, or any task that pulls web content for LLM processing.
  Do NOT use for fetching APIs that return JSON, downloading binary files,
  or accessing pages where exact HTML structure matters (e.g., scraping
  specific DOM elements).
metadata:
  version: 1.0.0
---

# Markdown Fetch

When fetching web content for AI processing, request markdown instead of HTML.
Cloudflare's "Markdown for Agents" feature (and similar services) convert HTML
to clean markdown on the fly when the request includes an `Accept: text/markdown`
header. This dramatically cuts token usage since HTML markup, nav bars, script
tags, and wrapper divs are stripped out.

## How It Works

Any Cloudflare-enabled site with "Markdown for Agents" turned on will honor
content negotiation. The pattern is simple:

1. Send `Accept: text/markdown, text/html` in the request headers
2. If the server supports it, you get back `content-type: text/markdown`
3. If not, you get standard HTML as a fallback

The response may also include:
- `x-markdown-tokens` header: estimated token count of the markdown content.
  Use this to decide on chunking strategy or check context window fit.
- `Content-Signal` header: declares the publisher's AI usage permissions
  (training, search, agentic input).

## When to Apply This Pattern

Apply this when ALL of these are true:
- You are fetching a web page (not an API endpoint or binary file)
- The content will be processed by an LLM (summarization, analysis, RAG, etc.)
- You don't need the raw HTML structure itself

Skip this when:
- The task requires specific DOM elements or CSS selectors
- You're calling a REST API that returns JSON/XML
- You need to render the page visually

## Implementation

### curl
```bash
curl https://example.com/page \
  -H "Accept: text/markdown, text/html"
```

### Python (requests)
```python
import requests

response = requests.get(
    "https://example.com/page",
    headers={"Accept": "text/markdown, text/html"}
)

is_markdown = "text/markdown" in response.headers.get("content-type", "")
token_estimate = response.headers.get("x-markdown-tokens")
content = response.text
```

### TypeScript / Workers
```typescript
const response = await fetch("https://example.com/page", {
  headers: { Accept: "text/markdown, text/html" },
});

const isMarkdown = response.headers.get("content-type")?.includes("text/markdown");
const tokenCount = response.headers.get("x-markdown-tokens");
const content = await response.text();
```

## Checking Whether a Site Supports It

Not every site supports this. After fetching, check the response `content-type`
header. If it contains `text/markdown`, the conversion succeeded. If it returns
`text/html`, the site either doesn't use Cloudflare or hasn't enabled the feature.
Your code should handle both cases gracefully.

## Presenting Markdown to the User

When a fetch returns `text/markdown`, save the content as a `.md` file and
present it to the user in addition to using it for the task at hand. The
markdown is already in context from the fetch, so this adds negligible cost.

1. Complete the primary task (summarize, analyze, etc.) using the markdown content
2. Write the markdown to `/mnt/user-data/outputs/{descriptive-name}.md`
3. Call `present_files` to share it

The user gets a clean, rendered, downloadable copy of the page content alongside
whatever they originally asked for. This is a side effect, not a replacement for
the primary task. If the response came back as `text/html` (site doesn't support
markdown negotiation), skip this step and proceed normally.

## Alternative Conversion Methods

If markdown negotiation isn't available from the source, Cloudflare provides two
other conversion options:

- **Workers AI `AI.toMarkdown()`**: Converts HTML, PDFs, Office docs, and other
  formats to markdown server-side. Useful for document ingestion pipelines.
- **Browser Rendering `/markdown` REST API**: Renders dynamic pages (SPAs,
  JS-heavy sites) in a real browser first, then converts to markdown.

## Example: Deciding Based on Token Count

```python
token_estimate = response.headers.get("x-markdown-tokens")
if token_estimate and int(token_estimate) > context_window_limit:
    # Content too large - chunk it
    chunks = split_markdown_by_sections(content)
else:
    # Fits in context - use directly
    process(content)
```
