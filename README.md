# BugForge 🐛🛠️  
A simple and powerful CLI tool for logging bugs — designed for manual QA testers, indie devs, or anyone tired of dumping bugs into spreadsheets.  
Think of BugForge like a pocket notebook for bugs — not a full management system like JIRA or Asana.

---

## 💡 Features

- ✅ Generates unique Bug IDs with timestamps
- ✅ Input validation for clean and complete bug reports
- ✅ Includes severity, bug type, reproducibility, attachments, and platform
- ✅ Exports to `.txt`, `.csv`, and `.json`
- ✅ Saves to a shared file or custom-named file per session
- ✅ CLI-friendly, portable, and zero dependencies (just Python)
- ✅ Supports structured bug steps and attachments
- ✅ Prints bug summary at the end

---

## 🛠️ How to Use

Run in terminal or inside VSCode:

```bash
python BugForge.py
```
You’ll be prompted to enter:

Reporter name or email

Bug title

Severity (Low, Medium, High)

Bug type (UI, Logic, Crash, Security, Performance, Other)

Reproducibility (Always, Sometimes, Rarely, Unable to reproduce)

Platform/Device (e.g., Windows 10, iPhone 13)

Expected vs. actual result

Optional attachment file names or URLs

Steps to reproduce

Output file format (TXT, CSV, JSON)


📁 Output Examples

bug_reports.txt – readable format for humans

bug_reports.csv – spreadsheet-friendly

bug_reports.json – structured for automation and tools

⚙️ Potential Future Additions

--csv, --json, --silent CLI flags

Status editing (e.g. "Closed", "In Progress")

Editable JSON log parser

Config presets and reusable session profiles

GUI wrapper for non-CLI users

👤 Author
🧑‍🔧 Made with 💻 and ☕ by HenriQA
📜 Licensed under the MIT License

BugForge is best suited for solo testers, small QA teams, or indie developers who need a fast, simple way to log bugs without full-scale tools like JIRA or Asana.
