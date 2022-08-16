aukstis = 740
plotis = 834
lauko_dydis = 10
langeliu_sk = lauko_dydis ** 2
minu_sk = langeliu_sk // 10


def aukscio_dalis(procentai):
    return int(aukstis // 100 * procentai)

def plocio_dalis(procentai):
    return int(plotis // 100 *procentai)
