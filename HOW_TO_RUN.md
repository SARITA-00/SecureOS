# SecureCloudOS v2 — How to Run & Demo Guide

## ── Step 1: Install Dependencies ──────────────────────────────────────────────
Open terminal inside the SecureOS_v2 folder and run:

```bash
pip install -r requirements.txt
```

## ── Step 2: Launch the Dashboard ─────────────────────────────────────────────

```bash
cd SecureOS_v2
python -m streamlit run dashboard/app.py
```

Your browser will open automatically at: http://localhost:8501

---

## ── Demo Script (What to Show the Evaluator) ─────────────────────────────────

### 1. Dashboard Page
- Point out the **4 metric cards**: CPU, Memory, Disk, Alerts
- Show the **time-series chart** of CPU & Memory over time
- Show the **disk gauge**
- Explain: "We collect real-time data using psutil every time the dashboard refreshes"

### 2. Security Alerts Page
- Show the "ML Engine" status badge at the top
- Explain: "We use **Isolation Forest** — an unsupervised ML algorithm — to detect
  anomalous processes. It learns what normal CPU+Memory patterns look like,
  and flags anything that deviates significantly."
- Show the alert history table and pie chart
- Key phrase: "Unlike simple threshold rules, our system adapts to each machine's
  normal baseline — so a process using 60% CPU on a busy server is NOT flagged,
  but the same process on an idle server WOULD be."

### 3. Process Manager Page
- Show the live process table sorted by CPU usage
- Show the **Kill Process** button — demonstrate it with a test PID
- Show the **per-process history graph** — select any process to see its
  CPU/memory trend over time

### 4. AI & Prediction Page
- Explain both AI models clearly:
  - Linear Regression → predicts future memory load
  - Isolation Forest → detects anomalous system states
- Show the CPU vs Memory scatter plot
- Key phrase: "We use two ML models: one for prediction, one for anomaly detection.
  These work together with our Docker manager to proactively reduce load."

### 5. Container Manager Page
- If Docker is running: show live containers, demonstrate Stop button
- Show auto-management: "When CPU > 80%, the system automatically stops a
  container to free resources. When CPU < 30%, it starts one."

### 6. CPU Scheduling Simulator Page ← MOST IMPRESSIVE FOR OS COURSE
- Enter some burst times, change the quantum, hit Enter
- Point at the **comparison table**: show which algorithm has lower wait time
- Show the **Gantt chart** for Round Robin
- Key phrase: "This directly simulates core OS scheduling — FCFS, Round Robin,
  and Priority Scheduling — and lets us compare their performance metrics
  like average waiting time and turnaround time in real time."

---

## ── Project Structure ──────────────────────────────────────────────────────────

```
SecureOS_v2/
├── main.py                    ← Orchestrates all modules
├── requirements.txt
├── monitoring/
│   └── monitor.py             ← CPU, Memory, Disk, Network, Processes
├── security/
│   ├── analyser.py            ← Isolation Forest anomaly detection ⭐
│   ├── detector.py            ← Process data collector
│   └── logger.py              ← Alert logging (JSON + txt)
├── ai_engine/
│   └── predictor.py           ← Linear Regression + System Isolation Forest
├── docker_manager/
│   └── docker_ops.py          ← Container start/stop/auto-manage
├── dashboard/
│   └── app.py                 ← Full Streamlit UI (6 pages) ⭐
└── data/
    ├── cpu_data.csv           ← Historical CPU/Memory log
    ├── alerts.json            ← Alert history
    ├── process_history.json   ← Per-process resource history
    └── logs.txt               ← Plain text alert log
```

---

## ── Common Questions Evaluators Ask ──────────────────────────────────────────

**Q: Why Isolation Forest?**
A: It's an unsupervised algorithm — it doesn't need labeled "attack" data.
   It learns the normal distribution of process behavior and isolates points
   that require fewer random cuts to separate — which is the anomaly.

**Q: What does the AI actually do?**
A: Two things. The Isolation Forest in security/analyser.py scores every
   running process and flags outliers. The predictor.py Isolation Forest
   monitors overall system state. The Linear Regression predicts memory load
   so the Docker manager can act *before* the system gets overloaded.

**Q: Is this a real OS or simulation?**
A: It's an OS management layer — like a lightweight version of what cloud
   providers use. We sit on top of Linux and manage real processes and
   real Docker containers using actual system calls via psutil and subprocess.
