import sys

with open('/home/malav/.openclaw/workspace/tmp_awesome/README.md', 'r') as f:
    content = f.read()

# Locate the CLI Utilities section and insert the new line
insertion = "\n- [cleanup-reporter](https://github.com/MalavyaRaval/cleanup-reporter) - Scan your machine for large directories, duplicate files, and stale resume files.\n"
pattern = '<summary><h3 style="display:inline">CLI Utilities</h3></summary>'
start_index = content.find(pattern)
if start_index != -1:
    # Look for the end of the details block or the end of the list inside the details
    end_index = content.find('>', start_index)
    # Just insert it at the end of the list inside that summary block
    # It's better to insert it after the summary line? No, inside the list.
    # I'll just append it to the end of the CLI Utilities section list.
    list_end = content.find('>', start_index) # Just after the summary tag.
    # Actually, the file uses a list: 
    # - [13-day-sprint-method](...) - ...
    # ...
    # > **[View all 180 skills in CLI Utilities →](categories/cli-utilities.md)**
    # I can just insert it before the "> **[View all..."
    
    insert_point = content.find('> **[View all', start_index)
    if insert_point != -1:
        new_content = content[:insert_point] + "- [cleanup-reporter](https://github.com/MalavyaRaval/cleanup-reporter) - Scan your machine for large directories, duplicate files, and stale resume files.\n" + content[insert_point:]
        with open('/home/malav/.openclaw/workspace/tmp_awesome/README.md', 'w') as f:
            f.write(new_content)
        print("Updated README.md")
    else:
        print("Could not find insert point")
else:
    print("Could not find CLI Utilities section")
