satuan = ('nol', 'satu', 'dua', 'tiga', 'empat', 'lima', 'enam', 'tujuh', 'delapan', 'sembilan')
suffix = ((1000000000000, "trilyun"),
          (1000000000, "milyar"),
          (1000000, "juta"),
          (1000, "ribu"),
          (100, "ratus"),
          (10, "puluh"))


def find_first(predicate, items):
    """
    mencari item pertama yang memenuhi persyaratan predicate

    :param predicate: persyaratan yang harus dipenuhi
    :param items: list items
    :return: tuple (pos, item) jika tidak ditemukan (-1, None)
    """
    hasil = list(filter(predicate, items))
    return hasil[0] if len(hasil) > 0 else None


def terbilang(angka):
    """
    mengembalikan string terbilang dari angka
    :param angka: integer input untuk menghasilkan terbilang
    :return: string terbilang
    """
    if angka < 0:
        return "negatif " + terbilang(abs(angka))
    elif 0 <= angka <= 9:
        return satuan[int(angka)]
    elif 11 <= angka <= 19:
        return "{} belas".format(satuan[angka % 10]).replace("satu belas", "sebelas")
    else:
        pos, batas = find_first(lambda x: angka >= x[1][0], enumerate(suffix))
        if batas is not None:
            return "{} {} {}".format(terbilang(int(angka / batas[0])), suffix[pos][1],
                                     terbilang(angka % batas[0]) if angka % batas[0] > 0 else "")\
                .replace("satu puluh", "sepuluh")\
                .replace("satu ratus", "seratus")\
                .replace("satu ribu", "seribu")
        else:
            return ""


if __name__ == '__main__':
    tests = (0, 10, 11, 19, 29, 99, 399, 500, 702, 1000, 2000, 372159, 1000000, 2000000, 12759247, 3000000000,
             79296467392, 932658259587, 1000000000000, 716005407201000, 857689000128256, 342857689000128256)
    for x in tests:
        print(x, terbilang(x))
