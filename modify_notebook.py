import json
import re

notebook_path = 'd:/pythonProject_Book/all_python_files_save_images.ipynb'

with open(notebook_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

current_name = None

for cell in nb['cells']:
    if cell['cell_type'] == 'markdown':
        text = "".join(cell['source']).strip()
        m = re.search(r'([a-zA-Z0-9_\-\.\'\s]+)\.py', text, re.IGNORECASE)
        if m:
            current_name = m.group(1).strip()
            # If current_name has leading #, strip it
            current_name = re.sub(r'^#+\s*', '', current_name)
    elif cell['cell_type'] == 'code' and current_name is not None:
        source = "".join(cell['source'])
        
        save_code = f"""
# --- Save Figures ---
import matplotlib.pyplot as plt
_fignums = plt.get_fignums()
if len(_fignums) == 1:
    plt.figure(_fignums[0]).savefig('{current_name}.png')
    plt.figure(_fignums[0]).savefig('{current_name}.pdf')
elif len(_fignums) > 1:
    for _i, _fignum in enumerate(_fignums):
        plt.figure(_fignum).savefig(f'{current_name}_{{_i+1}}.png')
        plt.figure(_fignum).savefig(f'{current_name}_{{_i+1}}.pdf')
# --------------------
"""
        
        new_source = []
        lines = source.splitlines(keepends=True)
        found_show = False
        for line in lines:
            m = re.match(r'^(\s*)plt\.show\(\)', line)
            if m:
                found_show = True
                indent = m.group(1)
                indented_save_code = "\n".join(indent + l if l.strip() else l for l in save_code.strip().splitlines())
                new_source.append(indented_save_code + "\n")
            new_source.append(line)
            
        if not found_show:
             new_source.append("\n" + save_code.strip() + "\n")
             
        cell['source'] = new_source
        current_name = None # Reset for next cell

with open(notebook_path, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1)

print("Notebook updated successfully.")
