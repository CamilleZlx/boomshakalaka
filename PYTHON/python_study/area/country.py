#  识别属于哪个国家的产品
#  发件人国别：  { 304：德国， 305：法国， 309：荷兰， 311：葡萄牙， 312：西班牙， 318：芬兰 }

import xlrd
import xlwt
import json

def days_to_counts(argument):
    switcher = {
        "0201": 0, "0202": 1, "0203": 2, "0204": 3, "0205": 4, "0206": 5, "0207": 6, "0208": 7, "0209": 8, "0210": 9,
        "0211": 10, "0212": 11, "0213": 12, "0214": 13, "0215": 14, "0216": 15, "0217": 16 ,"0218": 17 ,"0219": 18 ,"0220": 19 ,
        "0221": 20 ,"0222": 21 ,"0223": 22 ,"0224": 23 ,"0225": 24 ,"0226": 25, "0227": 26,"0228": 27,"0301": 28,"0302": 29,
        "0303": 30,"0304": 31,"0305": 32,"0306": 33,"0307": 34,"0308": 35, "0309": 36,"0310": 37,"0311": 38,"0312": 39,
        "0313": 40,"0314": 41,"0315": 42,"0316": 43,"0317": 44,"0318": 45, "0319": 46,"0320": 47,"0321": 48,"0322": 49,
        "0323": 50, "0324": 51, "0325": 52, "0326": 53, "0327": 54, "0328": 55, "0329": 56, "0330": 57, "0331": 58
    }
    return switcher.get(argument, None)

def sort():
    filename = "D:\\python projects\\eTrace\\rawdata.xlsx"
    data = xlrd.open_workbook(filename)
    sheet = data.sheet_by_index(0)
    nrows = sheet.nrows
    ncols = sheet.ncols
    Country = [304,305,309,311,312,318]
    countryDict = {}
    for i in range(6):
        countryDict[Country[i]] = [["0201", 0, 0, 0], ["0202", 0, 0, 0], ["0203", 0, 0, 0], ["0204", 0, 0, 0],
                      ["0205", 0, 0, 0], ["0206", 0, 0, 0], ["0207", 0, 0, 0], ["0208", 0, 0, 0],
                      ["0209", 0, 0, 0], ["0210", 0, 0, 0], ["0211", 0, 0, 0], ["0212", 0, 0, 0],
                      ["0213", 0, 0, 0], ["0214", 0, 0, 0], ["0215", 0, 0, 0], ["0216", 0, 0, 0],
                      ["0217", 0, 0, 0], ["0218", 0, 0, 0], ["0219", 0, 0, 0], ["0220", 0, 0, 0],
                      ["0221", 0, 0, 0], ["0222", 0, 0, 0], ["0223", 0, 0, 0], ["0224", 0, 0, 0],
                      ["0225", 0, 0, 0], ["0226", 0, 0, 0], ["0227", 0, 0, 0], ["0228", 0, 0, 0],
                      ["0301", 0, 0, 0], ["0302", 0, 0, 0], ["0303", 0, 0, 0], ["0304", 0, 0, 0],
                      ["0305", 0, 0, 0], ["0306", 0, 0, 0], ["0307", 0, 0, 0], ["0308", 0, 0, 0],
                      ["0309", 0, 0, 0], ["0310", 0, 0, 0], ["0311", 0, 0, 0], ["0312", 0, 0, 0],
                      ["0313", 0, 0, 0], ["0314", 0, 0, 0], ["0315", 0, 0, 0], ["0316", 0, 0, 0],
                      ["0317", 0, 0, 0], ["0318", 0, 0, 0], ["0319", 0, 0, 0], ["0320", 0, 0, 0],
                      ["0321", 0, 0, 0], ["0322", 0, 0, 0], ["0323", 0, 0, 0], ["0324", 0, 0, 0],
                      ["0325", 0, 0, 0], ["0326", 0, 0, 0], ["0327", 0, 0, 0], ["0328", 0, 0, 0],
                      ["0329", 0, 0, 0], ["0330", 0, 0, 0], ["0331", 0, 0, 0]]

    for i in range(1,nrows):
        t = sheet.cell_value(i, 4)      # 时间
        id = sheet.cell_value(i, 17)    # 商品名称
        n = sheet.cell_value(i, 20)     # 商品数量
        p = sheet.cell_value(i, 1)      # 订单金额
        country = sheet.cell_value(i, 13)  # 收货地址

        if id != '' and t != '' and n != '' and p != '' and country != '':  # 如果这四个值有一个都不为空值
            T = xlrd.xldate_as_tuple(t, 0)  # 时间元组
            print(T)
            if T[0] == 2017 and T[1] == 2 or T[0] == 2017 and T[1] == 3:
                if T[2] >= 10:
                    ts = '0' + str(T[1]) + str(T[2])  # ts  是时间的字符串形式 如 "0301"
                else:
                    ts = '0' + str(T[1]) + '0' + str(T[2])
            if country in Country:
                countryDict[country][days_to_counts(ts)][1] += 1
                print(n)
                countryDict[country][days_to_counts(ts)][2] += n
                countryDict[country][days_to_counts(ts)][3] += int(p)
            else:
                print('NO')
    return countryDict

def write(countryDict):
    workbook = xlwt.Workbook(encoding='utf-8')
    for key in countryDict.keys():
        data_sheet = workbook.add_sheet(str(key))
        row0 = ['时间', '订单数量', '商品数量', '订单总金额']
        for i in range(4):
            data_sheet.write(0, i, row0[i])

        ordersCount = 0
        productsCount = 0
        priceCount = 0
        for i in range(1, len(countryDict[key]) + 1):
            ordersCount += countryDict[key][i-1][1]
            productsCount += countryDict[key][i-1][2]
            priceCount += countryDict[key][i-1][3]
            data_sheet.write(i, 0, countryDict[key][i-1][0])
            data_sheet.write(i, 1, countryDict[key][i-1][1])
            data_sheet.write(i, 2, countryDict[key][i-1][2])
            data_sheet.write(i, 3, countryDict[key][i-1][3])
        # 求出每个地区最后总数量
        data_sheet.write(60, 0, "总计")
        data_sheet.write(60, 1, ordersCount)
        data_sheet.write(60, 2, productsCount)
        data_sheet.write(60, 3, priceCount)

        finalname = "D:\\python projects\\eTrace\\reModelling\\%s.xls" % "worldArea"
        workbook.save(finalname)

if __name__ == '__main__':
    countryDict = sort()
    write(countryDict)