---
title: DOCX Document Engineering Guide
domain: document-engineering
summary: DOCX creation and XML editing standards using docx (npm), pandoc, and LibreOffice.
critical_directives:
- Tables require dual widths (columnWidths on table AND width on every cell in WidthType.DXA).
- Never use solid table shading (ShadingType.CLEAR only).
- PageBreak must always be placed inside a Paragraph.
section_outline:
- DOCX Document Engineering Guide
- Core Capabilities
- Creation Standards (`docx-js`)
read_triggers:
- When working on document-engineering in .agents/skills/docx/SKILL.md
- When reading context for DOCX Document Engineering Guide
tags:
- docx
- word
- document-processing
updated: '2026-08-08'
name: docx
description: Create, read, edit, and convert Microsoft Word documents (.docx, .dotx) using docx-js (Node.js), pandoc, and
  XML editing tools. Includes table width rules, tracked changes, and PDF conversion validation.
---

# DOCX Document Engineering Guide

## Core Capabilities

1. **New Document Creation**: `docx` (npm package) for programmatic document generation.
2. **Existing Document Editing**: XML manipulation of `word/document.xml` after unzipping `.docx` archives.
3. **Markdown / Text Extraction**: `pandoc -t markdown document.docx`.

---

## Creation Standards (`docx-js`)

```javascript
const { Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell, WidthType, PageBreak } = require("docx");

const doc = new Document({
  sections: [{
    properties: {
      page: { size: { width: 12240, height: 15840 } } // Letter size in DXA (1440 = 1 inch)
    },
    children: [
      new Paragraph({
        children: [new TextRun({ text: "Document Title", bold: true, size: 32 })]
      }),
      new Paragraph({
        children: [new PageBreak()]
      })
    ]
  }]
});
```

- **Dual Table Widths**: Specify `columnWidths` on `Table` AND `width` on every `TableCell` using `WidthType.DXA`.
- **Shading Safety**: Use `ShadingType.CLEAR`, never `SOLID` (prevents rendering as black boxes in Word & Google Docs).
- **No Raw Newlines**: Use separate `Paragraph` objects instead of `\n`.
