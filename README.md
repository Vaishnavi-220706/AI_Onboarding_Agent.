# 🤖 AI Employee Onboarding Agent

<p align="center">
  <strong>A Safe, Grounded & Human-Controlled AI Assistant for Employee Onboarding</strong>
</p>

<p align="center">
  <em>Answer employee questions from approved company knowledge — without hallucinating policies or performing sensitive actions automatically.</em>
</p>

---

## 🌟 Overview

The **AI Employee Onboarding Agent** is a local-first intelligent assistant designed to help employees with common onboarding and workplace-support questions.

Instead of relying on unrestricted external knowledge, the agent searches a controlled collection of **approved internal documents**, retrieves the most relevant information, and generates a response grounded in that evidence.

For sensitive requests such as **account access**, the system does not directly perform the action. It follows a controlled workflow involving:

**Authorization → Human Approval → Mock Action**

This makes the project a practical demonstration of **grounded AI, information retrieval, AI safety, role-based access control, and human-in-the-loop decision making**.

---

## 💡 Why This Project?

A normal chatbot may confidently answer a question even when it does not actually know the company's policy.

This project takes a different approach:

> **If the approved knowledge does not contain enough evidence, the agent should not invent an answer.**

It also follows the principle:

> **AI can recommend an action, but sensitive actions should remain under human control.**

---

## ✨ Key Features

| Feature                             | Description                                                |
| ----------------------------------- | ---------------------------------------------------------- |
| 📚 **Approved Knowledge Base**      | Uses controlled internal onboarding documents              |
| 🔎 **Smart Retrieval**              | TF-IDF + cosine similarity finds relevant information      |
| 🎯 **Grounded Responses**           | Answers are based on retrieved evidence                    |
| 🛑 **Safe Abstention**              | Avoids unsupported answers when evidence is insufficient   |
| 🛡️ **Prompt-Injection Protection** | Retrieved content cannot override system rules             |
| 🔐 **Role-Based Authorization**     | Checks user permissions for sensitive actions              |
| 👤 **Human Approval**               | Requires explicit approval before privileged actions       |
| 🧰 **Mock Access Tool**             | Demonstrates access workflows without real account changes |
| 🧾 **Source Citations**             | Shows where the answer came from                           |
| 🖥️ **Workflow Trace**              | Makes the agent's decision process visible                 |
| ⚡ **Local-First**                   | Runs locally without requiring an external AI API          |
| 🦙 **Optional Ollama**              | Supports optional local LLM generation                     |

---

## 🏗️ System Architecture

### 📖 Knowledge Question Flow

```text
┌──────────────────┐
│   User Question  │
└────────┬─────────┘
         ↓
┌──────────────────┐
│ Input Validation │
└────────┬─────────┘
         ↓
┌──────────────────────────┐
│ Security / Injection     │
│ Detection                │
└────────┬─────────────────┘
         ↓
┌──────────────────┐
│ Intent Detection │
└────────┬─────────┘
         ↓
┌──────────────────────────┐
│ Document Retrieval       │
│ TF-IDF + Cosine Similarity│
└────────┬─────────────────┘
         ↓
┌──────────────────────────┐
│ Relevance Threshold      │
└────────┬─────────────────┘
         ↓
   ┌─────┴─────┐
   ↓           ↓
Relevant     Insufficient
Evidence      Evidence
   ↓           ↓
Grounded    Safe
Answer      Abstention
   ↓
Source Citation
```

### 🔐 Sensitive Action Flow

```text
┌─────────────────────┐
│   Access Request    │
└──────────┬──────────┘
           ↓
┌─────────────────────┐
│ Authorization Check │
└──────────┬──────────┘
           ↓
      ┌────┴────┐
      ↓         ↓
   Allowed    Denied
      ↓         ↓
      ↓      No Action
      ↓
┌─────────────────────┐
│  Human Approval     │
│     Required        │
└──────────┬──────────┘
           ↓
      ┌────┴────┐
      ↓         ↓
  Approved    Rejected
      ↓         ↓
 Mock Tool   No Action
      ↓
 Action Result
```

