import time

class Node:
    def __init__(self, key, val, timestamp, prev=None, next=None):
        self.key = key
        self.val = val
        self.timestamp = timestamp
        self.prev = prev
        self.next = next

class WindowedAverage:
    def __init__(self, expiration_ms):
        self.expiration_ms = expiration_ms
        self.head = Node(None, None, None)
        self.tail = Node(None, None, None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.records = {}
    
    def _add_node(self, node):
        self.tail.prev.next = node
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev = node
    
    # Only remoe non-head and non-tail nodes
    def _remove_node(self, node):
        pre, nxt = node.prev, node.next
        pre.next = nxt
        nxt.prev = pre
        print("remove node: ", node.key, node.val, node.timestamp)
    
    def add_record(self, key, val):
        node = Node(key, val, time.time())
        self._add_node(node)
        self.records[key] = node

    def _prune_expired_entries(self):
        current_time = time.time()
        while self.head.next != self.tail:
            cur = self.head.next
            if (current_time - cur.timestamp)*1000 > self.expiration_ms:
                self._remove_node(cur)
                del self.records[cur.key]
            else:
                break
    
    def get(self, key):
        self._prune_expired_entries()
        if key not in self.records:
            return None
        return self.records[key].val
    
    def get_average(self):
        self._prune_expired_entries()
        total = 0
        cnt = 0
        node = self.head.next
        while(node != self.tail):
            total += node.val
            cnt += 1
            node = node.next
        return total / cnt if cnt > 0 else 0
    
# Write a main function to test your code
if __name__ == "__main__":
    windowed_average = WindowedAverage(1000)
    windowed_average.add_record("a", 1)
    windowed_average.add_record("b", 2)
    windowed_average.add_record("c", 3)
    windowed_average.add_record("d", 4)
    windowed_average.add_record("e", 5)
    windowed_average.add_record("f", 6)
    windowed_average.add_record("g", 7)
    windowed_average.add_record("h", 8)
    windowed_average.add_record("i", 9)
    windowed_average.add_record("j", 10)
    windowed_average.add_record("k", 11)
    windowed_average.add_record("l", 12)
    windowed_average.add_record("m", 13)
    windowed_average.add_record("n", 14)
    windowed_average.add_record("o", 15)
    windowed_average.add_record("p", 16)
    windowed_average.add_record("q", 17)
    windowed_average.add_record("r", 18)
    windowed_average.add_record("s", 19)
    windowed_average.add_record("t", 20)
    windowed_average.add_record("u", 21)
    windowed_average.add_record("v", 22)
    windowed_average.add_record("w", 23)
    windowed_average.add_record("x", 24)
    windowed_average.add_record("y", 25)
    windowed_average.add_record("z", 26)
    print(windowed_average.get_average())
    time.sleep(5)
    print(windowed_average.get_average())

    

    