import pandas as pd

def readRank(file_path, sheet_name, size):
    # 使用pandas读取Excel文件的指定工作表
    df = pd.read_excel(file_path, sheet_name=sheet_name)

    # 获取指定行的数据（pandas的索引从0开始，所以需要减1）
    headers = df.columns.tolist()
    row_data = df.iloc[size - 1]
    return [list(headers), list(row_data)]

def readSheet(file_path):
    # Read the Excel file and get all sheet names
    xls = pd.ExcelFile(file_path)
    sheet_names = xls.sheet_names
    names = []
    values = []
    # For each sheet, read the data and slice from the third column
    for sheet_name in sheet_names:
        df = pd.read_excel(xls, sheet_name=sheet_name)
        if not names:
            names = df.iloc[0]
        values.append(df.iloc[:, 2:])
    return [names, values]