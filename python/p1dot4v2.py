# NEW: Import zip_longest so columns with different numbers of products
# can still be written row-by-row without losing data.
from itertools import zip_longest

import csv


# STEP 1 & 2: Open and read your raw CSV file
# EDIT! input_filename to match your downloaded CSV file.
input_filename = "mockaroo-data-09012026.csv"

cleaned_rows = []

with open(input_filename, mode="r", encoding="utf-8") as file:
    reader = csv.reader(file)
    next(reader)  # Skip header
    
    for row in reader:
        # Clean extra spaces and convert all text to lowercase.
        # SAME AS ORIGINAL CODE.
        cleaned_row = [col.strip().lower() for col in row]
        cleaned_rows.append(cleaned_row)


# ---------------------------------------------------------
# CHANGED FROM ORIGINAL STEP 4:
# ---------------------------------------------------------
# ORIGINAL:
# The output was a simple 2-column spreadsheet:
# Category | Product Data
#
# NEW:
# Each category will become its OWN COLUMN HEADER.
#
# Example:
# Food & Groceries | Clothing & Accessories | Tech & Gadgets | Pets & Fitness | Others
# product 1        | product 1               | product 1      | product 1     | product 1
# product 2        | product 2               | product 2      |               |
# ---------------------------------------------------------

output_filename = "edit-filename.csv"


# NEW:
# Create a dictionary to hold the products belonging to each category.
#
# The category names will later become the column headers.
categorized_data = {
    "Food & Groceries": [],
    "Tech & Gadgets": [],
    "Clothing & Accessories": [],
    "Pets": [],
    "Fitness": [],
    "Others": []
}


# ---------------------------------------------------------
# CHANGED FROM ORIGINAL STEP 5:
# ---------------------------------------------------------
# ORIGINAL:
# Each row was assigned ONE category and immediately written
# to the output CSV:
#
# writer.writerow([category, text])
#
# NEW:
# We first collect/group all products into category lists.
# They are NOT written to the CSV yet.
# ---------------------------------------------------------

for row in cleaned_rows:
    # Combine all columns from the original CSV row into
    # one piece of text.
    text = " ".join(row)
    
    
    if "food" in text:
        categorized_data["Food & Groceries"].append(text)
        
    elif "clothing" in text or "top" in text or "pants" in text:
        # NEW keywords: "top" and "pants"
        categorized_data["Clothing & Accessories"].append(text)
        
    elif "electronics" in text or "photography" in text:
        categorized_data["Tech & Gadgets"].append(text)
        
    elif "pets" in text:
        categorized_data["Pets"].append(text)

    elif "fitness" in text or "yoga" in text:
        categorized_data["Fitness"].append(text)

        
    else:
        # Anything that doesn't match the conditions
        # goes into the Others column.
        categorized_data["Others"].append(text)


# ---------------------------------------------------------
# NEW OUTPUT STRUCTURE:
# ---------------------------------------------------------
# Instead of writing:
#
# Category | Product Data
#
# We now write:
#
# Food & Groceries | Tech & Gadgets | Clothing & Accessories | Pets & Fitness | Others
# ---------------------------------------------------------

with open(output_filename, mode="w", newline="", encoding="utf-8") as outfile:
    writer = csv.writer(outfile)
    
    
    # NEW:
    # Get the category names from the dictionary.
    # These become the first/header row of the CSV.
    headers = list(categorized_data.keys())
    
    # Write the category names across the top.
    writer.writerow(headers)
    
    
    # NEW:
    # Get the lists of products from each category.
    #
    # Example:
    # [
    #   [food1, food2, food3],
    #   [tech1, tech2],
    #   [clothing1, clothing2, clothing3, clothing4],
    #   ...
    # ]
    columns = list(categorized_data.values())
    
    
    # NEW:
    # zip_longest lines up the products row-by-row.
    #
    # If one category has fewer products than another,
    # fillvalue="" leaves the empty cell blank instead
    # of stopping early.
    #
    # Example:
    #
    # Food     | Tech     | Clothing
    # ---------|----------|----------
    # food 1   | tech 1   | shirt 1
    # food 2   | tech 2   | shirt 2
    # food 3   |          | shirt 3
    #
    for row_items in zip_longest(*columns, fillvalue=""):
        writer.writerow(row_items)


# Updated confirmation message to reflect the new
# column-header spreadsheet structure.
print("Done! Your column-header spreadsheet is ready.")