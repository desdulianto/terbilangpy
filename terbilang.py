def find_first(predicate, items):
    for i, item in enumerate(items):
        if predicate(item):
            return i, item
    return None


def terbilang(angka):
    satuan = ('nol', 'satu', 'dua', 'tiga', 'empat', 'lima', 'enam', 'tujuh', 'delapan', 'sembilan')
    suffix = ((1000000000000, "trilyun"),
              (1000000000, "milyar"),
              (1000000, "juta"),
              (1000, "ribu"),
              (100, "ratus"),
              (10, "puluh"))

    if angka < 0:
        return "negatif " + terbilang(abs(angka))
    elif 0 <= angka <= 9:
        return satuan[int(angka)]
    elif 11 <= angka <= 19:
        return "{} belas".format(satuan[angka % 10]).replace("satu belas", "sebelas")
    else:
        batas = find_first(lambda x: angka >= x[0], suffix)
        if batas != None:
            return "{} {} {}".format(terbilang(int(angka / batas[1][0])), suffix[batas[0]][1],
                                     terbilang(angka % batas[1][0]) if angka % batas[1][0] > 0 else "")\
                .replace("satu puluh", "sepuluh")\
                .replace("satu ratus", "seratus")\
                .replace("satu ribu", "seribu")
        else:
            return ""


if __name__ == '__main__':
    tests = (0, 10, 11, 19, 29, 99, 399, 500, 702, 1000, 2000, 372159, 1000000, 2000000, 12759247, 3000000000, 79296467392,
             932658259587, 1000000000000, 716005407201000, 857689000128256, 342857689000128256)
    for x in tests:
        print(x, terbilang(x))
