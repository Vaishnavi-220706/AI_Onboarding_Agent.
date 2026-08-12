# AI Onboarding Agent

A local-first Python CLI onboarding assistant built for Assessment B - AI Agent and Workflow Builder - AI Engineer.

## Features

- Four approved synthetic documents
- TF-IDF based retrieval
- Cosine similarity ranking
- Grounded answers
- Source citations
- Safe abstention
- Prompt injection protection
- Role authorization
- Human approval workflow
- Mock account-access tool
- Tool failure handling
- Visible workflow trace
- Deterministic local fallback
- Optional Ollama integration
- Automated tests

## Architecture

Input
↓
Validation
↓
Security Check
↓
Intent Detection
↓
Retrieval
↓
Relevance Threshold
↓
Grounded Answer / Abstention

For account access:

Request
↓
Authorization
↓
Human Approval
↓
Mock Tool
↓
Result

## Installation

Create virtual environment:

```bash
python -m venv .venv