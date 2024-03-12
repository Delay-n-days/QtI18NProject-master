
@echo off
git add . 
git commit -m "jmq"
echo 1 >> "D:\downloads\QtI18NProject-master\QtI18NProject-master\main.cpp"
echo 1 >> "D:\downloads\QtI18NProject-master\QtI18NProject-master\mainwindow.cpp"
echo 1 >> "D:\downloads\QtI18NProject-master\QtI18NProject-master\mainwindow.h"
echo 1 >> "D:\downloads\QtI18NProject-master\QtI18NProject-master\·­ÒëÔ´ÎÄ¼ş.xlsx"

git reset --hard HEAD
echo "success!"
del a.cmd