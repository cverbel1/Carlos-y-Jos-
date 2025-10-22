from Node import Node
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def _get_kth(self, node, k):
        while node and k > 0:
            node = node.next
            k -= 1
        return node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def append_tail(self, data):
        node = Node(data)
        if self.tail is None:  # lista vacía
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self._size += 1

    def __str__(self):
        values = []
        current = self.head
        while current:
            values.append(str(current.data))
            current = current.next
        return " -> ".join(values) + " -> None"
    
    def traverse(self):
        current = self.head
        while current:
            print(current.data, end=" -- ")
            current = current.next
        print("None")

    def _node_at(self, index):
        if index < 0 or index >= self._size:
            raise IndexError("índice fuera de rango")
        cur = self.head
        for _ in range(index):
            cur = cur.next
        return cur  
    
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        self._size += 1
    
    def pop_first(self):
        if not self.head:
            return None
        value = self.head.data
        self.head = self.head.next
        return value
    
    def is_empty(self):
        if not self.head:
            return True
        return False
    
    def pop(self):  # eliminar cola
        if self.is_empty():
            raise IndexError("lista vacía")
        if self._size == 1:
            return self.pop_first()
        prev = self._node_at(self._size - 2)
        data = prev.next.data
        prev.next = None
        self.tail = prev
        self._size -= 1
        return data
    
    def find(self, target):
        current = self.head
        index = 0
        while current:
            if current.data == target:
                return index
            current = current.next
            index += 1
        return -1

    def set(self, index, data):
        self._node_at(index).data = data
    
    def insert(self, index, data):
        if index < 0 or index > self._size:
            raise IndexError("índice fuera de rango")
        if index == 0:
            return self.prepend(data)
        if index == self._size:
            return self.append(data)
        prev = self._node_at(index - 1)
        node = Node(data, prev.next)
        prev.next = node
        self._size += 1

    def sort_asc(self):
            prev_before = None
            current = self.head.next if self.head else None
            before = self.head
            while before and before.next is not None:
                while current is not None:
                    t_before = before
                    t_current = current
                    if before.data > current.data:
                        next_before = before.next
                        before.next = current.next
                        if next_before == current: # si el siguiente de b == c
                            current.next = before
                        else:
                            current.next = next_before
                            prev_current.next = t_before
                        if prev_before is not None: # si tiene anterior b
                            prev_before.next = current
                        else:
                            self.head = current
                        current = t_before
                        before = t_current
                        print(self)
                    prev_current = current
                    current = current.next
                prev_before = before
                before = before.next
                current = before.next

    def reverse_k_group(self, k):
        if k <= 1 or not self.head:
            return
        dummy = Node(0)
        dummy.next = self.head
        prev_group = dummy
        while True:
            kth = self._get_kth(prev_group, k)
            if not kth:
                break  # no hay suficientes nodos para invertir
            group_next = kth.next
            # invertimos el grupo
            prev = kth.next
            current = prev_group.next
            while current != group_next:
                tmp = current.next
                current.next = prev
                prev = current
                current = tmp
            tmp = prev_group.next
            prev_group.next = kth
            prev_group = tmp
        self.head = dummy.next

    def oredenar_2_listas(self, other):
        if not self.head:
            return
        if not other.head:
            return
        p1 = self.head
        p2 = other.head

        if p1.data < p2.data:
            new_head = p1
            p1 = p1.next
        else:
            new_head = p2
            p2 = p2.next

        current = new_head

        while p1 and p2:
            if p1.data < p2.data:
                current.next = p1
                p1 = p1.next
            else:
                current.next = p2
                p2 = p2.next
            current = current.next

        if p1:
            current.next = p1
        else:
            current.next = p2

        self.head = new_head
        finder = self.head
        tamaño = self._size
        while finder.next:
            finder = finder.next
            self._size = self._size + 1
        self.tail = finder
        self._size = self._size - tamaño

        return self


    def primer_nodo(self, other):
        if not self.head:
            return
        if not other.head:
            return
        
        p1 = self.head
        p2 = other.head
        comp = p1
        compare = p2
        e = True
        while e and comp:
            while compare:
                if comp.data == compare.data:
                    e = False
                    return comp
                compare = compare.next
            compare = p2
            comp = comp.next

        if e:
            print("No hay interseccion")
    
    def zigzag(self):
    # Si lista vacía o tiene menos de 2 nodos después de head, no hay nada que hacer
        if not self.head or not self.head.next or not self.head.next.next:
            return self

        prev = self.head              # nodo antes del primer par (head)
        first = prev.next             # primer nodo del primer par (nodo 2)

        while first and first.next:
            second = first.next
            following = second.next   # nodo después del par

            # hacer el swap: prev -> second -> first -> following
            prev.next = second
            second.next = first
            first.next = following

            # avanzar para el siguiente par
            prev = first              # ahora el "first" quedó como el segundo del par
            first = following         # siguiente primer nodo del próximo par

        # actualizar tail (opcional, si usas self.tail en tu clase)
        tail = self.head
        while tail.next:
            tail = tail.next
        self.tail = tail

        return self
    

    def mover_nodos_final(self):

        if not self.head or not self.head.next:
            return
        current = self.head
        x = 1  
        tamaño = self._size
        tamaño = tamaño + 2
        while x != tamaño:
            if x % 2 == 1:
                aux = current
            if x % 2 == 0:
                nodo = current
                valor = current.next
                aux.next = valor
                temp = self.head
                while temp.next != None:
                    temp = temp.next
                temp.next = nodo
                nodo.next = None 
            current = aux.next
            x = x + 1
        
        return self


lista1 = SinglyLinkedList()
for n in [10,20,30,40,50]:
    lista1.append(n)

print("Lista 1:")
lista1.traverse()
print()

lista1.mover_nodos_final()
lista1.traverse()

# Crear segunda lista ordenada
# lista2 = SinglyLinkedList()
# for n in [6,7,8,4]:
#     lista2.append(n)

# print("\nLista 2:")
# lista2.traverse()

# # Fusionar ambas listas
# print("\nLista fusionada:")
# lista1.oredenar_2_listas(lista2)

# lista1.traverse()




# sll = SinglyLinkedList()
# sll.append_tail(5)
# sll.append_tail(3)
# sll.append_tail(2)
# sll.append_tail(1)
# sll.append_tail(5)
# sll.reverse_k_group(2)
# sll.traverse()


# sll.sort_asc()

#print(sll)








    

        





