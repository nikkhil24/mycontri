# auto_commit.py
import subprocess
from datetime import datetime
import os
import sys

# ==== CONFIGURATIONS (EDIT THESE) ====
COMMIT_MESSAGE = "chore: daily activity update"
BRANCH_NAME = "main"  # or "master" or whatever your branch is
FILE_NAME = "activity.log"
# =====================================

def run_cmd(cmd):
    """Run a shell command and print it."""
    print(f"$ {' '.join(cmd)}")
    result = subprocess.run(cmd, text=True)
    if result.returncode != 0:
        print("Command failed. Check the output above.")
        sys.exit(result.returncode)

def main():
    # 1) Check this is a git repo
    if not os.path.isdir(".git"):
        print("This folder is not a git repository (.git not found).")
        sys.exit(1)

    # 2) Append timestamp to the activity file
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"{now} - automated activity\n"

    with open(FILE_NAME, "a", encoding="utf-8") as f:
        f.write(line)

    print(f"Updated {FILE_NAME} with: {line.strip()}")

    # 3) Stage the file
    run_cmd(["git", "add", FILE_NAME])

    # 4) Commit
    run_cmd(["git", "commit", "-m", COMMIT_MESSAGE])

    # 5) Push to remote
    run_cmd(["git", "push", "origin", BRANCH_NAME])

    print("✅ Commit pushed successfully!")

if __name__ == "__main__":
    main()
