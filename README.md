# 📊 Pulse Infographics

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=4f46e5&height=180&section=header&text=Pulse%20Infographics&fontSize=56&fontColor=ffffff&fontAlignY=38&animation=fadeIn" width="100%"/>

<br/>

[![Typing SVG](https://readme-typing-svg.demolab.com?font=DM+Mono&size=18&duration=3000&pause=1000&color=4F46E5&center=true&vCenter=true&multiline=true&repeat=true&width=600&height=80&lines=Multi-framework+data+unification;Single+visual+interface;Distributed+micro-module+architecture)](https://github.com/Joeljozzz/Pulse_Infographics)

<br/>

[![GitHub Repo](https://img.shields.io/badge/GitHub-Repo-0B0D0E?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Joeljozzz/Pulse_Infographics)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)
[![Built by Joel](https://img.shields.io/badge/Built%20by-Joel%20Jose-4f46e5?style=for-the-badge)](https://github.com/Joeljozzz)

<br/>

### 🛠️ Tech Stack Badges

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)](https://reactjs.org/)
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
[![PHP](https://img.shields.io/badge/PHP-777BB4?style=for-the-badge&logo=php&logoColor=white)](https://www.php.net/)
[![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)](https://www.sqlite.org/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white)](https://getbootstrap.com/)

</div>

---

## 📌 Project Overview

**Pulse Infographics** is a multi-framework data visualization platform that unifies live data streams from finance, bioinformatics, weather, news, and personal analytics into a single visual dashboard. Built with a distributed multi-server architecture, each micro-module independently ingests, processes, and displays real-time metrics across varied domains. Developed as a comprehensive final year Information Technology project, it breaks down data silos through modular visualization services.

---

## ✨ Features

- 🪙 **Pulse-Cryptograph**: Real-time cryptocurrency valuation against USD with interactive time-series historical charts.
- 📈 **Pulse-Stock-graph**: Dynamic stock market tracker visualizing opening, closing, and volume movements.
- 🧬 **Pulse-DNA-analyser**: Bioinformatics utility computing nucleotide composition counts and sequence frequency metrics.
- 🌦️ **Pulse-Weather**: City-level weather query engine displaying meteorological metrics and dynamic status symbology.
- 📰 **Pulse-News**: Automated news feed aggregator fetching real-time headlines from external media sources.
- 🧭 **Pulse-Advisor**: Geolocation-aware travel guide recommending nearby points of interest and landmarks.
- 💳 **Pulse-Expense-Tracker**: Personal finance manager featuring speech-to-text input, transaction categorization, and dynamic doughnut chart breakdowns.
- 🧩 **Multi-Framework Architecture**: Modular composition orchestrating Streamlit, Flask, React, and PHP sub-servers behind a coordinated interface.

---

## 🏛️ System Architecture

```text
┌────────────────────────────────────────────────────────────────────────┐
│  LAYER 1 — Ingestion        [Remote API Servers & Data Feeds]          │
│  Live metrics extraction via REST APIs, Geo-services & Web Requests    │
├────────────────────────────────────────────────────────────────────────┤
│  LAYER 2 — Processing       [Independent Sub-Servers]                 │
│  Data standardization and analysis using Flask, PHP, and Streamlit     │
├────────────────────────────────────────────────────────────────────────┤
│  LAYER 3 — Presentation     [Unified Visual Interface]                 │
│  Multi-framework dashboard rendering responsive graphical outputs      │
└────────────────────────────────────────────────────────────────────────┘
```

### Module Breakdown

| Module | Core Framework | Data Domain | Primary Function |
|---|---|---|---|
| **Pulse-Cryptograph** | PHP / Chart.js | Fintech / Crypto | Live exchange rates vs. USD with adjustable interval graphing |
| **Pulse-Stock-graph** | Python Streamlit | Financial Markets | Stock candlestick / line charts and historical trend views |
| **Pulse-DNA-analyser** | Python Streamlit | Bioinformatics | Nucleotide frequency calculation and sequence statistics |
| **Pulse-Weather** | Python Flask / REST APIs | Meteorology | Real-time weather parameters and condition indicators |
| **Pulse-News** | Python Flask | Media & Journalism | Curated topical headline streams from remote news APIs |
| **Pulse-Advisor** | React / Geolocation API | Travel & Tourism | Location-based interactive mapping of local attractions |
| **Pulse-Expense-Tracker** | React / Speech API / Charts | Personal Finance | Income/expense ledger with speech recognition & chart analytics |

---

## 📂 Project Structure

```text
Pulse_Infographics/
├── .git/                  # Git version control metadata
├── LICENSE                # MIT License
└── README.md              # Project documentation and architectural overview
```

### Distributed Architecture Ecosystem

```text
Pulse-Infographics-Ecosystem/
├── landing-site/          # Central portal & review system (PHP / Bootstrap)
├── pulse-cryptograph/     # Cryptocurrency visualization module (PHP / REST APIs)
├── pulse-stock-graph/     # Equity trends & stock chart visualizer (Streamlit / Python)
├── pulse-dna-analyser/    # Bioinformatics nucleotide analyzer (Streamlit)
├── pulse-weather/         # City-based weather service (Flask / OpenWeatherMap)
├── pulse-news/            # Live headline news aggregation service (Flask)
├── pulse-advisor/         # Geolocation travel recommendations (React)
└── pulse-expense-tracker/ # Voice-enabled income & expense tracker (React)
```

---

## 🚀 Getting Started

### Prerequisites

To run modules across the Pulse Infographics ecosystem, ensure you have the following installed:

- **Python**: `3.8+`
- **Node.js**: `16.x+` & `npm`
- **PHP**: `8.0+`
- **Web Server**: Apache / Nginx (or PHP built-in server)
- **SQLite3**

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Joeljozzz/Pulse_Infographics.git
   cd Pulse_Infographics
   ```

2. **Python Sub-Servers (Flask & Streamlit):**
   ```bash
   # Create and activate a virtual environment
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

   # Install common dependencies
   pip install flask streamlit pandas requests matplotlib
   ```

3. **React Sub-Servers:**
   ```bash
   npm install
   ```

---

## 💻 Usage

Each sub-system operates as an independent micro-service that can be executed based on the required module:

- **Run Streamlit Applications (Stock Graph & DNA Analyser):**
  ```bash
  streamlit run app.py
  ```

- **Run Flask Applications (Weather & News APIs):**
  ```bash
  python app.py
  ```

- **Run React Applications (Expense Tracker & Advisor):**
  ```bash
  npm start
  ```

- **Run PHP Landing Site & Cryptograph:**
  ```bash
  php -S localhost:8000
  ```

Access the unified portal or individual service endpoints via your web browser at their assigned localhost ports.

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

<div align="center">

<br/>

[![Typing SVG](https://readme-typing-svg.demolab.com?font=DM+Mono&size=13&duration=4000&pause=1000&color=6B7280&center=true&vCenter=true&repeat=true&width=500&lines=Designed+and+built+with+care+by+Joel+Jose;Data+Science+%7C+ML+%7C+Cloud;github.com%2FJoeljozzz)](https://github.com/Joeljozzz)

<br/>

<img src="https://capsule-render.vercel.app/api?type=waving&color=4f46e5&height=100&section=footer&animation=fadeIn" width="100%"/>

</div>
