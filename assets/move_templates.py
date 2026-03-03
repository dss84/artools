import glob
import os
import re

src_dir = r"c:\Users\diego\OneDrive\Área de Trabalho\Cursos\Asimov - Design IA\artools_inicial\artools\assets"
dest_dir = os.path.join(src_dir, "templates")

files = glob.glob(os.path.join(src_dir, "design_system*.html"))
print(f"Encontrou {len(files)} arquivos")

for file in files:
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()
    
    # "templates/digital-architect..." -> "digital-architect..."
    content = content.replace('"templates/', '"')
    content = content.replace("'templates/", "'")
    
    # Save the file in the new location
    basename = os.path.basename(file)
    dest_path = os.path.join(dest_dir, basename)
    
    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(content)
        
    print(f"Moved and updated {basename}")
    
    # Remove old file
    os.remove(file)
