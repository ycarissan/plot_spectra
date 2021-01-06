import numpy
import matplotlib.pyplot as plt

dir="/home/avaret/com_irreg_1_9_hexagons/done/classes"
file="/home/avaret/com_irreg_1_9_hexagons/done/classes/38_carbons_18_hydrogens/9_hexagons1968_irreg.log"

frequencies = []
intensities = []
lu = open(file, "r")
for l in lu.readlines():
    if "Frequencies" in l:
        a = l.split()
        frequencies.append(a[2])
        frequencies.append(a[3])
        frequencies.append(a[4])
    if "IR Inten" in l:
        a = l.split()
        intensities.append(a[2])
        intensities.append(a[3])
        intensities.append(a[4])

listlu = open("/home/avaret/com_irreg_1_9_hexagons/done/classes/list_dir", "r")
for dir in listlu.readlines():
    x=[]
    y=[]
    file="/home/avaret/com_irreg_1_9_hexagons/done/classes/"+dir.strip()+"results.txt"
    lu = open(file, "r")
    for l in lu.readlines()[12:]:
        l = l.replace("Result(","")
        l = l.replace(") =","")
        x.append(float(l.split()[0]))
        y.append(float(l.split()[1]))
    plt.plot(x,y)
    plt.show()
