# Project File Structure Structure

This document provides a detailed breakdown of the Nexis OS codebase, explaining the responsibility of each directory and key file.

## 📂 Root Directory
*   **`run.py`**: The application entry point. It initializes the Flask app, configures the port (dynamic for cloud/local), and starts the server.
*   **`requirements.txt`**: Lists all Python dependencies required to run the project (e.g., Flask, Gunicorn, Vis.js support).
*   **`README.md`**: The main landing page for the project, containing installation instructions, features, and disclaimers.
*   **`docs/`**: Contains architectural and operational documentation.
    *   `system_architecture.md`: Technical design diagrams and component breakdown.
    *   `workflow.md`: User journey and internal state logic flows.
    *   `file_structure.md`: (This file) Map of the codebase.

## 📂 app/ (Application Core)
This directory contains the source code for the backend and frontend logic.

### 📄 `app/__init__.py`
*   Initializes the Flask application factory.
*   Registers blueprints and routes.
*   Sets up configuration (e.g., secret keys, upload folders).

### 📄 `app/routes.py`
*   **API Gateway**: Defines the HTTP endpoints.
*   `GET /`: Serves the `dashboard.html` template.
*   `POST /scan`: Receives target input, triggers the `IntelligenceBrain`, and returns the JSON report.

### 📂 app/core/ (System Utilities)
*   **`ethics.py` (`EthicsGuardian`)**:
    *   The "Safety Layer". Contains `FORBIDDEN_PATTERNS` (Regex for IPs, SSNs).
    *   Validates all inputs *before* any processing occurs.
*   **`schema.py`**: Defines data models (e.g., `UnifiedSignal` class) to ensure consistent data structure across modules.

### 📂 app/agent/ (Orchestration)
*   **`brain.py` (`IntelligenceBrain`)**:
    *   The central controller class.
    *   Orchestrates the pipeline: `Ethics` -> `Scrape` -> `Correlate` -> `Risk` -> `Reverse OSINT` -> `Report`.

### 📂 app/scrapers/ (Data Collection)
*   **`social_scraper.py`**:
    *   Simulates the collection of public data fingerprints (OSINT).
    *   **Note**: Uses safe, simulated logic for demonstration to avoid violating real platform TOS during hackathons.

### 📂 app/intelligence/ (Analysis Engine)
*   **`correlator.py`**: Logic for linking disparate signals (e.g., matching a username to a domain).
*   **`risk.py` (`RiskAssessor`)**: Algorithms to calculate the 0-100 Threat Score based on signal severity.
*   **`reverse_osint.py`**: Analyzes the target's "Indexability" (how easily they can be found by others).

### 📂 app/templates/ (Frontend)
*   **`dashboard.html`**:
    *   The main Single-Page Application (SPA) interface.
    *   Contains the CSS ("Glassmorphism"), HTML structure, and the **Client-Side JavaScript controller**.
    *   Handles the `vis.js` graph rendering and UI state management (`READY`, `SCANNING`, `RESULTS`).
