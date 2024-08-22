import pandas as pd
import re

# convert Benchmark result to the Data of Box Plot
def convertToBox(file_path, save_path):
    # file_name = re.findall(r'[^\\]+$', file_path)[0]              # Get name without extension
    file_name = re.search(r'[^\\]+$', file_path).group()            # Get name
    save_name = "Box-" + file_name
    save_path = save_path + save_name

    # Select sheets
    sheet_names = ['F10', 'F21', 'F22', 'F23', 'F24', 'F25', 'F26', 'F27', 'F28', 'F29', 'F30']
    # sheet_names = ['F10']

    
    # Record data of sheets
    all_sheets_data = {}

    for sheet_name in sheet_names:
        # Read data by sheet name
        sheet_data = pd.read_excel(file_path, sheet_name=sheet_name, header=None)
        
        # Drop the number of experiments
        # sheet_data = sheet_data.drop(columns=sheet_data.columns[1])
        
        # Get algorithm name
        algorithm_names = sheet_data.iloc[:, 0].unique()
        
        # Record processed data 
        reshaped_data = pd.DataFrame()
        for name in algorithm_names:
            algorithm_data = sheet_data[sheet_data.iloc[:, 0] == name].iloc[:, -1]
            # algorithm_data = pd.DataFrame(algorithm_data.iloc[:, 1:]).values.flatten()
            # reshaped_data.append(algorithm_data)
            reshaped_data[name] = algorithm_data.reset_index(drop=True)

        # Show the size of sheet
        print('sheetName: ', sheet_name, 'Size: ', reshaped_data.shape)
        all_sheets_data[sheet_name] = reshaped_data
    with pd.ExcelWriter(save_path) as writer:
        for sheet_name, df in all_sheets_data.items():
            df.to_excel(writer, sheet_name=sheet_name, index=False)

file_path = "E:\\MDM\\Python\\Table\\Excel\\Function23-06-13_09_22.xlsx"
save_path = "E:\\MDM\\Python\\Table\\"
convertToBox(file_path, save_path)