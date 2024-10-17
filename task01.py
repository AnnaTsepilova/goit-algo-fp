# Вузол однозв'язного списку
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # 1. Функція для реверсування однозв'язного списку
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    # 2. Функція для сортування вставками
    def insertion_sort(self):
        sorted_list = None
        current = self.head
        while current:
            next_node = current.next
            sorted_list = self.sorted_insert(sorted_list, current)
            current = next_node
        self.head = sorted_list

    def sorted_insert(self, head_ref, new_node):
        current = head_ref
        if not head_ref or head_ref.data >= new_node.data:
            new_node.next = head_ref
            head_ref = new_node
        else:
            while current.next and current.next.data < new_node.data:
                current = current.next
            new_node.next = current.next
            current.next = new_node
        return head_ref

    # 3. Функція для об'єднання двох відсортованих списків
    def merge_sorted_lists(self, l1, l2):
        dummy = Node(0)
        tail = dummy
        while l1 and l2:
            if l1.data < l2.data:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        tail.next = l1 or l2
        return dummy.next

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print(None)


# Приклад використання
linked_list = LinkedList()
linked_list.push(10)
linked_list.push(20)
linked_list.push(30)
print("Original list:")
linked_list.print_list()

linked_list.reverse()
print("Reversed list:")
linked_list.print_list()

linked_list.insertion_sort()
print("Sorted list:")
linked_list.print_list()

# Об'єднання двох відсортованих списків
list1 = LinkedList()
list1.push(10)
list1.push(30)
list1.push(50)

list2 = LinkedList()
list2.push(20)
list2.push(40)
list2.push(60)

merged_list = LinkedList()
merged_list.head = merged_list.merge_sorted_lists(list1.head, list2.head)
print("Merged sorted list:")
merged_list.print_list()
