import pandas as pd
import re

def calMeanAndCreate(input_path):
    # New Excel path
    out_path = re.sub(r'\\[^\\]*\.xlsx$', '.xlsx', input_path)

    # Step 1: Read the Excel file and get all sheet names
    xls = pd.ExcelFile(input_path)
    sheet_names = xls.sheet_names

    writer = pd.ExcelWriter(out_path, engine='openpyxl')

    keywords = ['overall', 'result', 'pvalue', 'ans']
    # Step 2: For each sheet, read the data, reset the index, group by the first column, and calculate the mean
    for sheet_name in sheet_names:
        print(sheet_name)
        # Skip sheets whose names contain 'result', 'pValue', 'ans', or 'overall'
        if any(key in sheet_name.lower() for key in keywords):
            continue
        df = pd.read_excel(xls, sheet_name=sheet_name, header=None)
        grouped_df = df.groupby(df.columns[0], sort=False).mean()

        # Step 3: Write the processed data of each sheet to the new Excel file
        grouped_df.to_excel(writer, sheet_name=sheet_name, index=True)

    # Save the new Excel file
    print(out_path)
    writer.close()
    return out_path