---

## 🧠 How It Works

The agent follows a controlled pipeline:

### 1️⃣ User Input

The employee enters a question through the CLI.

### 2️⃣ Security Check

The input is inspected for unsafe or prompt-injection-style instructions.

### 3️⃣ Intent Detection

The system determines whether the request is a normal knowledge question or an action-related request.

### 4️⃣ Document Retrieval

The question is converted into a TF-IDF representation and compared with the approved documents using cosine similarity.

### 5️⃣ Relevance Evaluation

Only sufficiently relevant information is used.

If the evidence is weak, the agent can safely abstain.

### 6️⃣ Grounded Response

Relevant information is used to produce the final answer.

### 7️⃣ Human-Controlled Actions

If an account-access action is requested:

**Role → Authorization → Human Approval → Mock Tool**

No sensitive action happens automatically.

---

## 📚 Knowledge Base

The project currently contains four approved synthetic documents:

```text
data/
├── onboarding_guide.txt
├── security_policy.txt
├── support_escalation.txt
└── product_faq.txt
```

These documents contain the controlled knowledge used by the agent.

Keeping them inside the repository makes the project:

* ✅ Reproducible
* ✅ Easy to test
* ✅ Local-first
* ✅ Independent of external company systems
* ✅ Suitable for demonstration

---

## 🛠️ Technology Stack

<p align="center">

| Technology               | Purpose                       |
| ------------------------ | ----------------------------- |
| 🐍 **Python**            | Core application              |
| 🔎 **scikit-learn**      | Text processing and retrieval |
| 📊 **TF-IDF**            | Document representation       |
| 📐 **Cosine Similarity** | Relevance ranking             |
| 🧪 **Pytest**            | Automated testing             |
| 🦙 **Ollama**            | Optional local LLM generation |

</p>

---

## 📂 Project Structure

```text
AI_Onboarding_Agent/
│
├── 📁 data/
│   ├── onboarding_guide.txt
│   ├── product_faq.txt
│   ├── security_policy.txt
│   └── support_escalation.txt
│
├── 📁 src/
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
├── 📁 tests/
│   └── test_agent.py
│
├── 🐍 main.py
├── 📦 requirements.txt
├── 📄 EXPLANATION.md
├── 📄 PRESENTATION_CONTENT.md
├── 📄 SAMPLE_RUNS.md
└── 📖 README.md
```

---

# 🚀 Getting Started

## 1. Clone the Repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd AI_Onboarding_Agent
```

## 2. Create a Virtual Environment

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### Linux / macOS

```bash
python -m venv .venv
source .venv/bin/activate
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the Project

## ⚡ Deterministic Local Mode

The recommended mode does not require an external LLM service.

```bash
python main.py
```

The application starts an interactive onboarding assistant.

Example:

```text
======================================================================
AI EMPLOYEE ONBOARDING AGENT
======================================================================
Approved sources only | Local-first | Human approval for actions
Generation mode: deterministic
======================================================================

Question (or 'exit'): What should I do if my laptop is lost?
User role [employee]: employee
```

The agent then performs:

```text
Question
   ↓
Security Check
   ↓
Document Retrieval
   ↓
Relevance Check
   ↓
Grounded Answer
   ↓
Source Citation
```

Type:

```text
exit
```

to stop the application.

---

# 💬 Example Interactions

### 🔹 Example 1 — Knowledge Question

**User:**

```text
What should I do if my laptop is lost?
```

**Agent:**

```text
Retrieves the relevant security document
        ↓
Checks relevance
        ↓
Generates grounded response
        ↓
Provides source information
```

---

### 🔹 Example 2 — Support Question

**User:**

```text
How can I contact support?
```

The agent searches the approved support documentation and returns the relevant information.

---

### 🔹 Example 3 — Sensitive Access Request

**User:**

```text
I need access to an account.
```

The system does **not** immediately perform the action.

