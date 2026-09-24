# Grok Bot Roster: Autonomous Multi-Bot Fleet

> **Operational Architecture:** 20 Grok Bots running concurrently on a single shared physical machine. Each agent operates with its own sandboxed desktop, dedicated chat session, and sidebar hook.

---

## 📊 Fleet Overview

- **Total Active Bots:** 20 (including Chief of Staff coordinator)
- **Host Topology:** Single shared host with separate virtual desktop spaces and isolated chat contexts
- **Current Live Status:** All 20 bots are present and reachable in the sidebar; zero bots currently reporting an active blocking job.
- **Failover / Backup Layer:** Nous Research Hermes Desktop & Hermes Agent ([Guide](./NOUS-RESEARCH-HERMES-INSTALL.md)).

---

## 🎯 Bot Roster Categorization

### 1. Outreach & LinkedIn (9 Bots)

These bots specialize in UK IT contractor pipeline generation, outreach tracking, network expansion, and media syndicate distribution:

| Bot Name | Function & Purpose | Current State |
| :--- | :--- | :--- |
| **LinkedIn Contractor Responses** | Auto-drafts and handles replies to inbound recruiter and contractor threads. | Idle / Reachable |
| **Linkedin Followup Agent** | Systematically chases unanswered messages, pending connection requests, and post engagements. | Idle / Reachable |
| **Linkedin Connector** | Proactive connection outreach targeted at UK tech recruiters and hiring directors. | Idle / Reachable *(Lightly documented)* |
| **Linkedin Research** | Gathers company data, client tech stacks, contract rates, and decision-maker profiles. | Idle / Reachable *(Lightly documented)* |
| **Linkedin Job Apply** | Submits targeted LinkedIn job applications with tailored CV highlights. | Idle / Reachable *(Lightly documented)* |
| **Linkedin Stats** | Weekday profile & post analytics via Apify → Google Drive sync (Telegram alert upon completion). | Idle / Reachable |
| **Linkedin Youtube Posts** | Every-other-day LinkedIn posts drafted automatically from `@RifatErdemSahin` videos. | Idle / Reachable |
| **Linkedin Youtube Promote o Messages** | Direct messaging campaign to share relevant YouTube tutorials with active contractor peers. | Idle / Reachable *(Lightly documented)* |
| **youtube promotion on whatsapp** | Timed WhatsApp broadcasts of the latest video releases (enforces strict blacklist and no-double-send logic). | Idle / Reachable |

---

### 2. Jobs & Operations (11 Bots)

These bots manage back-office automation, physical ops, multi-machine access, code development, and strategic coordination:

| Bot Name | Function & Purpose | Current State |
| :--- | :--- | :--- |
| **Job Portal Applications** | UK contract applications on JobServe, CWJobs, and similar portals; logs all submissions to Google Drive. | Idle / Reachable |
| **Ms Todo Asistant** | Manages Microsoft To Do tasks for Hotmail account; synchronizes GitHub backups and specs docs. | Idle / Reachable |
| **Gmail asistant** | Inbox triage, email filtering, and contract inquiry draft assistance. | Idle / Reachable *(Lightly documented)* |
| **Cambridge And London Ai Events** | Scrapes, monitors, and collates high-impact AI/tech events in London and Cambridge. | Idle / Reachable |
| **Grocery** | Manages household grocery lists, recurring orders, and delivery coordination. | Idle / Reachable *(Lightly documented)* |
| **Any Desk Manager** | Maintains AnyDesk connections across physical hardware (e.g. Mac mini), keeping IDs and availability clear. | Idle / Reachable |
| **Github Coder** | Autonomous code generation, pull request reviews, test runs, and git pipeline execution. | Idle / Reachable *(Lightly documented)* |
| **Grokbot Installs** | Handles Grok Bot provisioning, API key rotation, dependencies, and environment bootstrapping. | Idle / Reachable *(Lightly documented)* |
| **Skool** | Community management, interaction tracking, and student engagement for Skool community. | Idle / Reachable *(Lightly documented)* |
| **Kingston Ram** | Hardware memory optimization / inventory tracker *(Named but lightly documented)*. | Idle / Reachable |
| **Chief Of Staff (me)** | Central orchestrator; coordinates tasks, monitors bottlenecks, and delegates across all 19 worker bots. | Active Coordinator |

---

## ⚡ Operational Guidelines & First Principles

1. **Shared Resource Management:**
   - Because all bots share one machine, CPU/RAM contention is minimized by event-driven wakeups rather than constant polling loops.
   - Background tasks report to Google Drive or Telegram upon milestone completion.
2. **Lightly Documented Bots Protocol:**
   - 10 bots (Research, Job Apply, Connector, Promote o Messages, Grocery, Skool, Github Coder, Grokbot Installs, Kingston Ram, Gmail) have foundational names but need deep historical audits.
   - Chief of Staff can drill into any individual bot workspace to inspect its last run artifacts, prompt cache, or logs upon request.
3. **Hermes Desktop Backup:**
   - If an xAI quota or connectivity interruption occurs, task payloads can be transferred directly to Hermes Desktop running locally on the same host.
