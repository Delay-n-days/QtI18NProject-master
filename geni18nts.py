# 我的表格如下，这是一个通过excel生成翻译文件.ts的表 的需求，请使用python实现
#
# en	zh	jp
# hujintao	胡金涛	hujintao_jp
# huhuhu	呼呼呼	huhuhu_jp
# 使用xlwing库操作excel 读取数据
# 1.第一行表头的数据为生成的翻译文件的文件名，例如 en.ts zh.ts jp.ts 有多少列就生成多少个文件
# 2.下面的数据为翻译文件的context 原文使用en列的数据，每个翻译文件的译文使用表格中对应的列的数据
# 例如 en列的数据为 hujintao 那么zh列的数据为 胡金涛 jp列的数据为 hujintao_jp
# 生成模版为
# <?xml version="1.0" encoding="utf-8"?>
# <!DOCTYPE TS>
# <TS version="2.1" language="ja_JP">
# <context>
#     <message>
#         <source>huhuhu</source>
#         <translation type="unfinished">テキストラベル2</translation>
#     </message>
# </context>
# </TS>
# 及 在<context> 块中往下写 使用jinja2模版
import xlwings as xw
from jinja2 import Environment, FileSystemLoader
import subprocess
# 打开Excel文件并读取数据
xlsxApp = xw.App(visible=True, add_book=False)
xlsxApp.display_alerts = False
xlsxApp.screen_updating = False
wb = xlsxApp.books.open("翻译源文件.xlsx")
sheet = wb.sheets[0]
data = sheet.range("A1").options(expand="table").value

# 读取第一行的数据作为文件名
file_names = data[0]

# 读取剩余的数据作为文件内容
contents = data[1:]

# 设置jinja2模板环境
env = Environment(loader=FileSystemLoader("./"))

# 对于每一列数据，生成一个.ts文件
for i, file_name in enumerate(file_names):
    # 加载模板
    template = env.get_template("template.ts")

    # 生成文件内容
    file_content = template.render(contents=[(content[0], content[i]) for content in contents])

    # 写入文件
    with open(f"{file_name}.ts", "w", encoding="utf-8") as f:
        f.write(file_content)

# 关闭Excel
wb.save()
wb.close()
xlsxApp.quit()
# 执行 cmd 命令 "E:\qt\qtEnv\sqlite3\aaa\bin\lrelease.exe D:/downloads/QtI18NProject-master/QtI18NProject-master/QtI18NProject.pro"
subprocess.run(r'"E:\qt\qtEnv\sqlite3\aaa\bin\lrelease.exe" "QtI18NProject.pro"', shell=True)