#-*-coding:utf-8-*-

'''
单链表
'''

class Node(object):

    def __init__(self, data, next_node=None):
        self.data = data
        self._next = next_node

class SinglyLinkedList(object):

    def __init__(self):
        self._head = None

    # 将待添加的值实例化成Node类
    def change_value_to_node(self, value):
        new_node = Node(value)
        self.insert_node_to_head(new_node)

    # 将新结点插入到最前面
    def insert_node_to_head(self, new_node):
        if new_node:
            new_node._next = self._head
            self._head = new_node

    # 根据索引查找结点信息
    def find_by_index(self, index):
        p = self._head 
        position = 0
        while p and position != index:
            p = p._next
            position += 1
        return p

    # 根据值查找结点信息
    def find_by_value(self, value):
        p = self._head
        while p and p.data != value:
            p = p._next
        return p

    # 在给定结点后插入值
    def insert_value_after(self, node, value):
        new_node = Node(value)
        self.insert_node_after(node, new_node)

    # 在给定结点后插入新结点
    def insert_node_after(self, node, new_node):
        new_node._next = node._next
        node._next = new_node

    # 删除等于给定值的结点
    def delete_by_value(self, value):
        current_p = self._head
        next_p = current_p._next
        # 处理当给定值是第一个结点的情况
        if current_p and current_p.data == value:
            self._head = next_p
            return
        
        while next_p and next_p.data != value:
            current_p = current_p._next
            next_p = current_p._next
        # return current_p
        if next_p:
            current_p._next = current_p._next._next
        else:
            return

    # 删除给定结点的前驱结点
    def delete_prev_node_before_target(self, node):
        current_node = self._head
        if current_node == node:
            return 

        next_node = current_node._next
        next_2_node = current_node._next._next
        if next_node == node:
            self._head = next_node

        while next_2_node and next_2_node != node:
            current_node = current_node._next
            # next_node = current_node._next
            next_2_node = current_node._next._next

        if next_2_node:
            current_node._next = next_2_node
        else:
            return



    # 删除给定结点的后继结点
    def delete_next_node_after_target(self, node):
        if node._next == None:
            return 
        else:
            node._next = node._next._next

    # 删除当前结点
    def delete_current_node(self, node):
        p = self._head
        if p == node:
            self._head = p._next
        while p and p._next == node:
            p._next = p._next._next
            
    def print_all(self):
        current = self._head
        if current:
            print(f"{current.data}", end="")
            current = current._next
        while current:
            print(f"->{current.data}", end="")
            current = current._next
            
    # 删除链表中倒数第 n 个节点
    def delete_last_n_node(self, n):
        print('\nexecute delete_last_%s_node method:' % n)
        slow = self._head
        fast = self._head
        
        step = 0
        while step < n:
            fast = fast._next
            step += 1
            
        while fast._next != None:
            fast = fast._next
            slow = slow._next
            
        slow._next = slow._next._next
        

if __name__ == '__main__':
    l = SinglyLinkedList()
    for i in range(5):
        l.change_value_to_node(i)
    l.print_all()
    l.delete_last_n_node(2)
    l.print_all()
    exit()
    delete_node = l.find_by_value(4)
    print(delete_node.data)
    exit()
    # l.insert_value_after(node3, 10)
    # l.print_all()
    print()
    exit()
    l.delete_prev_node_before_target(delete_node)
    # l.delete_current_node(l.find_by_value(1))
    l.print_all()
    # l.delete_by_value(4)
    # print()
    # l.print_all()



