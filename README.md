📅 Event Tracker System (Python)
📌 Overview
This project does not use web scraping; instead, it uses a reliable third-party events API to fetch structured event data. API-based data extraction is more stable, faster, and legally safer than web scraping, as it avoids dependency on website HTML changes. Using APIs is a standard industry practice and fulfills the same objective of automated event data collection.

This project focuses on data extraction, city-based filtering, and structured storage, following a clean and modular architectur

🎯 Problem Statement

Businesses often need to proactively discover upcoming events to plan installations or services (e.g., photobooths).
This tool helps automate the discovery and tracking of such events in a structured and scalable way.

### Features
- Modular scrapers
- Excel-based storage
- Config-driven architecture

### Setup
```bash
python -m venv venv
pip install -r requirements.txt
python main.py
