import shutil


for x in range(1,101):
    try:   
        shutil.move(f'day{x}.py', f'day{x}folder')
    except FileNotFoundError:
        pass