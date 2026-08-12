AI Employee Onboarding Agent

A local-first Python CLI agent that helps employees answer onboarding questions using approved internal documents only. The project combines retrieval, grounded response generation, security checks, role authorization, and a human-in-the-loop workflow for account-access actions.

Project Overview

The AI Employee Onboarding Agent is designed to demonstrate a safe and controlled AI workflow for employee onboarding.

Instead of answering from unrestricted external knowledge, the agent retrieves relevant information from a small set of approved company documents and generates responses grounded in those sources.

For requests that require an account-access action, the system does not execute the action immediately. It first checks authorization and requires explicit human approval before calling the mock access tool.

Key Features

Local-first Python CLI

Four approved synthetic knowledge documents

TF-IDF-based document retrieval

Cosine-similarity ranking

Top-K relevant passage selection

Relevance threshold for safe abstention

Grounded answers with source citations

Prompt-injection protection

Role-based authorization

Human approval before account-access actions

Mock account-access tool

Tool failure handling

Visible workflow trace

Deterministic local response mode

Optional Ollama response-generation mode

Test suite included in the repository

Architecture

Knowledge Question Flow

User Question
      |
      v
Input Validation
      |
      v
Security / Prompt-Injection Check
      |
      v
Intent Detection
      |
      v
Document Retrieval
      |
      v
TF-IDF + Cosine Similarity
      |
      v
Relevance Threshold
      |
      +----------------------+
      |                      |
      v                      v
Relevant Sources        Insufficient Evidence
      |                      |
      v                      v
Grounded Answer          Safe Abstention
      |
      v
Source Citations

Account-Access Workflow

Access Request
      |
      v
Authorization Check
      |
      v
Human Approval Required
      |
      +------------------+
      |                  |
    Approved           Rejected
      |                  |
      v                  v
 Mock Access Tool     No Action
      |
      v
Action Result

Approved Knowledge Sources

The agent currently uses these four synthetic documents:

data/onboarding_guide.txt

data/security_policy.txt

data/support_escalation.txt

data/product_faq.txt

These documents are intentionally kept inside the repository so that the system can be run locally without depending on an external knowledge base.

Technology Stack

Python

scikit-learn

TF-IDF Vectorization

Cosine Similarity

Pytest

Optional Ollama integration

Project Structure

AI_Onboarding_Agent.-main/
│
├── data/
│   ├── onboarding_guide.txt
│   ├── product_faq.txt
│   ├── security_policy.txt
│   └── support_escalation.txt
│
├── src/
│   ├── agent.py
│   ├── config.py
│   ├── embeddings.py
│   ├── llm.py
│   ├── loader.py
│   ├── models.py
│   ├── prompts.py
│   ├── retriever.py
│   ├── security.py
│   ├── tools.py
│   └── __init__.py
│
├── tests/
│   └── test_agent.py
│
├── main.py
├── requirements.txt
├── EXPLANATION.md
├── PRESENTATION_CONTENT.md
├── SAMPLE_RUNS.md
└── README.md

Installation

1. Clone the repository

git clone <YOUR_GITHUB_REPOSITORY_URL>
cd AI_Onboarding_Agent.-main

2. Create a virtual environment

python -m venv .venv

3. Activate the environment

Windows:

.venv\Scripts\activate

Linux / macOS:

source .venv/bin/activate

4. Install dependencies

pip install -r requirements.txt

Running the Agent

The default mode is deterministic and does not require an external LLM service.

python main.py

You will see:

AI EMPLOYEE ONBOARDING AGENT
Approved sources only | Local-first | Human approval for actions
Generation mode: deterministic

The application then accepts questions interactively.

Example:

Question (or 'exit'): What should I do if my laptop is lost?
User role [employee]: employee

The agent displays:

Workflow trace

Final response

Retrieved/source information

Approval prompt when an action is required

Type exit to stop the application.

Optional Ollama Mode

The application also supports an optional Ollama-based generation mode:

python main.py --llm ollama

This mode requires a working local Ollama installation and an available compatible model.

If Ollama is not configured, use the default deterministic mode:

python main.py

Example Questions

Try questions related to the approved documents, such as:

How do I report a lost laptop?

What should I do if I cannot access my account?

How can I contact support?

What is the process for onboarding?

The agent should provide grounded responses when sufficient information is available and abstain when the approved documents do not contain enough evidence.

Safety and Security

The project is designed around controlled AI behavior.

Approved Sources Only

The agent is restricted to the repository's approved synthetic documents for onboarding knowledge.

Grounded Responses

Retrieved passages are used as evidence for the final answer, and source citations are included where applicable.

Safe Abstention

If the retrieved information is not sufficiently relevant, the agent can refuse to provide an unsupported answer rather than inventing information.

Prompt-Injection Protection

Retrieved document content is treated as reference material, not as instructions that can override the agent's system rules.

Role Authorization

Actions that require elevated permissions are checked against the user's role.

Human-in-the-Loop Approval

Account-access actions require explicit approval from the user before execution.

Mock Tools

The repository uses a mock access tool rather than performing real account changes.

Testing

The repository contains automated tests under:

tests/test_agent.py

Run them with:

pytest

Current repository note: the existing test file is from an earlier interface/version of the project and currently requires alignment with the latest OnboardingAgent implementation. The core CLI flow itself has been verified to initialize, retrieve approved content, generate a grounded response, display the workflow trace, and handle the interactive flow.

Current Status

Working

Agent initialization

Local document loading

TF-IDF retrieval

Cosine-similarity ranking

Grounded response flow

Source citation flow

Workflow trace

Security checks

Human approval workflow

Mock action workflow

Deterministic local execution

To Be Improved Before Final Deployment

Align the automated tests with the current agent interface

Add a web interface for browser-based usage

Deploy the application to a public hosting platform

Add screenshots and a final live-demo URL to this README

Future Deployment

The current version is a command-line application. For a browser-accessible submission, the agent can be wrapped in a lightweight web interface and deployed to a suitable hosting platform.
