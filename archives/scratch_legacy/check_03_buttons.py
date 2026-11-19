import os

DIR_03 = r"C:\Users\HP\Downloads\Components\03-buttons-and-interactions"
items = os.listdir(DIR_03)
for item in items:
    abs_p = os.path.join(DIR_03, item)
    if os.path.isdir(abs_p):
        has_index = os.path.exists(os.path.join(abs_p, "index.html"))
        print(f"Subdir: {item} | Has index.html: {has_index}")
