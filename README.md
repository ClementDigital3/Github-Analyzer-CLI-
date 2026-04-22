![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![Status](https://img.shields.io/badge/Status-Active-success)
![License](https://img.shields.io/badge/License-MIT-green)
![GitHub](https://img.shields.io/badge/GitHub-CLI%20Project-black?logo=github)

# GitHub Analyzer CLI Tool

A clean and interactive Python command-line tool that fetches and analyzes GitHub user profiles using the GitHub API.

---

## 🚀 Features

- Fetch GitHub user profile data in real time
- Display name, bio, company, and profile details
- Show repository count, followers, and following
- Calculate a simple developer score
- Clean and colored terminal output
- Continuous search mode (no restart needed)

---

## 🛠️ Tech Stack

- Python 3
- Requests (HTTP requests)
- Colorama (terminal styling)
- GitHub REST API

---

## 📦 Installation

```bash
git clone git@github.com:ClementDigital3/Github-Analyzer-CLI.git
cd Github-Analyzer-CLI
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt