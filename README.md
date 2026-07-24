# 🚀 Page Pulse API

A production-ready URL Audit Service built with **FastAPI**.

The API analyzes any website URL and returns useful metadata such as:

- HTTP Status Code
- HTTPS Availability
- Response Time
- Server Information
- Page Title
- Content Length

---

## Features

- FastAPI REST API
- URL Validation
- Response Caching
- Request Logging
- Rate Limiting
- Error Handling
- Docker Support
- GitHub Actions CI
- Swagger Documentation
- Unit Tests

---

## Tech Stack

- Python 3.12
- FastAPI
- Uvicorn
- Requests
- BeautifulSoup4
- Pytest
- SlowAPI
- Docker
- GitHub Actions

---

## Installation

Clone the repository

```bash
git clone https://github.com/yourusername/PagePulse.git
```

Move into the project

```bash
cd PagePulse
```

Create Virtual Environment

```bash
python -m venv venv
```

Activate

Windows

```bash
venv\Scripts\activate
```

Linux / Mac

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run server

```bash
uvicorn app.main:app --reload
```

---

## API Documentation

Swagger UI

```
http://127.0.0.1:8000/docs
```

---

## Example Request

POST

```
/audit
```

Body

```json
{
    "url":"https://example.com"
}
```

Example Response

```json
{
  "success": true,
  "data": {
    "url": "https://example.com",
    "status_code": 200,
    "https": true,
    "response_time_ms": 123.45,
    "title": "Example Domain",
    "server": "cloudflare",
    "content_length": 559,
    "cached": false
  }
}
```

---

## Running Tests

```bash
python -m pytest
```

---

## Docker

Build

```bash
docker build -t pagepulse .
```

Run

```bash
docker run -p 8000:8000 pagepulse
```

---

## Project Structure

```
PagePulse/
│
├── app/
│   ├── main.py
│   ├── routes.py
│   ├── models.py
│   ├── audit.py
│   ├── cache.py
│   ├── limiter.py
│   ├── logger.py
│   ├── config.py
│   ├── responses.py
│   ├── exceptions.py
│   └── utils.py
│
├── tests/
├── .github/workflows/
├── Dockerfile
├── requirements.txt
├── pytest.ini
└── README.md
```

---

## Author

Shrikant Pawar