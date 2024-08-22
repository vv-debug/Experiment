### Draw the Mult-Rank
import Excel.Read as rd
import Bar.MultBar as mb
def drawRank(file_paths, sheet_names, sizes, labels):
    categories = []
    data = []
    for i in range(len(file_paths)):
        res = rd.readRank(file_paths[i], sheet_names[i], sizes[i])
        # Get the categories
        if i == 0:
            res[0].pop(0)
            categories = res[0]
        # Get the data
        data.append([res[1][i + 1] for i in range(len(categories))])
    mb.drawMultBar(categories, data, labels)

if __name__ == "__main__":
    file_paths = [r"D:\Project\MDM\Python\Table\Excel\LGDAO-10.xlsx", 
                  r"D:\Project\MDM\Python\Table\Excel\LGDAO-30.xlsx", 
                  r"D:\Project\MDM\Python\Table\Excel\LGDAO-50.xlsx", 
                  r"D:\Project\MDM\Python\Table\Excel\LGDAO-100.xlsx"]
    sheet_names = ["ans", "ans", "ans", "ans"]
    labels = ["10 Dim", "30 Dim", "50 Dim", "100 Dim"]
    sizes = [31, 31, 31, 31]
    res = drawRank(file_paths, sheet_names, sizes, labels)


