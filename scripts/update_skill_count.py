import re
from pathlib import Path

def update_skill_count():
    cli_utilities_path = Path("tmp_awesome/categories/cli-utilities.md")
    if not cli_utilities_path.exists():
        print(f"Error: {cli_utilities_path} not found.")
        return

    content_lines = cli_utilities_path.read_text(encoding='utf-8').splitlines()
    skill_count = 0
    
    for line in content_lines:
        if line.strip().startswith('- ['):
            skill_count += 1

    new_content_lines = []
    updated = False
    for line in content_lines:
        # Match the line like '- **180 skills**'
        match = re.match(r'^- \*\*(.*)\*\* skills$', line)
        if match:
            current_count_str = match.group(1)
            try:
                current_count = int(current_count_str.replace(',', '')) # Handle commas if any
                if current_count != skill_count:
                    new_content_lines.append(f'- **{skill_count} skills**')
                    updated = True
                else:
                    new_content_lines.append(line) # Keep the original line if count is already correct
            except ValueError:
                # If it's not a number, just append the line as is
                new_content_lines.append(line)
        else:
            new_content_lines.append(line)
            
    # If the count was never found or updated correctly, append it as a fallback
    if not updated and not any(f'- **{skill_count} skills**' in l for l in new_content_lines):
         # Attempt to insert it near the header if not found, or just append if section unclear
         header_pos = -1
         for i, l in enumerate(new_content_lines):
             if l.strip() == "### CLI Utilities":
                 header_pos = i
                 break
         if header_pos != -1 and header_pos + 1 < len(new_content_lines) and "**180 skills**" in new_content_lines[header_pos+1]:
             new_content_lines[header_pos+1] = f'- **{skill_count} skills**'
             updated = True
         elif header_pos != -1:
             # Insert after header if count line not found
             new_content_lines.insert(header_pos + 1, f'- **{skill_count} skills**')
             updated = True
         else:
             # Fallback: append if header not found
             new_content_lines.append(f'- **{skill_count} skills**')
             updated = True


    if updated:
        cli_utilities_path.write_text('\n'.join(new_content_lines) + '\n', encoding='utf-8')
        print(f"Updated skill count in {cli_utilities_path} to {skill_count}.")
    else:
        print(f"Skill count in {cli_utilities_path} was already correct or could not be updated.")

if __name__ == "__main__":
    update_skill_count()
