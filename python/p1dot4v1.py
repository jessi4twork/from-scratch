# STEP 1: Grab the spreadsheet tool
import csv

# STEP 2: Open and read your raw CSV file
# EDIT! input_filename to match your downloaded CSV file
# Make sure your CSV file is in the same folder as this script, or provide the full path to the file.
input_filename = "mockaroo-data-09012026.csv"
cleaned_rows = []

with open(input_filename, mode="r", encoding="utf-8") as file:
    reader = csv.reader(file)
    next(reader) # Skip header
    
    for row in reader:
        # STEP 3: Clean extra spaces and uppercase letters
        cleaned_row = [col.strip().lower() for col in row]
        cleaned_rows.append(cleaned_row)

# STEP 4: Sort data and export a new file for Google Sheets
# output_filename is the name of the new CSV file that will be created. EDIT! based on your preference.
output_filename = "edit-this-filename.csv"

with open(output_filename, mode="w", newline="", encoding="utf-8") as outfile:
    writer = csv.writer(outfile)
    writer.writerow(["Category", "Product Data"])
    
    for row in cleaned_rows:
        text = " ".join(row)
        
        # STEP 5: Assign categories
        #depending on data in the text, assign a category. You can customize these conditions based on your dataset.
        if "food" in text:
            category = "Food & Groceries"
        elif "clothing" in text or "image" in text:
            category = "Clothing & Accessories"
        elif "electronics" in text or "photography" in text:
            category = "Tech & Gadgets"
        elif "pets" in text:
            category = "Pets"
        elif "fitness" in text:
            category = "Fitness"
        else:
            category = "Others"
            
        writer.writerow([category, text])

print("Done! Your Google Sheets file is ready.")