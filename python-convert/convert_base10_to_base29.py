#!/usr/bin/python
import csv
import argparse

alpha = list("0123456789BCFGHJKLMNPQRTVWXYZ")


def GetArgs():
    """
     Supports the command-line arguments listed below.
     """
    parser = argparse.ArgumentParser(
        description='Please input info for your command')
    parser.add_argument('-q', '--quantity', required=True, action='store',
                        help='Input quantity: 1-9999')
    parser.add_argument('-f', '--format', required=False, action='store',
                        help='2: XX, 4: XXXX')

    args=parser.parse_args()
    return args


def main():
    args = GetArgs()
    quantity = int(args.quantity)
    format = int(args.format)

    list = []
    i = 1
    while i < quantity:

        #print len(decrypt(i))
        my_str = "0000" + "%s" % decrypt(i)
        my_str_trunc = '{0}'.format(my_str[-format:])
        #print my_str_trunc
        i = i + 1
        #print int(my_str_trunc)
        print my_str_trunc
        list.append([my_str_trunc])

        #a = numpy.asarray([list])
        with open("output.csv", "wb") as f:
            writer = csv.writer(f)
            writer.writerows(list)


def decrypt(a):
    remainder = int(a)
    result = ""
    while remainder > 0:
        result = alpha[remainder % 29] + result
        remainder //= 29
    return result or "0"

if __name__ == "__main__":
    main()