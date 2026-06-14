from datetime import date
import argparse
import os
import platform

parser = argparse.ArgumentParser(description="Prints date and copy it to the clipboard on Windows.")
parser.add_argument("-f", "--format", choices=["iso", "au"], default="iso", help="The ISO format (YYYY-MM-DD) or Australian (au) format (DD/MM/YYYY)")
args = parser.parse_args()

today = date.today()
date = today.isoformat() if args.format == "iso" else today.strftime("%d/%m/%Y")

if os.name == "nt" and platform.system() == "Windows":
    import pyperclip
    pyperclip.copy(date)

print(date)