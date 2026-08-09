Three python scripts that simply print the corresponding date and copies it to clipboard.

Please see the Justfile for build instructions.

```
uv run python ./src/today.py --help
usage: today.py [-h] [-f {iso,au}]

Prints date and copy it to the clipboard on Windows.

options:
  -h, --help            show this help message and exit
  -f, --format {iso,au}
                        The ISO format (YYYY-MM-DD) or Australian (au) format (DD/MM/YYYY)
```