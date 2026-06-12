from pathlib import Path
p = Path(r'C:\Users\zabal\OneDrive\Desktop\MI TIENDA RELOJERIA DIVINA\imagenes')
files = sorted([f.name for f in p.iterdir() if f.is_file() and f.name.lower().startswith('reloj')], key=lambda x: int(''.join(filter(str.isdigit, x)) or 0))
print('const imagenes = [')
for name in files:
    print(f'  "{name}",')
print('];')
