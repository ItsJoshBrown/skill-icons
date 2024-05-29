import os

def update_readme(readme_file, new_content, start_marker, end_marker):
    with open(readme_file, 'r') as file:
        content = file.read()
    
    start_index = content.find(start_marker) + len(start_marker)
    end_index = content.find(end_marker)

    if start_index == -1 or end_index == -1:
        raise ValueError("Markers not found in the README file")
    
    updated_content = content[:start_index] + '\n' + new_content + '\n' + content[end_index:]
    
    with open(readme_file, 'w') as file:
        file.write(updated_content)

def generate_icons_table(icon_folder, icon_id_width=20, icon_path_width=20):
    icons = sorted(os.listdir(icon_folder))
    header = f"| {'Icon ID'.ljust(icon_id_width)} | {'Dark Icon'.ljust(icon_path_width)} | {'Icon ID'.ljust(icon_id_width)} | {'Light Icon'.ljust(icon_path_width)} | {'Icon ID'.ljust(icon_id_width)} | {'Neutral Icon'.ljust(icon_path_width)} |\n"
    separator = f"| {'-' * icon_id_width} | {'-' * icon_path_width} | {'-' * icon_id_width} | {'-' * icon_path_width} | {'-' * icon_id_width} | {'-' * icon_path_width} |\n"

    table_md = header + separator
    dark_icons = [icon for icon in icons if "-dark" in icon]
    light_icons = [icon for icon in icons if "-light" in icon]
    neutral_icons = [icon for icon in icons if "-light" not in icon and "-dark" not in icon]
    max_icons = max(len(dark_icons), len(light_icons), len(neutral_icons))
    
    for i in range(max_icons):
        if i < len(dark_icons):
            dark_icon_id = os.path.splitext(dark_icons[i])[0].replace("-dark", "")
            dark_icon_path = f"<img src=\"./{icon_folder}/{dark_icons[i]}\" width=\"48\">"
        else:
            dark_icon_id = ""
            dark_icon_path = ""
        
        if i < len(light_icons):
            light_icon_id = os.path.splitext(light_icons[i])[0].replace("-light", "")
            light_icon_path = f"<img src=\"./{icon_folder}/{light_icons[i]}\" width=\"48\">"
        else:
            light_icon_id = ""
            light_icon_path = ""
        
        if i < len(neutral_icons):
            neutral_icon_id = os.path.splitext(neutral_icons[i])[0]
            neutral_icon_path = f"<img src=\"./{icon_folder}/{neutral_icons[i]}\" width=\"48\">"
        else:
            neutral_icon_id = ""
            neutral_icon_path = ""
        
        table_md += f"| {dark_icon_id.ljust(icon_id_width)} | {dark_icon_path.ljust(icon_path_width)} | {light_icon_id.ljust(icon_id_width)} | {light_icon_path.ljust(icon_path_width)} | {neutral_icon_id.ljust(icon_id_width)} | {neutral_icon_path.ljust(icon_path_width)} |\n"
    
    return table_md


if __name__ == "__main__":
    icon_folder = "assets"
    readme_file = "README.md"
    start_marker = "<!-- START ICONS LIST -->"
    end_marker = "<!-- END ICONS LIST -->"
    
    new_table = generate_icons_table(icon_folder)
    update_readme(readme_file, new_table, start_marker, end_marker)
