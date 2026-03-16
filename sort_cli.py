
file_path = '/home/malav/.openclaw/workspace/tmp_awesome/categories/cli-utilities.md'

with open(file_path, 'r') as f:
    lines = f.readlines()

new_lines = []
skill_entries = []

# Parse lines
for line in lines:
    if line.startswith('- ['):
        skill_entries.append(line.strip())
    else:
        new_lines.append(line)

# Filter unique entries for cleanup-reporter
unique_entries = []
seen = set()
for entry in skill_entries:
    if "cleanup-reporter" in entry:
        if "cleanup-reporter" not in seen:
            unique_entries.append(entry)
            seen.add("cleanup-reporter")
    else:
        unique_entries.append(entry)

# Sort alphabetically
unique_entries.sort()

# Reconstruct
# The file has a header and intro text.
# Find index to insert
header_index = 0
for i, line in enumerate(new_lines):
    if line.startswith('- '):
        header_index = i
        break

final_lines = new_lines[:header_index] + [entry + '\n' for entry in unique_entries] + new_lines[header_index:]

# Update skill count header
for i, line in enumerate(final_lines):
    if "**180 skills**" in line:
        final_lines[i] = line.replace("**180 skills**", "**181 skills**")
    if "**181 skills**" in line:
        pass # Already updated
        
with open(file_path, 'w') as f:
    f.writelines(final_lines)

print("Updated CLI Utilities list")
