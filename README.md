# PyQfy - Smart PYQ & Academic Intelligence Hub

![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue.svg?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.30%2B-red.svg?style=for-the-badge&logo=streamlit&logoColor=white)
![Google Gemini](https://img.shields.io/badge/Google%20Gemini-3.8%20Flash-orange.svg?style=for-the-badge&logo=googlegemini&logoColor=white)
![ReportLab](https://img.shields.io/badge/ReportLab-PDF%20Engine-blueviolet.svg?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)

**PyQfy** is an enterprise-grade academic evaluation and AI platform engineered to ingest Previous Year Question (PYQ) papers, parse complex multi-question structures, and synthesize exhaustive, professor-level model answers. Powered by **Google Gemini (`gemini-3.8-flash`)**, PyQfy bridges the gap between raw examination papers and structured academic mastery through deep automated analysis, real-time AI assistance, and dynamic multi-page PDF report compilation.

---

## Table of Contents

- [Overview & Vision](#overview--vision)
- [System Architecture](#system-architecture)
- [Detailed Pipeline & Component Breakdown](#detailed-pipeline--component-breakdown)
- [Comprehensive Feature Matrix](#comprehensive-feature-matrix)
- [Cascading Academic Structure](#cascading-academic-structure)
- [Prompt Engineering & AI Persona](#prompt-engineering--ai-persona)
- [UI/UX & Glassmorphic Styling](#uiux--glassmorphic-styling)
- [Tech Stack & Dependencies](#tech-stack--dependencies)
- [Step-by-Step Local Setup](#step-by-step-local-setup)
- [Deployment on Streamlit Community Cloud](#deployment-on-streamlit-community-cloud)
- [PDF Generation Engine & NumberedCanvas](#pdf-generation-engine--numberedcanvas)
- [Formspree API Integration](#formspree-api-integration)
- [Security & Rate-Limit Resilience](#security--rate-limit-resilience)
- [Troubleshooting & Common Edge Cases](#troubleshooting--common-edge-cases)
- [Project Directory Structure](#project-directory-structure)
- [Author & Branding](#author--branding)
- [License](#license)

---

## Overview & Vision

Preparing for university exams and competitive degrees requires analyzing years of Previous Year Question papers. Students and educators frequently spend dozens of hours searching for reliable mark-scheme solutions and structured derivations.

**PyQfy** solves this challenge by serving as an all-in-one **Smart PYQ & Academic Intelligence Hub**. By combining document parsing (`pypdf`) with Large Language Models (`gemini-3.8-flash`), PyQfy ingests whole question papers in seconds and breaks them down into complete model answers, marking scheme tips, step-by-step derivations, and real-world examples.

---

## System Architecture

```text
+-----------------------------------------------------------------------------------+
|                                 USER INTERFACE                                    |
|              (Streamlit Glassmorphic Dark UI / Cascading Selectors)                |
+----------------------------------------+------------------------------------------+
                                         |
                                         v
+-----------------------------------------------------------------------------------+
|                                 INPUT HANDLING                                    |
|            [Upload PDF / Upload TXT]   OR   [Direct Text Pasting]                 |
+----------------------------------------+------------------------------------------+
                                         |
                                         v
+-----------------------------------------------------------------------------------+
|                             CORE PROCESSING ENGINE                                |
|  - PyPDF Text Extraction & Sanitization                                           |
|  - Academic Context Tagging (Level > Stream > Subject)                           |
|  - System Persona Injection & Dynamic Prompt Packaging                            |
+----------------------------------------+------------------------------------------+
                                         |
                                         v
+-----------------------------------------------------------------------------------+
|                            AI REASONING SERVICE                                   |
|                        Google Gemini (gemini-3.8-flash)                            |
+----------------------------------------+------------------------------------------+
                                         |
                                         v
+-----------------------------------------------------------------------------------+
|                                OUTPUT GENERATION                                  |
|  1. Interactive Web Display (Cached Session State)                                |
|  2. ReportLab PDF Engine (HTML Sanitization + NumberedCanvas Page X of Y)          |
|  3. Formspree API Gateway (Asynchronous User Feedback)                           |
+-----------------------------------------------------------------------------------+
```

---

## Detailed Pipeline & Component Breakdown

Following the high-level architecture diagram above, the internal execution lifecycle follows a strict four-stage processing paradigm:

### 1. Multi-Format Input & Sanitization Pipeline
* **File Parsing (`PyPDF` Layer):** When a user uploads an academic question paper in PDF format, the text layer is extracted page-by-page. Special whitespace characters, line wraps, and non-printable control characters are normalized.
* **Direct Raw Text Injection:** Alternative input methods accept direct copy-pasted textual question sets or UTF-8 encoded text files (`.txt`), bypassing heavy parser overhead for quick evaluation.

### 2. Context Priming & Cascade Hierarchy
* **Context Selection:** Academic categorization selects three relational tiers: **Level**, **Stream**, and **Subject**.
* **System Prompt Augmentation:** The user's input text is wrapped in domain-specific evaluative constraints, informing the Gemini LLM of exact expected rigor (e.g., Undergraduate Computer Science vs. Higher Secondary Physics).

### 3. Inference Engine & Session Management
* **Model Request:** Structured prompts are transmitted to `gemini-3.8-flash` utilizing the official `google-generativeai` client module.
* **State Preservation:** Generated answers are instantly stored within Streamlit's `st.session_state`. This eliminates re-triggering API calls when interacting with auxiliary interface tabs or downloading generated PDF reports.

### 4. Dual Output Synthesizer
* **Dynamic Markdown Rendering:** Real-time web visualization with styled headers, formatted code/math blocks, and highlighting.
* **ReportLab Vector Graphics Compilation:** Generated answers undergo HTML entity encoding (`html.escape`) and tag translation (`**bold**` to `<b>bold</b>`) before being pushed into a custom two-pass canvas renderer to create physical print-ready PDF files.

---

## Comprehensive Feature Matrix

| Feature | Description | Impact / Benefit |
| :--- | :--- | :--- |
| **Cascading Dropdowns** | Dynamic 3-stage selector (Level > Stream > Subject). | Prevents mismatched selections and ensures accurate domain prompting. |
| **Multi-Source Ingestion** | Supports native PDF uploads, plain TXT files, and raw text pasting. | Handles clean vector PDFs as well as text inputs seamlessly. |
| **Deep Solution Breakdown** | Formats answers into Core Concepts, Derivations, Examples, and Exam Tips. | Matches official university marking schemes for maximum scoring. |
| **NumberedCanvas PDF** | Generates formal PDF downloads with custom headers and "Page X of Y". | Provides clean printouts for physical study materials and archives. |
| **Session Caching** | Retains model answers in Streamlit `session_state`. | Prevents redundant API calls and accidental loss of generated work. |
| **AI Academic Chatbot** | Dedicated interactive Assistant for query resolution. | Solves specific numerical doubts or individual sub-questions on the fly. |
| **API Feedback Gateway** | Formspree REST endpoint integration using Python `requests`. | Sends user feedback directly to the administrator's inbox. |
| **Glassmorphic UI** | Frosted glass card UI with neon gradients and custom scrollbars. | Ensures an immersive, high-end, emoji-free dark mode experience. |

---

## Cascading Academic Structure

PyQfy organizes academic content into a multi-tier hierarchy to prime the Gemini LLM with contextually accurate domain knowledge:

1. **10th Standard**
   - **General Curriculum:** Mathematics, Science, Social Science, English, Hindi
2. **11th & 12th Standard**
   - **Science (PCM/PCB):** Physics, Chemistry, Mathematics, Biology, Computer Science
   - **Commerce:** Accountancy, Business Studies, Economics, Business Mathematics
   - **Arts / Humanities:** History, Political Science, Geography, Sociology, Economics
3. **Undergraduate (B.Tech / B.E)**
   - **Computer Science & Engineering:** Data Structures & Algorithms, Operating Systems, Database Management Systems, Computer Networks, Software Engineering
   - **Electronics & Communication:** Digital Logic Design, Signals and Systems, Microcontrollers, Analog Circuits
   - **Mechanical / Civil Engineering:** Engineering Mechanics, Strength of Materials, Fluid Mechanics, Structural Analysis
4. **Postgraduate (M.Tech / MCA / MBA)**
   - **Computer Applications (MCA):** Advanced Data Structures, Web Technologies, Python Programming, Cloud Computing, Artificial Intelligence
   - **Management (MBA):** Financial Management, Marketing Management, Human Resource Management, Strategic Management
   - **Engineering (M.Tech):** Advanced Algorithms, Machine Learning, Research Methodology
5. **General Degrees (BA / B.Sc / B.Com)**
   - **Arts (BA):** English Literature, History, Political Science, Economics, Psychology
   - **Science (B.Sc):** Physics, Chemistry, Mathematics, Botany, Zoology
   - **Commerce (B.Com):** Financial Accounting, Corporate Tax, Business Law, Auditing

---

## Prompt Engineering & AI Persona

PyQfy leverages a system prompt designed to transform Gemini into a Senior Academic Evaluator:

```text
You are PyQfy's Elite Academic AI Professor and Expert Evaluator.
Your core objective is to provide exceptionally deep, accurate, rigorous, and exhaustive model answers for academic questions and question papers.

RULES FOR ANSWERING:
1. EXTRACT AND SOLVE ALL: Carefully scan the provided text or prompt. Identify every single question, sub-question, or numerical problem. Do NOT skip anything.
2. STRUCTURED DEEP BREAKDOWN: For every question, structure your response professionally using these headings:
   - Core Concept & Definition: Clear theoretical foundation and definitions.
   - Detailed Step-by-Step Explanation / Derivation / Calculation: In-depth breakdown with mathematical formulas, core principles, or logical steps. Avoid superficial summaries; provide complete depth.
   - Illustrative Example / Application: Where applicable, provide a short example or use case.
   - Exam Scoring Tip: Give precise advice on what examiners look for to award full marks.
3. MAINTAIN ACADEMIC RIGOR: Use proper terminology relevant to the subject.
```

---

## UI/UX & Glassmorphic Styling

PyQfy avoids standard flat templates in favor of a modern **Dark Glassmorphic Theme**:
- **Palette:** Deep Navy Background (`#030712`), Electric Blue (`#3b82f6`), Soft Purple (`#a78bfa`), and Muted Slate (`#94a3b8`).
- **Cards & Panels:** Custom `backdrop-filter: blur(24px)` with translucent borders (`rgba(255, 255, 255, 0.08)`).
- **Typography:** High-contrast CSS radial text-gradients and clean web fonts (`Inter`).
- **Interactive Controls:** Sleek glowing primary buttons and custom WebKit scrollbars (`#1e293b`).

---

## Tech Stack & Dependencies

- **Framework:** Streamlit (`>=1.30.0`)
- **Generative AI SDK:** Google Generative AI (`gemini-3.8-flash`)
- **PDF Parser:** PyPDF (`pypdf>=3.17.0`)
- **PDF Engine:** ReportLab (`reportlab>=4.0.0`)
- **HTTP Client:** Requests (`requests>=2.31.0`)

---

## PDF Generation Engine & NumberedCanvas

---

## Formspree API Integration

---


## Project Directory Structure

```text
pyqfy/
├── .streamlit/
│   └── secrets.toml          # Local API Key Secrets (Git Ignored)
├── app.py                    # Main Application Logic
├── requirements.txt          # Python Dependencies
├── .gitignore                # Git Exclusions
└── README.md                 # Complete Documentation
```

---

## Author & Branding

- **Brand & Design:** **SK Graphics**
- **Lead Developer:** **Sachin K** (`sachin4749`)
- **Project Name:** PyQfy

---

## License

MIT License

Copyright (c) 2026 Sachin K (SK Graphics)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
