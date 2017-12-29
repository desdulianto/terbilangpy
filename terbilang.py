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
    mengembalikan string terbilang dari integer angka

    >>> terbilang(10)
    'sepuluh'

    >>> terbilang(0)
    'nol'

    >>> terbilang(12759247)
    'dua belas juta tujuh ratus lima puluh sembilan ribu dua ratus empat puluh tujuh'

    :param angka: integer input untuk menghasilkan terbilang
    :return: string terbilang
    """
    if angka < 0:
        return "negatif " + terbilang(abs(angka)).strip()
    elif 0 <= angka <= 9:
        return satuan[int(angka)]
    elif 11 <= angka <= 19:
        return "{} belas".format(satuan[angka % 10]).replace("satu belas", "sebelas").strip()
    else:
        pos, batas = find_first(lambda x: angka >= x[1][0], enumerate(suffix))
        if batas is not None:
            return "{} {} {}".format(terbilang(int(angka / batas[0])), suffix[pos][1],
                                     terbilang(angka % batas[0]) if angka % batas[0] > 0 else "")\
                .replace("satu puluh", "sepuluh")\
                .replace("satu ratus", "seratus")\
                .replace("satu ribu", "seribu").strip()
        else:
            return ""

if __name__ == '__main__':
    import doctest
    doctest.testmod()
