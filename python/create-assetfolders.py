client_folders = ["01_raw_assets", "02_banners", "03_product_thumbnails", "04_brand_board"]

folder_purposes = {
    "01_raw_assets": "Unedited files straight from the client",
    "02_banners": "Resized website header graphics",
    "03_product_thumbnails": "Clean Shopify listing images",
    "04_brand_board": "Canva colors, fonts, and logos"
}

print("--- Setting up workspace structure ---")

for folder in client_folders:
    purpose = folder_purposes[folder]
    print(f"Creating folder -> [{folder}] | Purpose: {purpose}")
