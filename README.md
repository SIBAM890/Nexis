# Nexis OS | Active Surveillance Console 👁️

> **"Intelligence is not just about data. It's about connection."**

Nexis OS is a next-generation **Open Source Intelligence (OSINT)** dashboard designed for ethical surveillance, risk assessment, and identity correlation. It features a real-time "Glassmorphism" UI, dynamic graph visualizations, and a robust "Ethics Guardian" protocol to ensure safety.

---

## ⚡ Key Features

*   **🕵️ Visual Intelligence Graph**: Interactive node-edge visualization of digital footprints using `vis.js`.
*   **🛡️ Ethics Guardian Protocol**:
    *   **Client-Side**: Instant regex blocking of private IPs, SSNs, and admin roots.
    *   **Server-Side**: Secondary validation layer to prevent misuse.
*   **⚠️ Risk Assessment Engine**: Quantitative scoring (0-100) based on exposure and signal severity.
*   **🔄 Reverse OSINT Gauge**: Analyzes how "indexable" a target is to external surveillance.
*   **🎯 Autonomous Correlations**: Logically links disparate data points (e.g., Username -> Email -> Domain).
*   **🔒 Privacy-First Architecture**: Ephemeral session storage. No persistent database of targets.

---

## 🚀 Quick Start (Local)

### Prerequisites
*   Python 3.9+
*   Git

### Installation
```bash
# 1. Clone the repository
git clone https://github.com/your-username/Nexis-OS.git
cd Nexis-OS

# 2. Create Virtual Environment (Optional but Recommended)
python -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# 3. Install Dependencies
pip install -r requirements.txt
```

### Running the Console
```bash
python run.py
```
> Access the Secure Terminal at: **http://localhost:5000**

---

## 📦 Deployment (Cloud)

Nexis OS is cloud-native and Docker-ready.

### 🐳 Docker
```bash
docker build -t nexis-os .
docker run -p 5000:5000 nexis-os
```

### 🚂 Railway / Render
1.  Push to GitHub.
2.  Connect repository to **Railway** or **Render**.
3.  The system automatically detects the `Dockerfile` and `render.yaml`.
4.  **Note**: The app automatically binds to the `$PORT` environment variable.

---

## 🛠️ Engineering Standards

*   **Reliability**: Enforces a strict synchronous render path to prevent UI deadlocks.
*   **Safety**: Wrapped in a global `try/catch` safety net to handle visualization failures gracefully.
*   **Modes**:
    *   `STABLE MODE` (Default): Optimized for speed and reliability.
    *   `VISUAL MODE`: Activates cosmetic pulse effects and transitions.

---

## ⚖️ Legal & Ethical Disclaimer

**EDUCATIONAL PURPOSE ONLY.**
Nexis OS is a demonstration of intelligence analysis capability. It uses **simulated data logic** combined with public API patterns. It must **NOT** be used for:
*   Unauthorized surveillance.
*   Targeting private infrastructure.
*   Harassment or doxxing.

*The "Ethics Guardian" module is active by default and cannot be disabled in standard operation.*
