# 🤖 Local AI Agent (Email Automation Assistant)

A lightweight **local AI agent** that monitors your inbox, summarizes new emails using a local LLM, and notifies you about important messages — all running **fully offline** using Ollama.

---

## 🚀 Features

* 📩 Fetch unread emails via IMAP
* 🧠 AI-powered email summarization (local LLM)
* 🔔 Desktop notifications for important emails
* ⏱️ Automated background execution (scheduler)
* 🔒 Privacy-first (no external APIs required)

---

## 🏗️ Tech Stack

* **Python 3.12+**
* **IMAPClient** – Email fetching
* **email (stdlib)** – Email parsing
* **Ollama** – Local LLM runtime
* **Qwen / LLaMA models** – AI processing
* **schedule** – Task automation
* **requests** – API communication

---

## 📂 Project Structure

```
ai-agent/
│
├── agent.py          # AI logic + decision making
├── email_tool.py     # Email fetching + parsing
├── main.py           # Scheduler + entry point
├── venv/             # Virtual environment
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/ai-agent.git
cd ai-agent
```

---

### 2️⃣ Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install imapclient schedule requests
```

---

### 4️⃣ Install Ollama (Local AI)

Install Ollama:

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

Run model:

```bash
ollama run qwen3.5:4b
```

---

### 5️⃣ Configure Email Credentials

Edit `email_tool.py`:

```python
USERNAME = "your_email@gmail.com"
PASSWORD = "your_app_password"
```

> ⚠️ Use **Gmail App Password**, not your actual password.

---

## ▶️ Run the Agent

```bash
python main.py
```

---

## 🔁 Auto Start on PC Boot (Linux)

To start the agent automatically whenever your PC turns on, create a `systemd` user service.

### 1️⃣ Create Service File

```bash
mkdir -p ~/.config/systemd/user

cat > ~/.config/systemd/user/ai-agent.service << 'EOF'
[Unit]
Description=Local AI Email Agent
After=network-online.target
Wants=network-online.target

[Service]
Type=simple
WorkingDirectory=/home/manish/Documents/project/ai-agent
ExecStart=/home/manish/Documents/project/ai-agent/venv/bin/python /home/manish/Documents/project/ai-agent/main.py
Restart=always
RestartSec=5
Environment=PYTHONUNBUFFERED=1

[Install]
WantedBy=default.target
EOF
```

### 2️⃣ Enable and Start the Service

```bash
systemctl --user daemon-reload
systemctl --user enable --now ai-agent.service
```

### 3️⃣ Keep It Running After Reboot (Without Login)

```bash
sudo loginctl enable-linger manish
```

### 4️⃣ Make Sure Ollama Also Starts on Boot

```bash
sudo systemctl enable --now ollama
```

### 5️⃣ Check Service Status and Logs

```bash
systemctl --user status ai-agent.service
journalctl --user -u ai-agent.service -f
```

---

## 🔄 How It Works

1. Scheduler triggers the agent every X minutes
2. Agent fetches unread emails
3. Emails are sent to local LLM (Qwen via Ollama)
4. AI summarizes and identifies important messages
5. System sends notification if needed

---

## 🧠 Example Output

```
AI Agent Started...
Running agent...

=== AI RESPONSE ===
You have 2 important emails:
- Interview invitation from XYZ
- Deadline reminder from college
```

---

## ⚡ Customization

You can easily extend this agent:

* ✅ Auto-reply to emails
* ✅ Filter job/internship emails
* ✅ Save logs to JSON/database
* ✅ Connect with React dashboard
* ✅ Add more tools (WhatsApp, GitHub, Fiverr alerts)

---

## 🛠️ Known Issues

* Requires IMAP enabled in email provider
* Gmail requires App Password
* Ollama must be running locally

---

## 📌 Future Improvements

* Multi-tool agent system
* Voice assistant (Jarvis-style)
* Web dashboard (React + API)
* Smart email classification (ML-based)

---

## 👨‍💻 Author

**Manish Suthar**

* GitHub: https://github.com/Sutharmanish09
* Portfolio: https://bento.me/manishsuthar
* LinkedIn: https://www.linkedin.com/in/manish-suthar-dev

---

## ⭐ Contributing

Pull requests are welcome! For major changes, please open an issue first.

---

## 📄 License

This project is open-source and available under the MIT License.

---

## 💡 Inspiration

This project is a step toward building a **personal AI assistant (Jarvis)** that runs locally and automates daily digital tasks.

---
