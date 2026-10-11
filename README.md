# 🚀 PagePulse — URL Audit API

<p align="center">
  <strong>A Python FastAPI service for analyzing website URLs and retrieving useful technical metadata.</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI">
  <img src="https://img.shields.io/badge/Pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white" alt="Pytest">
  <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker">
  <img src="https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white" alt="GitHub Actions">
</p>

---

## 📌 Overview

PagePulse is a URL auditing API built with FastAPI. It analyzes a website URL and returns useful information about its HTTP response and page metadata.

The project demonstrates backend API development, request validation, error handling, automated testing, containerization, and continuous integration.

## ✨ Features

- 🔗 URL validation
- 🌐 HTTP status code detection
- 🔒 HTTPS availability checks
- ⏱️ Response-time measurement
- 🖥️ Server information retrieval
- 📄 Page title extraction
- 📏 Content-length reporting
- ⚡ Response caching
- 🛡️ Rate limiting and request logging
- ⚠️ Error handling
- 🐳 Docker support
- 🧪 Automated tests with Pytest
- 🔄 GitHub Actions CI workflow
- 📚 API documentation through FastAPI

## 🛠️ Technology Stack

| Category | Technologies |
|---|---|
| Language | Python |
| API Framework | FastAPI |
| HTTP Requests | Requests |
| HTML Parsing | BeautifulSoup4 |
| Testing | Pytest |
| Containerization | Docker |
| CI/CD | GitHub Actions |

## 📂 Project Structure

```text
PagePulse/
├── .github/
│   └── workflows/
├── app/
├── tests/
├── .dockerignore
├── Dockerfile
├── pytest.ini
├── requirements.txt
└── README.md
