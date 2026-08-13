---
title: n8n Node Reference & Production Workflow Engine
domain: skill
summary: n8n is a 100% open-source, self-hosted workflow automation platform. Workflows in n8n are represented as JSON structures
  containing `nodes`, `connections`, and `settings`. | Category | Node Type String | Usage / Purpose |
critical_directives:
- Follow document guidance without bypassing established safeguards.
section_outline:
- n8n Node Reference & Production Workflow Engine
- Overview
- Standard Node Types (`n8n-nodes-base.*`)
- n8n Expression Standard
- 1-Click Launch Script (`start_n8n.bat`)
read_triggers:
- When working on skill in .agents/skills/n8n/references/n8n-nodes-guide.md
- When reading context for n8n Node Reference & Production Workflow Engine
tags:
- skill
- n8n-nodes-guide
updated: '2026-08-08'
---

# n8n Node Reference & Production Workflow Engine

## Overview

n8n is a 100% open-source, self-hosted workflow automation platform. Workflows in n8n are represented as JSON structures containing `nodes`, `connections`, and `settings`.

---

## Standard Node Types (`n8n-nodes-base.*`)

| Category | Node Type String | Usage / Purpose |
|---|---|---|
| **Triggers** | `n8n-nodes-base.webhook` | HTTP Webhook listener for incoming POST/GET payloads |
| **Triggers** | `n8n-nodes-base.cron` | Scheduled timer trigger (runs on cron expressions) |
| **Spreadsheets** | `n8n-nodes-base.googleSheets` | Read/Write/Append/Update rows in Google Sheets |
| **HTTP Request** | `n8n-nodes-base.httpRequest` | Raw REST API caller (GET, POST, PUT, DELETE) |
| **Logic & Control** | `n8n-nodes-base.if` | Conditional branching based on expressions |
| **Logic & Control** | `n8n-nodes-base.switch` | Multi-branch routing based on field values |
| **Code Execution** | `n8n-nodes-base.code` | Custom JavaScript or Python code node for data transformation |
| **Communication** | `n8n-nodes-base.emailSend` | Send email via SMTP or direct server connection |
| **Database** | `n8n-nodes-base.postgres` | Read/Write PostgreSQL / Supabase databases |

---

## n8n Expression Standard

n8n uses JS expressions inside double curly braces:
- Access incoming item data: `{{ $json.fieldName }}`
- Access query params: `{{ $json.query.paramName }}`
- Access headers: `{{ $json.headers["x-api-key"] }}`
- Null guard: `{{ $json.phone ? $json.phone.replace(/[^0-9]/g, '') : '' }}`
- Format dates: `{{ $today.format('YYYY-MM-DD') }}`

---

## 1-Click Launch Script (`start_n8n.bat`)

```batch
@echo off
echo Starting ZORIXEL Client Self-Hosted n8n Automation Engine...
npx n8n
```
