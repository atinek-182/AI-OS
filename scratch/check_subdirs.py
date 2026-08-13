import os

for sub in ["codrops-add-to-cart", "ElasticProgress"]:
    p = os.path.join(r"C:\Users\HP\Downloads\Components\03-buttons-and-interactions", sub)
    print(f"\n--- {sub} ---")
    for root, dirs, files in os.walk(p):
        for f in files:
            print(" ", os.path.relpath(os.path.join(root, f), p))
