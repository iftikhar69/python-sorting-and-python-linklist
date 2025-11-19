"""Non-interactive demo runner that exercises each DS implementation with asserts."""
from stack_array import StackArray
from stack_linked import StackLinked
from queue_array import QueueArray
from queue_linked import QueueLinked
from hashtable_array import HashTableArray
from hashtable_linked import HashTableLinked
from hashset_array import HashSetArray
from hashset_linked import HashSetLinked
from hashmap_array import HashMapArray
from hashmap_linked import HashMapLinked


def run_all():
    # Stack
    sa = StackArray()
    sa.push(1); sa.push(2)
    assert sa.pop() == 2
    sl = StackLinked()
    sl.push('x'); sl.push('y')
    assert sl.pop() == 'y'

    # Queue
    qa = QueueArray(4)
    qa.enqueue(5); qa.enqueue(6)
    assert qa.dequeue() == 5
    ql = QueueLinked()
    ql.enqueue('a'); ql.enqueue('b')
    assert ql.dequeue() == 'a'

    # Hash table
    ha = HashTableArray()
    ha.put('kk', 11)
    assert ha.get('kk') == 11
    assert ha.remove('kk')
    hl = HashTableLinked()
    hl.put(1, 'one')
    assert hl.get(1) == 'one'

    # Hash set
    hs_a = HashSetArray()
    hs_a.add(9)
    assert hs_a.contains(9)
    hs_l = HashSetLinked()
    hs_l.add('z')
    assert hs_l.contains('z')

    # Hash map
    hm_a = HashMapArray()
    hm_a.put('u', 100)
    assert hm_a.get('u') == 100
    hm_l = HashMapLinked()
    hm_l.put('k', 'v')
    assert hm_l.get('k') == 'v'

    print('All quick assertions passed.')


if __name__ == '__main__':
    run_all()
