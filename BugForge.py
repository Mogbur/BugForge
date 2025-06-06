import csv
import json
import os
import re
from datetime import datetime


def log_bug():
    def get_required_input(prompt):
        while True:
            value = input(prompt).strip()
            if value:
                return value
            print("This field is required. Please enter a value.")

    def get_severity():
        allowed = ["Low", "Medium", "High"]
        while True:
            value = input(
                "Enter severity (Low, Medium, High): ").strip().capitalize()
            if value in allowed:
                return value
            print("Please enter one of: Low, Medium, High.")

    def get_bug_type():
        allowed = ["UI", "LOGIC", "CRASH", "SECURITY", "PERFORMANCE", "OTHER"]
        while True:
            value = input(
                "Enter bug type (UI, Logic, Crash, Security, Performance, Other): ").strip().upper()
            if value in allowed:
                return value
            print("Please enter one of: UI, Logic, Crash, Security, Performance, Other.")

    def get_reproducibility():
        allowed = ["Always", "Sometimes", "Rarely", "Unable to reproduce"]
        while True:
            value = input(
                "Enter reproducibility (Always, Sometimes, Rarely, Unable to reproduce): ").strip().capitalize()
            # Special case for "Unable to reproduce"
            if value == "Unable to reproduce":
                return value
            if value in allowed:
                return value
            print("Please enter one of: Always, Sometimes, Rarely, Unable to reproduce.")

    # Ask user for base filename (without extension)
    base_filename = input(
        "Enter a base name for your bug report file (no extension). Leave blank to use 'bug_reports' (all bugs will go into the same file): "
    ).strip()
    if not base_filename:
        base_filename = "bug_reports"
    # Only allow safe characters
    base_filename = re.sub(r'[^a-zA-Z0-9_\-]', '_', base_filename)

    # Ask if user wants CSV and JSON versions
    save_csv = input("Also save as CSV? (y/n): ").strip().lower() == "y"
    save_json = input("Also save as JSON? (y/n): ").strip().lower() == "y"

    bug_id = datetime.now().strftime("%Y%m%d%H%M%S")  # Simple unique ID
    reporter = get_required_input("Enter your name or email: ")
    title = get_required_input("Enter bug title: ")
    severity = get_severity()
    bug_type = get_bug_type()
    reproducibility = get_reproducibility()
    platform = get_required_input(
        "Enter platform/device (e.g., Windows 10, iPhone 13): ")
    expected = get_required_input("Enter expected result: ")
    actual = get_required_input("Enter actual result: ")
    attachments = input(
        "Enter attachment file paths (screenshots/videos, comma-separated, optional): ")
    status = "Open"
    print("Enter steps to reproduce (type 'END' on a new line to finish):")
    steps_lines = []
    while True:
        line = input()
        if line.strip().upper() == "END":
            break
        steps_lines.append(line)
    steps = "\n".join(steps_lines)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # TXT format
    bug_report_txt = f"""
Bug ID: {bug_id}
Timestamp: {timestamp}
Reporter: {reporter}
Bug Title: {title}
Bug Type: {bug_type}
Severity: {severity}
Reproducibility: {reproducibility}
Platform/Device: {platform}
Expected Result: {expected}
Actual Result: {actual}
Status: {status}
Attachments: {attachments}
Steps to Reproduce:
{steps}
-------------------------------
"""
    try:
        with open(f"{base_filename}.txt", "a", encoding="utf-8") as file:
            file.write(bug_report_txt)
    except Exception as e:
        print(f"Error writing to TXT file: {e}")

    # CSV format
    if save_csv:
        csv_file = f"{base_filename}.csv"
        file_exists = os.path.isfile(csv_file)
        try:
            with open(csv_file, "a", newline='', encoding="utf-8") as file:
                writer = csv.writer(file)
                if not file_exists:
                    writer.writerow([
                        "Bug ID", "Timestamp", "Reporter", "Bug Title", "Bug Type", "Severity",
                        "Reproducibility", "Platform/Device", "Expected Result", "Actual Result", "Status", "Attachments", "Steps to Reproduce"
                    ])
                writer.writerow([
                    bug_id, timestamp, reporter, title, bug_type, severity,
                    reproducibility, platform, expected, actual, status, attachments, " | ".join(
                        steps_lines)
                ])
        except Exception as e:
            print(f"Error writing to CSV file: {e}")

    # JSON format
    if save_json:
        json_file = f"{base_filename}.json"
        try:
            if os.path.isfile(json_file):
                with open(json_file, "r", encoding="utf-8") as file:
                    bugs = json.load(file)
            else:
                bugs = []
            bugs.append({
                "bug_id": bug_id,
                "timestamp": timestamp,
                "reporter": reporter,
                "title": title,
                "bug_type": bug_type,
                "severity": severity,
                "reproducibility": reproducibility,
                "platform": platform,
                "expected": expected,
                "actual": actual,
                "status": status,
                "attachments": [a.strip() for a in attachments.split(",") if a.strip()],
                "steps": steps_lines
            })
            with open(json_file, "w", encoding="utf-8") as file:
                json.dump(bugs, file, indent=4)
        except Exception as e:
            print(f"Error writing to JSON file: {e}")

    print("Bug logged successfully!")
    print("\nBug summary:")
    print(bug_report_txt)


log_bug()
