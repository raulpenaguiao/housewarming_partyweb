# Housewarming Party Website Creator

A simple web application to create and host your housewarming party website.

## Quick Start

1. Clone the repository
```bash
git clone [repository-url]
```

2. Add private information

Create a file named `private_info.json` in the root directory with the following structure:
```private_info.json
{
    "address": "Your address",
    "transport": "<strong>transport options</strong><br> STOP: station",
    "time": "day<br>STARTS time"
}
```

3. Run the server
```bash
python3 server.py
```

The website will be available at `http://127.0.0.1:5000` (or the configured port).

## Description

This tool helps you create a personalized website for your housewarming party. Share details, directions, and manage RSVPs easily.

## Requirements
- Python 3.x
- Flask