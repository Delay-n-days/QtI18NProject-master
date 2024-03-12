<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE TS>
<TS version="2.1" language="ja_JP">
<context>
    <name>MainWindow</name>
    {% for content in contents %}
    <message>
        <source>{{ content[0] }}</source>
        <translation type="unfinished">{{ content[1] }}</translation>
    </message>
    {% endfor %}
</context>
</TS>