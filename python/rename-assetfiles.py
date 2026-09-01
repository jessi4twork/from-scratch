raw_filenames = ["glow cream banner (1).jpg", "serum-thumb-FINAL.png", "cleanser shot.JPG"]

cleaned_filenames = []

for name in raw_filenames:
    step1 = name.lower()
    step2 = step1.replace(" ", "_")
    step3 = step2.replace("(", "").replace(")", "")
    cleaned_filenames.append(step3)

print("Original Names:", raw_filenames)
print("Cleaned Names:", cleaned_filenames)
