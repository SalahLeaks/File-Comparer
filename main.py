import json

# File paths
old_file = "Old.txt"
new_file = "New.txt"
output_json = "added_lines.json"

# Read old file
with open(old_file, "r", encoding="utf-8") as f:
    old_lines = set(f.readlines())

# Read new file
with open(new_file, "r", encoding="utf-8") as f:
    new_lines = set(f.readlines())

# Find added lines
added_lines = list(new_lines - old_lines)

# Save added lines to JSON
with open(output_json, "w", encoding="utf-8") as f:
    json.dump({"added_lines": added_lines}, f, indent=4, ensure_ascii=False)

print(f"Added lines saved to {output_json}")