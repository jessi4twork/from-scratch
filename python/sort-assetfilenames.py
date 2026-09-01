raw_assets = ["glow_cream_banner.jpg", "serum_thumb.png", "cleanser_shot.jpg"]
banners = []
thumbnails = []
others = []
for file in raw_assets:
    if "banner" in file:
        banners.append(file)
    elif "thumb" in file:
        thumbnails.append(file)
    else:
        others.append(file)
print("Banners:", banners)
print("Thumbnails:", thumbnails)
print("Others:", others)
