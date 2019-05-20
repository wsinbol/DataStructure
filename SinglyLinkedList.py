#-*-coding:utf-8-*-

class Node(object):

    def __init__(self, data, next_node=None):
        self.data = data
        self._next = next_node

class SinglyLinkedList(object):

    def __init__(self):
        self._head = None

    def insert_node_to_head(self, new_node):
        if new_node:
            new_node._next = self._head
            self._head = new_node

    def find_by_index(self, index):
        p = self._head 
        position = 0
        while p and position != index:
            p = p._next
            position += 1
        return p

    def find_by_value(self, value):
        p = self._head
        while p and p.data != value:
            p = p._next
        return p

    def insert_value_to_head(self, value):
        new_node = Node(value)
        self.insert_node_to_head(new_node)

    def insert_value_after(self, node, value):
        new_node = Node(value)
        self.insert_node_after(node, new_node)

    def insert_node_after(self, node, new_node):
        new_node._next = node._next
        node._next = new_node

    def delete_by_value(self, value):
        current_p = self._head
        next_p = current_p._next
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

    # 删除给定节点的后继节点
    def delete_next_node_after_target(self, node):
        if node._next == None:
            return 
        else:
            node._next = node._next._next

    # 删除当前节点
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

if __name__ == '__main__':
    l = SinglyLinkedList()
    for i in range(2):
        l.insert_value_to_head(i)
    # node3 = l.find_by_value(1)
    # print(node3.data)
    # l.insert_value_after(node3, 10)
    l.print_all()
    print()
    # print(l.find_by_value(0)
    # l.delete_by_node(l.find_by_value(1))
    l.delete_current_node(l.find_by_value(1))
    l.print_all()
    # l.delete_by_value(4)
    # print()
    # l.print_all()