Instead:

```text
Access Request
      ↓
Role Check
      ↓
Authorization
      ↓
Human Approval
      ↓
Mock Access Tool
      ↓
Result
```

---

### 🔹 Example 4 — Unsupported Question

**User:**

```text
What will the weather be tomorrow?
```

If the approved knowledge base contains no relevant information, the agent should avoid inventing an answer.

```text
No Reliable Evidence
        ↓
Safe Abstention
```

---

# 🔐 Security & Safety

Security is a core part of the project rather than an additional feature.

### 🛡️ Approved Sources Only

The agent uses the controlled knowledge base instead of unrestricted external information.

### 🚫 Prompt-Injection Protection

Retrieved documents are treated as **data**, not as instructions capable of overriding system behavior.

### 🎯 Relevance Threshold

Low-relevance retrieval results can trigger a safe abstention.

### 🔑 Role-Based Authorization

Sensitive actions are checked against the user's role.

### 👤 Human-in-the-Loop

Privileged operations require explicit human approval.

### 🧰 Mock Actions

The access tool is intentionally mocked so the project can demonstrate the workflow without modifying real employee accounts.

---

# 🧪 Testing

Run:

```bash
pytest
```

Tests are located in:

```text
tests/test_agent.py
```

> **Current status:** The existing test file was created against an earlier interface of the agent and needs to be aligned with the latest implementation. The core CLI workflow has been verified independently and successfully initializes, retrieves approved content, generates a grounded response, displays the workflow trace, and handles interactive input.

---

# 📊 Project Status

| Component                   |       Status       |
| --------------------------- | :----------------: |
| Project Initialization      |          ✅         |
| Document Loading            |          ✅         |
| TF-IDF Retrieval            |          ✅         |
| Cosine Similarity           |          ✅         |
| Grounded Responses          |          ✅         |
| Source Citations            |          ✅         |
| Security Checks             |          ✅         |
| Prompt-Injection Protection |          ✅         |
| Role Authorization          |          ✅         |
| Human Approval              |          ✅         |
| Mock Access Tool            |          ✅         |
| Deterministic Mode          |          ✅         |
| Ollama Mode                 |     🟡 Optional    |
| Automated Tests             | 🟡 Needs Alignment |
| Web Interface               |         🔜         |
| Live Deployment             |         🔜         |

---

# 🖥️ Demo

## Current Version

The current version runs as a **Python CLI application**.

A browser-based interface can be added for public deployment.

### 📸 Screenshots

> Add screenshots of the working application here after final testing.

Example:

```markdown
![Agent Demo](assets/demo.png)
```

---

# 🛣️ Roadmap

```text
[x] Local onboarding agent
[x] Approved document retrieval
[x] TF-IDF similarity search
[x] Grounded responses
[x] Source citations
[x] Security checks
[x] Role-based authorization
[x] Human approval workflow
[x] Mock access tool
[ ] Align automated tests
[ ] Build browser-based UI
[ ] Deploy live application
[ ] Add screenshots
[ ] Add live demo link
```

---

# 🎓 What This Project Demonstrates

### 🔎 Information Retrieval

TF-IDF and cosine similarity are used to identify relevant onboarding information.

### 🧠 Grounded AI

Responses are generated using retrieved evidence instead of unrestricted knowledge.

### 🛡️ AI Safety

Prompt-injection protection and safe abstention reduce unsafe or unsupported behavior.

### 🔐 Access Control

Role-based authorization prevents unauthorized actions.

### 👤 Human-in-the-Loop

Sensitive actions require explicit human approval.

### 💻 Local-First Architecture

The project can operate locally without depending on external APIs.

---

# 🌐 Deployment

The final version can be deployed as a browser-accessible application.

---

# 👩‍💻 Author

### **Vaishnavi**

<p align="center">
  <strong>🔐 Grounded Answers • Controlled Actions • Human Oversight</strong>
</p>

<p align="center">
  ⭐ If you find this project useful, consider giving the repository a star!
</p>
