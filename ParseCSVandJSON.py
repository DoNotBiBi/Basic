import csv


# todo:
#   理清为啥要重新读取文件才能输出
def test_csv_read():
    exampleFile = open('test.csv')
    exampleReader = csv.reader(exampleFile)
    for row in exampleReader:
        print(str(row))
    exampleFile = open('test.csv')
    exampleReader = csv.reader(exampleFile)
    exampleData = list(exampleReader)
    print(exampleData)
    print(exampleData[1])
    print(exampleData[0][1])
    exampleFile.close()


def test_csv_write():
    outputFile = open('outputCSV.csv', 'w', newline='')
    outputWriter = csv.writer(outputFile)
    outputWriter.writerows([['hello', 'wangkang', 'nihao'], ['heqing', 'shacha', 'shabi']])
    outputFile.close()
