---
title: Self-Hosted n8n Production Workflow Engine
domain: workflow-automation
summary: Complete self-hosted n8n workflow generation and launch engine.
critical_directives:
- Always export complete, executable n8n workflow JSON files with valid nodes and connections array.
- Include 1-click startup scripts (start_n8n.bat / start_n8n.sh) for client execution.
section_outline:
- Self-Hosted n8n Production Workflow Engine
- Overview
- Operating Instructions
- 1. Build Full n8n Workflow JSON
- 2. Generate Client Launch Script
read_triggers:
- When working on workflow-automation in .agents/skills/n8n/SKILL.md
- When reading context for Self-Hosted n8n Production Workflow Engine
tags:
- n8n
- automations
- webhooks
- workflows
updated: '2026-08-08'
name: n8n
description: Self-hosted n8n visual workflow automation engine based on official n8n architecture (https://github.com/n8n-io/n8n).
  Create, export, import, and execute 100% free open-source n8n full production workflows (.json files) and batch launch scripts
  for client automations, webhooks, database syncs, and multi-channel messaging without subscription fees.
---

# Self-Hosted n8n Production Workflow Engine

## Overview

Based on [github.com/n8n-io/n8n](https://github.com/n8n-io/n8n), this skill builds full, executable n8n visual automation workflows for client handoffs. All workflows are 100% zero-subscription and run locally or on a client VPS via `npx n8n` or Docker.

For detailed node parameters, expressions, and syntax, see [references/n8n-nodes-guide.md](references/n8n-nodes-guide.md).

---

## Operating Instructions

### 1. Build Full n8n Workflow JSON
Construct a complete, valid n8n JSON file containing:
- **`nodes`**: Array of triggers (`n8n-nodes-base.webhook`), logic (`n8n-nodes-base.if`), spreadsheets (`n8n-nodes-base.googleSheets`), code (`n8n-nodes-base.code`), and API callers (`n8n-nodes-base.httpRequest`).
- **`connections`**: Complete graph mapping node outputs to downstream inputs.
- **`settings`**: `{ "executionOrder": "v1" }`.

Save the resulting JSON to `output/n8n_full_workflow.json`.

### 2. Generate Client Launch Script
Save a 1-click startup script `start_n8n.bat` for Windows and `start_n8n.sh` for Linux/Mac alongside the workflow JSON:

```batch
@echo off
echo Starting ZORIXEL Self-Hosted n8n Automation Engine...
npx n8n
```

---

## Complete Executable Workflow Example

```json
{
  "name": "ZORIXEL Zero-Subscription Client Pipeline",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "client-webhook",
        "responseMode": "onReceived",
        "options": {}
      },
      "name": "Client Webhook Trigger",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1,
      "position": [250, 300]
    },
    {
      "parameters": {
        "jsCode": "return $input.all().map(item => ({\n  json: {\n    ...item.json,\n    processed_at: new Date().toISOString(),\n    status: 'ACTIVE'\n  }\n}));"
      },
      "name": "Transform & Clean Payload",
      "type": "n8n-nodes-base.code",
      "typeVersion": 1,
      "position": [450, 300]
    }
  ],
  "connections": {
    "Client Webhook Trigger": {
      "main": [
        [
          {
            "node": "Transform & Clean Payload",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  },
  "settings": {
    "executionOrder": "v1"
  }
}
```
