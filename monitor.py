import argparse
import datetime
import time
from pathlib import Path
from typing import List

import psutil  # make sure psutil is installed


LOGS_DIR = Path("logs")
LOGS_DIR.mkdir(exist_ok=True)

SYSTEM_LOG = LOGS_DIR / "system_status.log"
ALERTS_LOG = LOGS_DIR / "alerts.log"


def log(msg: str, file_path: Path) -> None:
    """Append a timestamped message to a log file."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with file_path.open("a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {msg}\n")


def monitor_system(interval: int, cpu_threshold: float, mem_threshold: float) -> None:
    """
    Monitor CPU and memory usage every `interval` seconds.
    If usage exceeds threshold --> write alert to alerts.log.
    """
    print(f"Starting system monitor (interval={interval}s)... Press Ctrl+C to stop.")
    try:
        while True:
            cpu = psutil.cpu_percent(interval=None)
            mem = psutil.virtual_memory().percent
            disk = psutil.disk_usage("C:\\").percent  # main disk on Windows

            status_msg = f"CPU={cpu:.1f}%, MEM={mem:.1f}%, DISK={disk:.1f}%"
            log(status_msg, SYSTEM_LOG)
            print(status_msg)

            alerts = []
            if cpu > cpu_threshold:
                alerts.append(f"High CPU usage: {cpu:.1f}% > {cpu_threshold}%")
            if mem > mem_threshold:
                alerts.append(f"High memory usage: {mem:.1f}% > {mem_threshold}%")

            for a in alerts:
                log(f"ALERT: {a}", ALERTS_LOG)
                print(f"[ALERT] {a}")

            time.sleep(interval)
    except KeyboardInterrupt:
        print("\nMonitoring stopped by user.")


def scan_log_file(input_path: str, keywords: List[str]) -> None:
    """
    Scan a log file and copy lines containing any of the given keywords
    into alerts.log.
    """
    input_file = Path(input_path)
    if not input_file.exists():
        print(f"Log file not found: {input_path}")
        return

    found = 0
    with input_file.open("r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            if any(kw.lower() in line.lower() for kw in keywords):
                log(f"LOG ALERT from {input_file}: {line.strip()}", ALERTS_LOG)
                found += 1

    print(f"Scan finished. Found {found} matching lines.")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Simple system monitoring & log scanning automation tool."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # monitor command
    monitor_parser = subparsers.add_parser("monitor", help="Monitor system resources.")
    monitor_parser.add_argument(
        "--interval", type=int, default=5, help="Interval in seconds between checks."
    )
    monitor_parser.add_argument(
        "--cpu-threshold",
        type=float,
        default=80.0,
        help="CPU percent threshold for alerts.",
    )
    monitor_parser.add_argument(
        "--mem-threshold",
        type=float,
        default=80.0,
        help="Memory percent threshold for alerts.",
    )

    # scan-log command
    scan_parser = subparsers.add_parser(
        "scan-log", help="Scan a log file for error keywords."
    )
    scan_parser.add_argument("file", help="Path to the log file to scan.")
    scan_parser.add_argument(
        "--keywords",
        nargs="+",
        default=["ERROR", "CRITICAL", "WARN"],
        help="Keywords to search for in the log file.",
    )

    args = parser.parse_args()

    if args.command == "monitor":
        monitor_system(args.interval, args.cpu_threshold, args.mem_threshold)
    elif args.command == "scan-log":
        scan_log_file(args.file, args.keywords)


if __name__ == "__main__":
    main()
