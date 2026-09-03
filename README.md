# AI Code Review Tool

A lightweight Python tool that reviews source code using a combination of rule-based heuristics and an AI-powered analysis via the Anthropic API (Claude).

## What it does

Given a Python file, the tool runs two layers of analysis and prints out a combined list of issues:

1. **Heuristic checks** (`analyze.py`) — fast, free, instant checks with no API calls:
   - Long lines (over 100 characters)
   - Trailing whitespace
   - TODO/FIXME markers left in code
   - Bare `except:` clauses (a common Python anti-pattern that silently catches all errors, including ones you probably don't want to catch)

2. **AI-powered review** (`ai.py`) — sends the code to Claude (Anthropic's LLM) with a structured prompt, asking it to identify bugs, style issues, security concerns, and performance problems, returned as structured JSON.

Each issue is reported with a `type`, `severity` (low/medium/high), and a human-readable `message`.

## Example output

$ python main.py test.py

[HIGH] bug: File is opened without a context manager ('with' statement). If an exception occurs before f.close(), the file will not be closed, causing a resource leak.
[MEDIUM] bug: Parameters 'encoding', 'skip_rows', 'header', and 'columns' are accepted but never used, making the function misleading and incomplete.
[LOW] style: The else branch 'p = p' in the clean block is a no-op and should be removed.
[MEDIUM] performance: f.readlines() reads the entire file into memory at once. Iterating directly over the file object is more memory-efficient.


## Setup

1. Clone the repo and install dependencies:
```bash
pip install anthropic
```

2. Set your Anthropic API key as an environment variable:
```bash
export ANTHROPIC_API_KEY="your-key-here"
```
(Get a key from [console.anthropic.com](https://console.anthropic.com) — API usage is billed separately and pay-as-you-go, but small test files cost fractions of a cent.)

## Usage

```bash
python main.py <path-to-file>
```

Example:
```bash
python main.py my_script.py
```

## Project structure

├── main.py # Entry point — loads the file, runs both analysis layers, prints results
├── analyze.py # Heuristic (non-AI) checks
├── ai.py # Calls the Anthropic API and parses the response into structured issues
└── test.py # Sample file used for testing the tool


## Design notes

- The heuristic and AI layers are intentionally separate — heuristics are instant and free, so they always run first, with the AI layer adding deeper analysis on top.
- The AI prompt explicitly requests JSON-only output, with defensive parsing (stripping markdown code fences, handling malformed JSON) since LLM output isn't always perfectly formatted.

## Possible future improvements

- Replace the line-based heuristics in `analyze.py` with Python's `ast` module for more accurate structural analysis (e.g. correctly identifying function boundaries even with nested functions, rather than approximating based on line distance between `def` statements).
- Support scanning an entire directory/repository rather than a single file.
- Add a `--severity` flag to filter output (e.g. only show medium/high issues).