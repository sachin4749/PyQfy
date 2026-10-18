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
- [Comprehensive Feature Matrix](#comprehensive-feature-matrix)
- [Cascading Academic Structure](#cascading-academic-structure)
- [Prompt Engineering & AI Persona](#prompt-engineering--ai-persona)
- [Tech Stack & Dependencies](#tech-stack--dependencies)
- [Step-by-Step Local Setup](#step-by-step-local-setup)
- [Deployment on Streamlit Community Cloud](#deployment-on-streamlit-community-cloud)
- [PDF Generation Engine & NumberedCanvas](#pdf-generation-engine--numberedcanvas)
- [Formspree API Integration](#formspree-api-integration)
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
|  - PyPDF Text Extraction                                                          |
|  - Academic Context Tagging (Level > Stream > Subject)                           |
|  - Prompt Enhancement & System Persona Injection                                  |
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
