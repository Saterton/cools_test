import time

from file_parse import FileParse

if __name__ == '__main__':
    parse = FileParse('products.txt')
    timer = time.time()
    parse.parse()
    print(time.time() - timer)
