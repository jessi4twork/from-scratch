# --- STEP 1: Set up your project workspace structure (Project 1.3) ---
client_folders = ["01_raw_assets", "02_banners", "03_product_thumbnails", "04_brand_board"]

folder_purposes = {
    "01_raw_assets": "Unedited files straight from the client",
    "02_banners": "Resized website header graphics",
    "03_product_thumbnails": "Clean Shopify listing images",
    "04_brand_board": "Canva colors, fonts, and logos"
}

print("=== 1. BUILDING WORKSPACE BLUEPRINT ===")
for folder in client_folders:
    purpose = folder_purposes[folder]
    print(f"Creating folder -> [{folder}] | Purpose: {purpose}")


# --- STEP 2: Clean the messy raw filenames (Project 1.2) ---
# Imagine this is the messy batch of files downloaded for your Shopify/Canva project
raw_filenames = [
    "Glow Cream Banner (1).jpg", 
    "serum-thumb-FINAL.png", 
    "CLEANSER SHOT.JPG",
    "glow_cream_sku101.jpg"
]

cleaned_filenames = []

print("\n=== 2. CLEANING FILENAMES ===")
for name in raw_filenames:
    step1 = name.lower()
    step2 = step1.replace(" ", "_")
    step3 = step2.replace("(", "").replace(")", "")
    cleaned_filenames.append(step3)
    print(f"Cleaned: '{name}' ---> '{step3}'")


# --- STEP 3: Sort the clean files into categories (Project 1.1) ---
banners = []
thumbnails = []
others = []

for file in cleaned_filenames:
    if "banner" in file:
        banners.append(file)
    elif "thumb" in file:
        thumbnails.append(file)
    else:
        others.append(file)

print("\n=== 3. FINAL SORTED ASSETS ===")
print("Banners bucket:", banners)
print("Thumbnails bucket:", thumbnails)
print("Others/Product shots bucket:", others)
