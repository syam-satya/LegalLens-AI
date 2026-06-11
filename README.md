# LegalLens AI

## Overview

LegalLens AI is an AI-powered Loan & EMI Contract Risk Analyzer that helps users understand loan agreements before signing them.

The system automatically extracts information from loan contracts, identifies potential risks, checks compliance with financial regulations, retrieves relevant RBI guidelines, and generates borrower-friendly explanations using Large Language Models (LLMs).

The goal of LegalLens AI is to simplify complex financial documents and help users make informed borrowing decisions.

---

## Features

### Contract Analysis

* PDF Loan Contract Upload
* Automatic Text Extraction
* Structured Contract Parsing
* Interest Rate Detection
* Processing Fee Detection
* Foreclosure Charge Detection
* Late Payment Fee Detection

### Risk Assessment

* Risk Detection Engine
* Contract Risk Scoring
* High / Medium / Low Risk Classification
* Compliance Issue Identification

### AI-Powered Insights

* Plain-English Contract Summary
* Borrower-Friendly Explanation
* AI Recommendations
* Contract Simplification
* Risk Explanation Generation

### Regulatory Intelligence

* RBI Rule Retrieval
* Semantic Search using Vector Embeddings
* Relevant Regulation Matching

### Contract Comparison

* Compare Multiple Loan Contracts
* Interest Rate Comparison
* Fee Comparison
* Risk Comparison
* AI-Based Recommendation

### Data Management

* Analysis History Storage
* Dashboard Statistics
* Historical Analysis Tracking

---

## System Architecture

User Uploads PDF

↓

PDF Text Extraction

↓

Contract Parsing

↓

Risk Detection

↓

Compliance Checking

↓

Regulatory Retrieval (RAG)

↓

AI Explanation Engine

↓

Analysis Storage

↓

Frontend Dashboard

---

## Tech Stack

### Backend

* Python
* FastAPI
* SQLAlchemy
* SQLite

### AI & NLP

* OpenRouter API
* OpenAI SDK
* Sentence Transformers
* FAISS Vector Search

### PDF Processing

* PyMuPDF (fitz)

### Frontend

* HTML
* CSS
* JavaScript

### Reporting

* ReportLab

---

## Project Structure

```text
LegalLens-AI/

├── backend/
│   ├── app/
│   ├── scripts/
│   ├── data/
│   └── requirements.txt
│
├── frontend/
│   ├── index.html
│   ├── upload.html
│   ├── result.html
│   ├── compare.html
│   ├── css/
│   └── js/
│
└── README.md
```

---

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd LegalLens-AI
```

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Virtual Environment

Windows:

```bash
.venv\Scripts\activate
```

Linux / Mac:

```bash
source .venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file inside the backend folder.

```env
LLM_PROVIDER=open_router

LLM_API_KEY=YOUR_OPENROUTER_API_KEY

OPENROUTER_MODEL=mistralai/mistral-7b-instruct
```

---

## Run Backend

```bash
cd backend

uvicorn app.main:app --reload
```

Backend URL:

```text
http://127.0.0.1:8000
```

Swagger Documentation:

```text
http://127.0.0.1:8000/docs
```

---

## Run Frontend

```bash
cd frontend

python -m http.server 5500
```

Frontend URL:

```text
http://127.0.0.1:5500
```

---

## Main API Endpoints

### Upload & Analyze Contract

```http
POST /upload-and-analyze
```

### Compare Contracts

```http
POST /compare-contracts
```

### Analysis History

```http
GET /history
```

### Dashboard Statistics

```http
GET /dashboard-stats
```

### Health Check

```http
GET /health
```

---

## Future Enhancements

* OCR Support for Scanned PDFs
* Multi-Language Contract Analysis
* Cloud Storage Integration
* User Authentication
* Advanced Compliance Engine
* Real-Time Financial Risk Monitoring
* Loan Recommendation System

---

## Project Goals

* Simplify financial contracts
* Improve borrower awareness
* Reduce hidden fee risks
* Enhance contract transparency
* Provide AI-assisted financial decision support

---

## Author

Developed as an AI-powered LegalTech project using FastAPI, Retrieval-Augmented Generation (RAG), Large Language Models, and Financial Risk Analysis techniques.
