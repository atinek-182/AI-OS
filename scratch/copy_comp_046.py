import os
import shutil

src_dir = r"C:\Users\HP\Downloads\Components\02-navigation-and-menus\side-navigation-with-wipe-effectosmo\side-navigation-with-wipe-effectosmo"
dest_dir = r"d:\AI-OS\projects\Websites\Vidya-Dham-Academy\reference\side-navigation-with-wipe-effectosmo"

if os.path.exists(dest_dir):
    shutil.rmtree(dest_dir)

shutil.copytree(src_dir, dest_dir)
print(f"[OK] Copied {src_dir} -> {dest_dir}")
