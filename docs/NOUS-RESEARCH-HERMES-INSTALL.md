# Nous Research Hermes Agent & Hermes Desktop Installation Guide

> **Ecosystem Positioning:** Primary Open-Source Local Agent Framework & Resilient Backup Option to GrokBot (xAI).

---

## 🧭 Executive Summary & First Principles Rationale

In autonomous multi-agent environments, redundancy and fault-tolerance are primary physical and operational imperatives:
- **Primary Agent Driver:** **GrokBot (xAI Grok)** provides real-time access to the X firehose, high-speed cloud reasoning, zero-filter epistemic truth, and contractor market intelligence.
- **Secondary / Backup Agent:** **Nous Research Hermes Agent & Hermes Desktop** functions as the hardened, autonomous local and open-source **backup option**. If cloud API connectivity, rate limits, or upstream tokens become constrained, Hermes Desktop runs on the same physical host with local models (llama.cpp) or multi-provider fallbacks.

Both systems can operate alongside each other on macOS, maintaining parallel workspaces, skills, and session memory.

---

## 🛠️ System Architecture & Prerequisites

The Hermes stack consists of:
1. **Hermes Agent Core (CLI / Daemon):** Python 3.11 virtual environment powered by `uv`, handling tool executions, ACP, session history, and skill management.
2. **Hermes Desktop (Electron App):** Native macOS GUI (`Hermes.app`) built with Vite, React, and Electron, offering side-by-side previews, file inspection, voice channels, and multi-bot workspace visibility.

### Verified Local Host Specifications
- **Operating System:** macOS Darwin (arm64 / Apple Silicon)
- **Node.js:** `v22.22.0` (managed via nvm)
- **Package Manager:** `npm` + `uv`
- **Python:** `3.11.15`
- **Electron:** `40.10.2`
- **Installed App Location:** `~/Applications/Hermes.app` & `~/.hermes/hermes-agent/apps/desktop/release/mac-arm64/Hermes.app`

---

## 🚀 Installation & Build Procedures

### Step 1: Clone / Update Hermes Agent Core
```bash
# If installing freshly:
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash -s -- --skip-setup --non-interactive

# Or update existing checkout:
cd ~/.hermes/hermes-agent
git fetch --depth 1 origin main
git reset --hard origin/main
```

### Step 2: Install Python Dependencies via UV
```bash
cd ~/.hermes/hermes-agent
~/.local/bin/uv pip install -e . --python ./venv/bin/python
```

Verify version:
```bash
hermes --version
# Output: Hermes Agent v0.21.4 (2026.9.21) · upstream d188a47e
```

### Step 3: Build & Package Hermes Desktop
```bash
# Direct build via CLI
hermes desktop --build-only

# Or manual build within workspace:
cd ~/.hermes/hermes-agent/apps/desktop
npm ci --include=optional
npm run pack
```

### Step 4: Deploy Hermes.app to Applications
```bash
mkdir -p ~/Applications
cp -R ~/.hermes/hermes-agent/apps/desktop/release/mac-arm64/Hermes.app ~/Applications/Hermes.app
```

---

## 🖥️ Launch & Operational Commands

| Objective | Command |
| :--- | :--- |
| **Launch Desktop App** | `open -a ~/Applications/Hermes.app` or `hermes desktop` |
| **Run CLI Chat** | `hermes` |
| **Run One-Shot Prompt** | `hermes -z "Check system status and report back"` |
| **Start Web Dashboard** | `hermes dashboard` *(runs on port 9119)* |
| **Check Doctor & Health** | `hermes doctor` |
| **Update Everything** | `hermes update` |

---

## 🔄 Hermes as the GrokBot Backup Option

When operating the 20 Grok Bot roster across a shared machine:
1. **Fallback Provider Chain:** Hermes supports `hermes fallback add <provider>` allowing automatic rerouting from xAI to OpenRouter, Anthropic, or local GGUF weights.
2. **Independent Desktop UI:** Hermes Desktop provides a sandboxed window per task, allowing visual inspection of file system changes, shell commands, and headless browser sessions without disturbing active GrokBot jobs.
3. **Disaster Recovery:** If the xAI API encounters latency or quota limits during high-volume contractor outreach, Hermes stands ready to take over scheduled background runs.

---

*Authored for the GrokBot Fleet Operations • Single Source of Truth.*
