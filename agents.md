# AGENTS.md — GrokBot Coordinator & Agent Rules

`agents.md` is the **coordinator** and single source of truth for all agent mandates, project conventions, and execution rules in the `grokbot` repository. All agents must read and strictly adhere to the guidelines below.

---

## 🧠 Always Remember (Mandatory Agent Directives)

### 1. Bloom's Taxonomy Navigation & Educational Hierarchy
All user-facing documentation, web interfaces, and educational tools must implement the cognitive sequence:
1. **Remember**: Recall foundational primitives, prerequisite commands, xAI endpoints (`https://api.x.ai/v1`), and model constants.
2. **Understand**: Deconstruct concepts through first principles (physics of information latency, epistemic truth vs alignment tax, supercomputing scale).
3. **Analyse**: Examine architectural differentiation (live X firehose integration, zero preachiness, OpenAI drop-in compatibility, comparison matrix).
4. **Evaluate**: Assess engineering trade-offs, ROI, suitability scoring, and decision boundaries.
5. **Create**: Hands-on building, installation pipeline, runnable Python scripts ([`src/grok_bot.py`](./src/grok_bot.py)), and testing simulators.

### 2. Server Port Policy (30,000+ Mandate)
- **Always** run local application and development preview servers on ports **over 30,000+** (e.g., `30110`, `30080`).
- **Never** bind to standard lower ports (e.g., `3000`, `8000`, `8080`) to eliminate port collisions with system and background services.

### 3. Browser Policy (Google Chrome Only)
- Whenever launching or previewing local servers, web endpoints, or documentation, **ALWAYS use Google Chrome**:
  ```bash
  open -a "Google Chrome" <URL>
  ```

### 4. Git Commit & Push Discipline
- **After every command and milestone, commit and push** to remote:
  ```bash
  git add <files>
  git commit -m "<clear descriptive message>"
  git push origin main
  ```
- Do not batch or leave unpushed commits lingering. Proactively resolve any git conflicts or index issues.

### 5. First Principles Engineering
- Do not build by analogy. Deconstruct every system to its irreducible physical and computational limits:
  - What is the information horizon?
  - What is the computational and memory bottleneck?
  - What is the minimum viable telemetry path to truth?

### 6. Clickable Links at Response Termination
- Whenever modifying or creating HTML pages or web resources, **ALWAYS** output clickable markdown links at the very end of the response.

---

## 🛠️ Project Structure & Execution Conventions

```
grokbot/
├── index.html          # Main interactive guide: Bloom's taxonomy, install/usage,
│                       # LinkedIn real-time playbook, evidence gallery
├── src/
│   └── grok_bot.py     # Runnable first-principles xAI agent proof of concept
├── images/             # Phase-ordered evidence screenshots (NN-description.jpg)
├── docs/
│   └── REPORT.md       # Installation, file scan/rename, grouping, rationale report
├── .env.example        # Environment variable template (XAI_API_KEY)
├── .gitignore          # Excludes venv/ and .env secrets
├── requirements.txt    # Python dependencies (openai, python-dotenv, requests)
├── README.md           # Project summary
└── agents.md           # Coordinator rules and always remember mandates
```

### File Grouping Convention
- **`src/`** — all runnable code.
- **`images/`** — evidence only, named `NN-kebab-case-description.jpg`, ordered by phase.
- **`docs/`** — written reports and long-form prose.
- **Root** — site entrypoint (`index.html`) and project config only.

### Menu Grouping Convention
Navigation must be grouped by purpose, not dumped as one flat list. The canonical groups are:
1. **Guide** — Bloom levels 1–5 (Remember, Understand, Analyse, Evaluate, Create).
2. **Install & Use** — install, usage, custom bots & plugins.
3. **LinkedIn Playbook** — real-time rationale, daily routine, reply template.
4. **Evidence** — screenshot gallery and reports.

---

## 🚀 Quick Run Commands

```bash
# 1. Environment Activation
source venv/bin/activate

# 2. Local HTTP Server (Port 30,000+)
python3 -m http.server 30110

# 3. Launch in Chrome
open -a "Google Chrome" http://localhost:30110/index.html

# 4. Run GrokBot CLI
python3 src/grok_bot.py "Explain quantum entanglement from first principles"
```
