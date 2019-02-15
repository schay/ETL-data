import math
import os

pkg_dir = os.environ['PYTHONPATH']

shift_jis = []
jisx0208 = []
unicode = []

with open(pkg_dir[:-1] + "/etl/JIS0208.TXT") as f:
    for line in f:
        if line[0] == "#":
            pass
        else:
            sjis, jisx, unic, _ = line.strip().split("\t")
            shift_jis.append(int(sjis,16))
            jisx0208.append( int(jisx,16))
            unicode.append(  int(unic,16))

def jis2uni(n):
    return unicode[jisx0208.index(n)]

def decode_label(label) :
    border = 71
    l1 = 36
    l2 = 32
    if label < 5 :
        l2 += (label+1)*2
    elif label < 29 :
        l2 += label + 6
    elif label < 60:
        l2 += label + 7
    elif label < 63:
        l2 += (label - 60)*2 + 68
    elif label < 68:
        l2 += label + 10
    elif label < 69:
        l2 += label + 11
    elif label < 71:
        l2 += label + 13
    else:
        # 漢字
        l1 += math.floor((label - border) / 94) + 12
        l2 += (label - border)%94 + 1

    return chr(jis2uni(eval(hex(l1 * 256 + l2))))
