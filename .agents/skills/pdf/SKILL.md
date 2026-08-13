---
title: PDF Processing & Generation Engine
domain: pdf-processing
summary: PDF manipulation, extraction, report building, form filling, and OCR processing using Python and CLI tools.
critical_directives:
- Never use Unicode subscript/superscript characters in ReportLab PDFs; use ReportLab XML tags (<sub>, <super>).
section_outline:
- PDF Processing & Generation Engine
- Core Capabilities
- Python Implementation Patterns
- 1. Extract Text & Tables with `pdfplumber`
- 2. Merge & Split with `pypdf`
read_triggers:
- When working on pdf-processing in .agents/skills/pdf/SKILL.md
- When reading context for PDF Processing & Generation Engine
tags:
- pdf
- pypdf
- pdfplumber
- reportlab
updated: '2026-08-08'
name: pdf
description: Use this skill whenever the user wants to process, read, edit, merge, split, extract text/tables, fill forms,
  or create PDF files. Includes pypdf, pdfplumber, reportlab, and qpdf command standards.
---

# PDF Processing & Generation Engine

## Core Capabilities

1. **Text & Table Extraction**: `pdfplumber` for structured text and Pandas DataFrames from PDF tables.
2. **Merge, Split, Rotate**: `pypdf` (`PdfReader`, `PdfWriter`) or `qpdf` for lossless PDF manipulation.
3. **PDF Generation**: `reportlab` (`SimpleDocTemplate`, `canvas`, `Paragraph`) for dynamic document rendering.
4. **Form Filling**: `pdf-lib` or `pypdf` for interactive form field extraction and filling.
5. **OCR & Image Extraction**: `pytesseract` + `pdf2image` for scanned PDF text extraction.

---

## Python Implementation Patterns

### 1. Extract Text & Tables with `pdfplumber`

```python
import pdfplumber
import pandas as pd

with pdfplumber.open("document.pdf") as pdf:
    tables = []
    for page in pdf.pages:
        text = page.extract_text()
        page_tables = page.extract_tables()
        for t in page_tables:
            if t:
                df = pd.DataFrame(t[1:], columns=t[0])
                tables.append(df)
```

### 2. Merge & Split with `pypdf`

```python
from pypdf import PdfReader, PdfWriter

# Merge multiple PDFs
writer = PdfWriter()
for pdf_file in ["doc1.pdf", "doc2.pdf"]:
    reader = PdfReader(pdf_file)
    for page in reader.pages:
        writer.add_page(page)

with open("merged_output.pdf", "wb") as f:
    writer.write(f)
```

### 3. Create PDF Reports with `reportlab`

> [!IMPORTANT]
> Never use Unicode subscript/superscript characters (`₀₁₂₃`, `⁰¹²³`) in ReportLab as built-in fonts render them as black boxes. Use `<sub>` and `<super>` XML tags inside `Paragraph` objects instead.

```python
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

doc = SimpleDocTemplate("report.pdf", pagesize=letter)
styles = getSampleStyleSheet()
story = []

story.append(Paragraph("Executive Summary", styles['Title']))
story.append(Spacer(1, 12))
story.append(Paragraph("Formula: H<sub>2</sub>O and E = mc<super>2</super>", styles['Normal']))

doc.build(story)
```
