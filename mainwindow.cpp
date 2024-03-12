#include "mainwindow.h"
#include "ui_mainwindow.h"

MainWindow::MainWindow(QWidget* parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    connect(ui->comboBox, SIGNAL(currentIndexChanged(int)), this, SLOT(changeLanguage(int)));\

   p1 = new QPushButton(tr("huhuhu"),this);
    p1->move(130,30);

    p2 = new QPushButton(tr("hujintao"),this);
     p2->move(130,70);
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::changeLanguage(int index)
{


    qDebug() << "1 ";
    bool loaded = false;
    qDebug() << index;
    switch (index) {
    case 0:  // 中文
    {

        qDebug() << "English";
        loaded = translator.load(":zh.qm");

        qDebug() << "Translation file loaded:" << loaded;
        break;
    }
    case 1:  // English
    translator.load(":en.qm");
    break;

    case 2:  // English
    translator.load(":jp.qm");
    break;

    default:
    break;
    }
    qApp->installTranslator(&translator);
    ui->retranslateUi(this); // 刷新UI

    QFontMetrics metrics(ui->label->font());
    int width = metrics.horizontalAdvance(ui->label->text());  // 计算文本的宽度
    ui->label->setMinimumWidth(width);  // 设置控件的最小宽度
    qDebug() <<"label setMinimumWidth" << width;
    QString a = "huhuhu";
    p1->setText(tr(a.toUtf8().data()));
    QString b = "hujintao";
    p2->setText(tr(b.toUtf8().data()));

}
