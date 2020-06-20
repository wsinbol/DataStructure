'''
@Description: 模拟浏览器前进后退功能
@Date: 2020-06-20 17:15:48
@Author: Wong Symbol
@LastEditors: Wong Symbol
@LastEditTime: 2020-06-20 17:43:37
'''

'''
我们使用两个栈，X 和 Y，
我们把首次浏览的页面依次压入栈 X，
当点击后退按钮时，再依次从栈 X 中出栈，并将出栈的数据依次放入栈 Y。
当我们点击前进按钮时，我们依次从栈 Y 中取出数据，放入栈 X 中。
当栈 X 中没有数据时，那就说明没有页面可以继续后退浏览了。
当栈 Y 中没有数据，那就说明没有页面可以点击前进按钮浏览了。
'''

import sys
sys.path.append('LinkedStack.py')

from LinkedStack import LinkedStack as stack

class Browser():
    def __init__(self):
        self._forward_stack = stack()
        self._back_stack = stack()
        
    def open(self, url=''):
        self._forward_stack.push(url)

    def back(self):
        cur = self._forward_stack.pop()
        self._back_stack.push(cur)

    def forward(self):
        cur = self._back_stack.pop()
        self._forward_stack.push(cur)
        
    def show(self):
        print('_forward_stack:\n',end="")
        self._forward_stack.print()
        print('\n_back_stack:',end="")
        self._back_stack.print()
        print('\nshow ending...')

if __name__ == '__main__':
    b = Browser()
    b.open('http://www.baidu.com')
    b.open('http://www.google.com')
    b.show()
    
    b.back()
    b.back()
    b.show()

