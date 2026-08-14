import os
import glob

components_dir = r"C:\Users\HP\Downloads\Components"
if os.path.exists(components_dir):
    py_files = glob.glob(os.path.join(components_dir, "**", "*.py"), recursive=True)
    print(f"Found {len(py_files)} Python files in {components_dir}:")
    for f in py_files:
        print(" -", f)
else:
    print(f"Directory {components_dir} does not exist.")
