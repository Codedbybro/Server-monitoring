# Server Monitor

A small Python CLI for checking resource usage and basic network availability on a Linux host. Built as a hands-on Linux, Python, and monitoring practice project.

## Features
- CPU, RAM, and root-filesystem usage via psutil
- Uptime
- Internet connectivity check (TCP connection to 8.8.8.8:53)
- TCP checks for selected ports on 127.0.0.1
- Combined OK / WARNING / CRITICAL status

## Requirements
- Python 3.10+
- Linux is the intended environment
- psutil (installed from requirements.txt)

## Run locally
1. Clone this repository and enter its directory.
2. Create a virtual environment: python3 -m venv .venv
3. Activate it: source .venv/bin/activate
4. Install dependencies: python -m pip install -r requirements.txt
5. Run: python monitor.py

The port checks currently target localhost and the ports are configured in monitor.py. They indicate whether a service accepts a TCP connection; they do not verify application-level health.

## Tests
Run: python -m unittest discover -s tests -v

Unit tests cover status thresholds and aggregation. GitHub Actions runs Python compilation and these tests on pushes and pull requests.

## Project layout
- .github/workflows/ci.yml — CI workflow
- monitor.py — CLI implementation
- requirements.txt — runtime dependencies
- tests/test_monitor.py — unit tests

## Current limitations / next steps
This is an educational CLI, not a production monitoring stack. It currently performs a one-shot report and has no alert delivery, persistent metrics, remote-host configuration, or dashboard. Useful next steps are configurable thresholds and targets, structured output, and alerting.

## What this project demonstrates
Python scripting, Linux resource inspection, TCP connectivity checks, dependency isolation with venv, unit testing, and basic CI with GitHub Actions.