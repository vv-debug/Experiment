### Generate the Friedman-Rank
import numpy as np
import pandas as pd
import re

def convertToFR(file_path, save_path, mean_index, result_index, count_index):
    # file_path = "E:\MDM\Python\BenchmarkResultManipulate_v3\Function23-06-13_09_22.xlsx"
    file_name = re.search(r'[^\\]+$', file_path).group()            # Get name
    save_name = "Rank-" + file_name
    save_path = save_path + save_name
    print(save_path)
    
    # Load the Sheet
    sheet_data = pd.read_excel(file_path, sheet_name="result & pValue", header=None)

    # Combine the non-empty cells in each column
    count_data = sheet_data.iloc[count_index:]

    # Record Name
    algorithm_names = sheet_data.iloc[0, 1:]
    algorithm_names = algorithm_names[(algorithm_names.notna()) & (algorithm_names != 'pvalue')]

    # Record Rank
    algorithm_rank = sheet_data.iloc[result_index, 1:]
    algorithm_rank = [x for x in algorithm_rank if not np.isnan(x)]

    # Record Mean
    algorithm_mean = sheet_data.iloc[mean_index, 1:]
    algorithm_mean = [x for x in algorithm_mean if not np.isnan(x)]

    # Record Count
    algorithm_count = []
    for col in count_data.columns:
        # Get non-empty cells in the column
        non_empty_cells = count_data[col].dropna().tolist()
        # Combine each cells with '/'
        combined_str = "/".join(map(str, non_empty_cells))
        # Append the combined string to the list
        algorithm_count.append(combined_str)
    algorithm_count = " ".join([str(cell) for cell in algorithm_count if str(cell) != ""])
    algorithm_count = algorithm_count.split()[1:]
    algorithm_count.insert(0, "")

    data_rows = pd.DataFrame({"Name":algorithm_names, "Mean": algorithm_mean, 
                              "Rank": algorithm_rank, "Result": algorithm_count}).T

    # Save the Result
    data_rows.to_excel(save_path, index=False, header=False)


file_path = r"D:\Project\MDM\Python\Table\Excel\GDAO.xlsx"
save_path = r"D:\Project\MDM\Python\Table\Excel\\"
## 2017
# The row number of mean
mean_index = 31
result_index = 32
count_index = 33
## 2022
# mean_index = 13
# result_index = 14
# count_index = 15
convertToFR(file_path, save_path, mean_index, result_index, count_index)
