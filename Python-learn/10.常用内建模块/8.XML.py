"""
    操作XML有两种方法
        - DOM:把整个XML读入内存，解析为树，因此占用内存大，解析慢，但可以任意遍历树的节点
        - SAX:流模式，边读边解析，占用内存小，解析快，缺点是需要自己处理事件
    正常情况下，优先考虑SAX，因为DOM实在实在太占内存
"""
"""
在Python中使用SAX解析XML非常简洁，通常我们关心的事件是start_element，end_element和char_data，准备好这3个函数，然后就可以解析xml了。

举个例子，当SAX解析器读到一个节点时：

<a href="/">python</a>
会产生3个事件：

start_element事件，在读取<a href="/">时；

char_data事件，在读取python时；

end_element事件，在读取</a>时。
"""
from xml.parsers.expat import ParserCreate

class DefaultSaxHandler(object):
    def start_elment(self, name, attrs):
        print('sax:start_element: %s, attrs: %s' %(name, str(attrs)))

    def end_element(self, name):
        print('sax:end_element: %s' % name)

    def char_data(self, text):
        print('sax:char_data: %s' % text)

xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li> 
<ol>
'''

handler = DefaultSaxHandler()
parser = ParserCreate()
parser.StartElementHandler = handler.start_elment
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data
parser.Parse(xml)

# 生成简单的XML的方法是拼接字符串
""" 如果要生成复杂 的XML呢？建议你不要用XML，改成JSON """

"""
   解析XML时，注意找出自己感兴趣的节点，响应事件时，把节点数据保存起来。
   解析完毕后，就可以处理数据。
"""

# Exercise
from datetime import datetime, timedelta


class WeatherSaxHandler(object):
    def __init__(self):
        self.today = datetime.now().strftime('%a')
        self.tomorrow = ((datetime.now() + timedelta(days=1)).strftime('%a'))
        self._data = {
            'city:': '',
            'country': '',
            'today': {
                'text': '',
                'low': 0,
                'high': 0
            },
            'tomorrow': {
                'text': '',
                'low': 0,
                'high': 0
            }

        }


    @property
    def get_data(self):
        return self._data

    def start_element(self, name, attrs):
        if name == 'yweather:location':
           self._data['city'] = attrs['city']
           self.__data['country'] = attrs['country']
        if name == 'yweather:forecast':
            if attrs['day'] == self.today:
                self.__data['today']['text'] = attrs['text']
                self.__data['today']['low'] = attrs['low']
                self.__data['today']['high'] = attrs['high']
            if attrs['day'] == self.tomorrow:
                self.__data['tomorrow']['text'] = attrs['text']
                self.__data['tomorrow']['low'] = attrs['low']
                self.__data['tomorrow']['high'] = attrs['high']

    def end_element(self, name, attrs):
        pass

    def char_data(self, text):
        pass


data = 'your data'

handler = WeatherSaxHandler()
parser = ParserCreate()
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data
parser.Parse(data)

print(handler.get_data)