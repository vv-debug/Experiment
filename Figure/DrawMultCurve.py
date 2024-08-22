# Draw the 
import Curve.MultCurve as mc
import Excel.Write as wr

if __name__ == "__main__":
    input_paths = [r"E:\MDM\Paper\LGDAO\Experiment\Improvement\LGDAO-2017-100\LGDAO.xlsx"]
    out_path = r"E:\MDM\Paper\LGDAO\Experiment\Improvement\LGDAO-2017-100.xlsx"
    for input_path in input_paths:
        # out_path = wr.calMeanAndCreate(input_path)
        mc.drawMultCurve(out_path)

