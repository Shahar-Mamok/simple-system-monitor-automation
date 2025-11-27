# System Monitoring and Log Scanning Tool

This Python utility provides a lightweight solution for monitoring system resources (CPU, Memory, Disk) and scanning log files for specific keywords. It automatically generates logs and alerts based on user-defined thresholds.

## Features

* **System Monitoring:** Continuously tracks CPU, Memory, and Disk usage.
* **Threshold Alerts:** Triggers alerts if CPU or Memory usage exceeds specified percentages.
* **Log Scanning:** Scans external log files for specific keywords (e.g., ERROR, WARN) and aggregates findings.
* **Automatic Logging:** Maintains organized logs for system status and alerts in a dedicated directory.

## Prerequisites

* Python 3.6 or higher
* `psutil` library

## Installation

1. Clone the repository or download the script.
2. Install the required dependency using pip:

   ```bash
   pip install psutil
