---
title: XLSX Spreadsheet Engineering Guide
domain: spreadsheet-engineering
summary: XLSX and CSV spreadsheet creation, formula auditing, data cleaning, and openpyxl formatting.
critical_directives:
- Use formulas over hardcoded numbers (e.g. '=SUM(B2:B9)').
- Post-2007 Excel functions (TEXTJOIN, IFS, MINIFS) require '_xlfn.' prefix when written in openpyxl strings.
- Never use XLOOKUP, XMATCH, or dynamic spill array functions; use INDEX and MATCH for maximum LibreOffice/Excel compatibility.
section_outline:
- XLSX Spreadsheet Engineering Guide
- Core Capabilities
- Formula Rules & Compatibility
- Financial Modeling Standards
read_triggers:
- When working on spreadsheet-engineering in .agents/skills/xlsx/SKILL.md
- When reading context for XLSX Spreadsheet Engineering Guide
tags:
- xlsx
- openpyxl
- pandas
- spreadsheets
updated: '2026-08-08'
name: xlsx
description: Spreadsheet manipulation, creation, editing, data cleaning, formula recalculation, financial modeling, and bulk
  data import/export with openpyxl, pandas, and LibreOffice.
---

# XLSX Spreadsheet Engineering Guide

## Core Capabilities

1. **Cell Formatting & Formula Creation**: `openpyxl` for explicit styling, cell colors, number formats, and formulas.
2. **Bulk Data I/O**: `pandas` (`pd.read_excel`, `df.to_excel`) for mass data manipulation and conversion.
3. **Data Inspection**: `markitdown file.xlsx` for rapid text layout inspection.

---

## Formula Rules & Compatibility

- **Formula Integrity**: Always write formulas (`ws['B10'] = '=SUM(B2:B9)'`) instead of hardcoded totals so workbooks remain interactive.
- **Prefix Guard**: Functions introduced post-Excel 2007 require the `_xlfn.` prefix when set via openpyxl strings (e.g., `_xlfn.TEXTJOIN(...)`, `_xlfn.IFS(...)`).
- **Compatibility Mandate**: Avoid `XLOOKUP`, `XMATCH`, `UNIQUE`, `FILTER`, `SORT`, or `SEQUENCE`. Use classic `INDEX(..., MATCH(...))` for 100% deterministic evaluation across Excel, Google Sheets, and LibreOffice engines.
- **Quoted Sheet Names**: Cross-sheet references with spaces MUST be quoted (e.g., `='Financial Summary'!B5`).

---

## Financial Modeling Standards

- **Color Coding**: Blue text (`#0000FF`) for hardcoded inputs; Black text for formula cells; Green text (`#008000`) for cross-sheet references; Yellow fill (`#FFFF00`) for user-input target cells.
- **Number Formats**: Currency `$#,##0` or `$#,##0.00`; Negatives in parentheses `($#,##0)`; Percentages stored as fractions (`0.15` for `15.0%`).
