System Monitoring and Log Scanning Tool
This Python utility provides a lightweight solution for monitoring system resources (CPU, Memory, Disk) and scanning log files for specific keywords. It automatically generates logs and alerts based on user-defined thresholds.

Features
System Monitoring: Continuously tracks CPU, Memory, and Disk usage.

Threshold Alerts: triggers alerts if CPU or Memory usage exceeds specified percentages.

Log Scanning: Scans external log files for specific keywords (e.g., ERROR, WARN) and aggregates findings.

Automatic Logging: Maintains organized logs for system status and alerts in a dedicated directory.

Prerequisites
Python 3.6 or higher

psutil library

Installation
Clone the repository or download the script.

Install the required dependency using pip:

Bash

pip install psutil
Or, if you have a requirements.txt file:

Bash

pip install -r requirements.txt
Usage
Run the script from the command line using one of the two available modes: monitor or scan-log.

1. Monitor System Resources
This command starts an infinite loop that checks system health at a set interval.

Basic Usage:

Bash

python main.py monitor
Custom Configuration:

You can customize the check interval and alert thresholds using flags.

Bash

python main.py monitor --interval 10 --cpu-threshold 90 --mem-threshold 85
Arguments:

--interval: Time in seconds between checks (default: 5).

--cpu-threshold: CPU usage percentage to trigger an alert (default: 80.0).

--mem-threshold: Memory usage percentage to trigger an alert (default: 80.0).

To stop the monitoring process, press Ctrl+C.

2. Scan Log Files
This command scans a specific text file for keywords and saves matching lines to the alert log.

Basic Usage:

Bash

python main.py scan-log /path/to/logfile.txt
Custom Keywords:

By default, it searches for "ERROR", "CRITICAL", and "WARN". You can specify your own keywords.

Bash

python main.py scan-log app.log --keywords "fail" "timeout" "exception"
Arguments:

file: The path to the log file you wish to scan.

--keywords: A list of keywords to search for (case-insensitive).

Output Files
The script automatically creates a logs/ directory in the same location as the script containing:

logs/system_status.log: Records the timestamped CPU, Memory, and Disk usage for every interval check.

logs/alerts.log: Records specific alerts when thresholds are crossed or when keywords are found during a file scan.
