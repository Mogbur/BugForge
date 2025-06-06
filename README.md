# BugForge 🐛🛠️  
A simple and powerful CLI tool for logging bugs — designed for manual QA testers, indie devs, or anyone tired of dumping bugs into spreadsheets.
Think of BugForge like a pocket notebook for bugs — not a full management system like JIRA or Asana.

---

## 💡 Features

- Generates unique Bug IDs with timestamp
- Input validation for clean and complete bug reports
- Exports to `.txt`, `.csv`, and `.json`
- Supports attachments (screenshots, video links)
- CLI-friendly, portable, and has **zero dependencies**

---

## 🛠️ How to Use

Run in terminal or inside VSCode:

```bash
python BugForge.py


You’ll be prompted to enter:

Reporter name
Bug title
Severity (validated)
Platform/device
Expected vs. actual result
Reproduction steps
Optional attachments
File format output options (TXT, CSV, JSON)
All bug logs are saved locally with timestamp and structured formatting.

📁 Output Examples
bug_reports.txt – human-readable logs
bug_reports.csv – spreadsheet-friendly format
bug_reports.json – structured data for automation or analytics

⚙️ Coming Soon Ideas
CLI flags (--csv, --json, --silent)
Status update support (e.g. “Closed”, “In Progress”)
Config presets and reusable sessions
GUI wrapper for non-CLI users

👤 Author
🧑‍🔧 Made with 💻 and ☕ by HenriQA
📜 Licensed under the MIT License
