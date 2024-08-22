### Draw the Single-Rank
import Excel.Read as rd
import Bar.SingleBar as sb

def drawRank(file_paths, sheet_names, sizes):
    categories = []
    data = []
    for i in range(len(file_paths)):
        res = rd.readRank(file_paths[i], sheet_names[i], sizes[i])
        # Get the categories
        if i == 0:
            res[0].pop(0)
            if (sheet_names[i] == "ans"):
                res[0].pop()
            categories = [cat if cat != 'm_SCA' else 'MSCA' for cat in res[0]]
            # categories = res[0]
        # Get the data
        data.append([res[1][i + 1] for i in range(len(categories))])
        # categories.pop(0)
        # data[0].pop(0)
    sb.drawSglBar(categories, data)

# 2017-30
# file_paths = [r"E:\MDM\Paper\LGDAO\Figure\4-2017-Improve-30\1-Source\LGDAO-30-E.xlsx"]
# sizes = [31]
# 2017-100
# file_paths = [r'E:\MDM\Paper\LGDAO\Figure\5-2017-Improve-100\1-Source\LGDAO-100-E.xlsx']
# sizes = [31]
# 2017-Ablation
file_paths = [r"D:\Project\MDM\Python\Table\Excel\LGDAO-10.xlsx"]
sizes = [31]
# 2022
# file_paths = [r"E:\MDM\Paper\LGDAO\Figure\6-2022-Improve\1-Source\LGDAO-2022.xlsx"]
# sizes = [13]
# Feature 
# file_paths = [r"E:\MDM\Paper\LGDAO\Figure\8-bLGDAO-Other\1-Source\Feature-Best_fitness.xlsx"]
# file_paths = [r"E:\MDM\Paper\LGDAO\Figure\8-bLGDAO-Other\1-Source\Feature-Error.xlsx"]
# file_paths = [r"E:\MDM\Paper\LGDAO\Figure\8-bLGDAO-Other\1-Source\Feature-NumOfFeature.xlsx"]
sheet_names = ["ans"]

res = drawRank(file_paths, sheet_names, sizes)

