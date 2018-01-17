import xlrd

def open_excel(fileName="C:/Users/Camille/Desktop/simple.xls"):
    try:
        fileHandler = xlrd.open_workbook(fileName)
        return fileHandler
    except Exception, e:
        print str(e)

def scan_excel(sheet_name1=u'Sheet1'):
    handler = open_excel()
    page = handler.sheet_by_name(sheet_name1)
    return page

def trim_cols(index=0):
    page = scan_excel()
    col1 = page.col_values(index)
    col2 = []

    for item in col1:
        if item not in col2:
            col2.append(item)
    print col1
    print col2


def main():
    trim_cols()


if __name__ == "__main__":
    main()