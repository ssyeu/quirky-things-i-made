from pathlib import Path
import datetime
import readline
import os

token = os.environ["GITHUB_TOKEN"]


title = input("Note title: ").strip()
body = input("Notes: ")
now = datetime.datetime.now()
duplicate = 0

# Keep practice notes in a folder beside this script.
notes_folder = Path("/home/syeu/Documents/Obsidian Vault/obsidian/Notes/")
notes_folder.mkdir(exist_ok=True)

# Replace characters that can cause problems in filenames.
safe_title = "".join(
    "_" if character in '/\\:*?"<>|' else character
    for character in title
).strip(". ")

note_path = notes_folder / f"{safe_title or 'Untitled'}.md"

try:
    # "x" creates a new file and prevents overwriting an existing note.
    with note_path.open("x", encoding="utf-8") as note:
        note.write(f"{now.strftime('%Y-%m-%d %H:%M:%S')}\n\n{body}\n")
    print(f"Created: {note_path}")
except FileExistsError:
    # If a note with the same title already exists, append a number to the filename.
    while True:
        duplicate += 1
        note_path = notes_folder / f"{safe_title or 'Untitled'}_{duplicate}.md"
        
        try:
            with note_path.open("x", encoding="utf-8") as note:
                note.write(f"{now.strftime('%Y-%m-%d %H:%M:%S')}\n\n{body}\n")
            print(f"Created: {note_path}")

            break
        except FileExistsError:
            continue