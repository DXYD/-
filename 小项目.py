from bs4 import BeautifulSoup
import requests
import xlwt
import re
from urllib.parse import quote  # 中文转乱码


def pages_(page):
    pages = 0
    pages += page * 20 - 20
    return pages


def fiction_page(url, data):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, features='lxml')
    soup_1 = soup.select("a[title]")
    for x in soup_1:
        s_s = x["title"]
        data.append(s_s)
    return data


def save_fiction(save, page):
    #    with open("爬取文件","w",encoding ="utf-8" ) as f:
    #  s_s=' '.join(s["title"])
    # print(s_s)
    book = xlwt.Workbook(encoding="utf-8", style_compression=0)  # 创建workbook对象
    sheet = book.add_sheet('爬取书籍', cell_overwrite_ok=True)  # 创建工作表
    for i in range(0, int(page) * 20):
        data_20 = save[i]
        sheet.write(i, 0, data_20)
    book.save('爬取的书籍.xls')

def main():
    tag = input("请输入你想输入的标签：")
    page = input("请输入要下载前几页的内容：")
    data = []
    for i in range(int(page)):
        pages_s = pages_(i + 1)
        #     # tags = quote(tag,encoding ='GBK' )
        url = 'https://book.douban.com/tag/' + tag + '?start=' + str(pages_s) + '&type=T'
        print("第%d页下载中" % (i + 1))
        save = fiction_page(url, data)
    save_fiction(save, page)
    print("保存成功！")


if __name__ == '__main__':
    main()
