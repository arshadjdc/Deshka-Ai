
# DeshkaAI

## Pre-Execution Safety Gateway for AI & Agent Actions

DeshkaAI is an experimental, model-agnostic safety layer designed to place a decision boundary between an AI/agent's intended action and the execution layer.

Instead of allowing every requested action to reach a tool or API directly, DeshkaAI evaluates the action before execution and separates lower-risk actions from high-risk or uncertain actions that require a safety hold or human review.

---

## Core Idea

```text
USER / AGENT INPUT
        │
        ▼
INTENT / CONTEXT ANALYSIS
        │
        ▼
PRE-EXECUTION SAFETY GATE
        │
        ├───────────────┐
        │               │
     LOW RISK      HIGH / UNCERTAIN
        │               │
        ▼               ▼
    EXECUTE         SAFE_HOLD
                        │
                        ▼
                   HUMAN REVIEW
                        │
                        ▼
                   HITL GATE
        │               │
        └───────┬───────┘
                ▼
           AUDIT LOGGER
                │
                ▼
        EXECUTION BOUNDARY
The key principle is simple:
An AI system should evaluate an intended action before allowing that action to cross an execution boundary.
Why DeshkaAI?
AI agents increasingly interact with tools, APIs, databases, files, and other real-world systems.
A model can generate a technically valid action while still being uncertain, destructive, irreversible, or inappropriate in context.
DeshkaAI explores a dedicated safety boundary before execution.
The system is designed around:
Risk classification
Confidence-aware decisions
Human-in-the-loop authorization
Pre-execution interception
Explicit execution boundaries
Auditability
Regression and behavioral testing
Architecture
DeshkaAI currently uses a pre-execution safety architecture.
AI / AGENT
    │
    ▼
Intent / Context
    │
    ▼
PFC PRE-EXECUTION INTERCEPTOR
    │
    ├── SAFE
    │     │
    │     ▼
    │   BDD SAFETY RULES
    │     │
    │     └──────────────┐
    │                    │
    └── HIGH / UNCERTAIN │
             │           │
             ▼           │
         SAFE_HOLD       │
             │           │
             ▼           │
        HUMAN REVIEW      │
             │           │
             ▼           │
          HITL GATE ──────┘
             │
             ▼
        AUDIT LOGGER
             │
             ▼
     EXECUTION BOUNDARY
A service integration can then expose the safety layer through a REST interface:
TOOL / API
    │
    ▼
SERVICE ARCHITECTURE
    │
    ▼
FastAPI / OpenAPI
    │
    ▼
PFC RISK CLASSIFIER
    │
    ▼
HITL GATE
    │
    ▼
AUDIT LOGGER
Safety Decision Model
DeshkaAI is designed to distinguish between actions that can proceed and actions that should stop before execution.
Lower-risk action
Request
   ↓
Risk evaluation
   ↓
LOW
   ↓
EXECUTE
High-risk or uncertain action
Request
   ↓
Risk evaluation
   ↓
HIGH / UNCERTAIN
   ↓
SAFE_HOLD
   ↓
HUMAN REVIEW
The safety layer is intended to prevent high-risk actions from reaching the execution layer without the required authorization.
Example
Low-risk request
User:
Show customer count

Safety result:
LOW
EXECUTE
The action can proceed through the authorized execution path.
Destructive request
User:
Delete all customer records

Safety result:
HIGH
SAFE_HOLD
The action is held before reaching the execution layer.
Conceptually:
AI / USER REQUEST
       ↓
SAFETY DECISION
       ↓
HIGH RISK
       ↓
SAFE_HOLD
       ↓
BLOCKED FROM EXECUTION
Key Components
1. Pre-Execution Interceptor
Intercepts an intended action before it reaches the execution layer.
Its purpose is to establish a dedicated decision boundary between AI intent and real-world action.
2. Risk Classification
Actions are evaluated according to their potential risk and uncertainty.
The system can distinguish between lower-risk actions and actions that require additional controls.
3. SAFE_HOLD
SAFE_HOLD represents a safety stop before execution.
It is intended for cases where an action is high-risk, uncertain, or requires additional authorization.
4. Human-in-the-Loop (HITL)
High-risk actions can be routed toward human review rather than being executed automatically.
This provides an explicit authorization boundary for protected actions.
5. Audit Logging
DeshkaAI uses JSON Lines (.jsonl) audit logging to support traceability of safety decisions and system behavior.
The goal is to make important decisions inspectable rather than silently disappearing inside an AI workflow.
6. FastAPI / OpenAPI Integration
The project includes a REST-oriented service architecture using FastAPI/OpenAPI.
This allows the safety layer to be positioned between an AI/agent system and downstream tools or APIs.
Verification
The current frozen baseline has been evaluated using multiple test groups.
PFC          9/9
Regression   14/14
BDD          8/8
HITL         4/4
Adversarial  17/18
The known adversarial false positive is intentionally retained and documented rather than presenting the benchmark as perfect.
This is important because the project treats transparent failure reporting as part of safety engineering.
Engineering Focus
DeshkaAI currently focuses on:
AI safety architecture
Pre-execution decision boundaries
Agent action governance
Risk classification
Human-in-the-loop workflows
FastAPI / OpenAPI services
JSONL audit logging
Behavioral testing
Regression testing
Adversarial testing
Responsible AI infrastructure
Repository Structure
The repository contains the implementation and documentation for the DeshkaAI safety architecture.
The exact structure may evolve as the project develops.
Deshka-Ai/
│
├── README.md
│
├── safety / core implementation
├── API / service integration
├── tests
├── audit / logging components
└── documentation
Local Setup
Clone the repository:
git clone https://github.com/arshadjdc/Deshka-Ai.git
cd Deshka-Ai
Install the Python dependencies:
pip install -r requirements.txt
The project is under active development, so service entry points and implementation structure may evolve between versions.
API / Service Layer
DeshkaAI is designed to expose its safety decision process through a service boundary.
The intended architecture is:
Client / AI Agent
       │
       ▼
FastAPI / OpenAPI
       │
       ▼
Safety Evaluation
       │
       ▼
Risk Decision
       │
   ┌───┴───────────────┐
   │                   │
 EXECUTE           SAFE_HOLD
   │                   │
   │              HUMAN REVIEW
   │                   │
   └────────┬──────────┘
            ▼
       Audit Logger
            │
            ▼
     Execution Boundary
Design Principles
1. Safety before execution
The safety decision should happen before an action reaches a tool or execution system.
2. Human control for high-risk actions
High-risk or uncertain actions should have an explicit path toward human review.
3. Model-agnostic architecture
The safety boundary is designed to sit outside the underlying AI model rather than depending on one specific model provider.
4. Transparent evaluation
Known failures and false positives should remain visible during development.
5. Auditable decisions
Important safety decisions should be recorded so system behavior can be inspected later.
Current Status
Frozen Baseline
The current safety architecture has a frozen baseline for the documented test groups.
Development continues around:
Safety evaluation
Regression coverage
Agent/tool integrations
API integration
Open-source documentation
Benchmarking
Reliability improvements
Open-Source Direction
DeshkaAI is being developed as an open-source exploration of safety infrastructure for AI and agent systems.
The project is particularly interested in the boundary between:
AI MODEL
   ↓
INTENDED ACTION
   ↓
SAFETY DECISION
   ↓
AUTHORIZED EXECUTION
The long-term goal is to make this boundary easier to integrate, test, inspect, and reason about.
Contributing
Contributions, feedback, issues, and technical discussion are welcome.
If you find a bug or an unexpected safety classification, please open an issue with:
The input/action
Expected behavior
Observed behavior
Relevant logs
Reproduction steps
Safety-related failures are especially valuable because they help improve the evaluation suite.
Project
DeshkaAI
Pre-Execution Safety & Governance Stack
GitHub:
https://github.com/arshadjdc/Deshka-Ai⁠�
Author:
Arshad Khan
Country:
India
Disclaimer
DeshkaAI is an experimental safety architecture and should not be treated as a guarantee that an AI system is safe or that every harmful action will be detected.
The project is intended to provide an additional safety and governance layer before AI-generated actions reach execution systems.
Building in Public
DeshkaAI is being developed openly with an emphasis on reproducible testing, transparent failure reporting, and practical AI safety engineering.
The project aims to explore one question:
What should happen in the moment between an AI deciding to act and the action actually reaching the real world?
That is the boundary DeshkaAI is trying to make safer.

## Proof of Work

The FastAPI gateway has been locally verified with:

- Health endpoint: `status = ok`
- Low-risk request: `LOW → EXECUTE`
- Destructive request: `HIGH → SAFE_HOLD`
- High-risk request: `execution_allowed = false`
- OpenAPI/Swagger documentation available at `/docs`

The gateway is explicitly simulation-only and does not execute
destructive or financial actions.

Docker configuration included; container build verification pending.
