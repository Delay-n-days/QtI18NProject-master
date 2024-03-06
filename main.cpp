#include "mainwindow.h"

#include <QApplication>
#include <QLocale>
#include <qtranslator.h>
#include <QDebug>
    QTranslator translate;
int main(int argc, char *argv[])
{
    QApplication a(argc, argv);


    QString name = QLocale::system().name();
    qDebug() << "locale language is " << name << endl;

    if (name == "ja_JP")
    {
        translate.load(":jp.qm");
    }
    else if (name == "zh_CN")
    {
        translate.load(":zh.qm");
    }

    a.installTranslator(&translate);

    MainWindow w;

    
    w.show();
    return a.exec();
}
