from datetime import date, timedelta
import argparse
import os
import platform

parser = argparse.ArgumentParser(description="Prints date and copy it to the clipboard on Windows.")
parser.add_argument("-f", "--format", choices=["iso", "au"], default="iso", help="Date format: iso (YYYY-MM-DD) or au (DD/MM/YYYY)")
args = parser.parse_args()

today = date.today() + timedelta(days=1)
date = today.isoformat() if args.format == "iso" else today.strftime("%d/%m/%Y")

if os.name == "nt" and platform.system() == "Windows":
    import pyperclip
    pyperclip.copy(date)

print(date)