from datetime import datetime, timedelta


def tle_epoch_datetime(line):
    try:
        yd, s = line[18:32].split('.')
        epoch = datetime.strptime(yd, "%y%j") + timedelta(seconds=float("." + s) * 24 * 60 * 60)
        return epoch
    except:
        return False


def tle_set_number(line):
    try:
        return line[65:68]
    except:
        return False
