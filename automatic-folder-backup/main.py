from pathlib import Path
from datetime import date
import shutil
import schedule
import time

SOURCE_DIR = Path(r"C:\Users\sayam\Pictures\Screenshots")
BACKUP_DIR = Path(r"C:\Users\sayam\Desktop\Backups")


def create_backup():
    today = date.today().isoformat()
    destination = BACKUP_DIR / today

    try:
        # Make sure the backup directory exists
        BACKUP_DIR.mkdir(parents=True, exist_ok=True)

        # Don't overwrite an existing backup
        if destination.exists():
            print(f"Backup already exists: {destination}")
            return

        shutil.copytree(SOURCE_DIR, destination)
        print(f"Backup completed successfully: {destination}")
    except FileNotFoundError:
        print(f"Source folder not found: {SOURCE_DIR}")
    except PermissionError:
        print("Permission denied. Check your folder permissions.")
    except OSError as error:
        print(f"Backup failed: {error}")


# Run the backup every day at 18:00
schedule.every().day.at("18:00").do(create_backup)
print("Backup scheduler started.")
print("Daily backup time: 18:00")

while True:
    schedule.run_pending()
    time.sleep(30)
