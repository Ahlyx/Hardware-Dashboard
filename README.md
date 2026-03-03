# Hardware Dashboard

A hardware monitoring tool built in Python while studying for CompTIA A+ Core 1.
Available as both a CLI tool and a web dashboard with live refresh.

## Features
- System overview (OS, architecture, hostname)
- CPU usage, core count, and clock speed
- RAM and swap memory usage
- Disk partitions, storage usage, and I/O stats
- Network interfaces, IP addresses, and traffic

## CompTIA A+ Concepts Covered
- CPU architecture and hyperthreading
- RAM types and memory management
- Storage devices and file systems
- Networking and IP addressing
- Binary storage measurement (bytes to GB conversion)

## Requirements
- Python 3.8+
- psutil
- rich
- fastapi
- uvicorn

## Installation
1. Clone the repository
2. Install dependencies with `pip install -r requirements.txt`

## Usage

### CLI Version
Run with:
```
python cli.py
```
Select a section from the menu using numbers 1-5.
Press Ctrl+C on any live section to return to the menu.
Press 6 to exit.

### Web Dashboard
1. Start the API server:
```
uvicorn api:app --reload
```
2. Open `static/index.html` in your browser
3. The dashboard will auto refresh every 2 seconds

## Screenshots
<img width="1872" height="919" alt="s2" src="https://github.com/user-attachments/assets/1da1823a-aa77-4bcc-b70d-b1c7f6db05b1" />
<img width="1886" height="909" alt="s1" src="https://github.com/user-attachments/assets/30433e42-e295-4ca2-875c-9696e7f7f39a" />

<img width="679" height="485" alt="CLI Menu" src="https://github.com/user-attachments/assets/a27cfc75-1f35-4fc1-bf8e-a552a55564e3" />
<img width="833" height="572" alt="CLI Disk Output" src="https://github.com/user-attachments/assets/67814862-2427-4232-826e-a67164fa01c9" />
