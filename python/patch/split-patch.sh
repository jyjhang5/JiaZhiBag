# This script splits the big.patch file into multiple patch files based on each "diff --git" section,
# and saves each split patch into the split_patches directory with filenames like part_XXXX.patch.
import os

with open("big.patch", "r") as f:
    lines = f.readlines()

chunks = []
current = []
for line in lines:
    if line.startswith("diff --git"):
        if current:
            chunks.append(current)
        current = [line]
    else:
        current.append(line)

if current:
    chunks.append(current)

os.makedirs("split_patches", exist_ok=True)
for idx, chunk in enumerate(chunks):
    with open(f"split_patches/part_{idx:04}.patch", "w") as f:
        f.writelines(chunk)
