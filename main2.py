import unittest
import read, copy
from logical_classes import *
from student_code import KnowledgeBase


class KBTest(unittest.TestCase):

    def setUp(self):
        # Assert starter facts
        file = 'statements_kb3.txt'
        data = read.read_tokenize(file)
        self.KB = KnowledgeBase([], [])
        for item in data:
            if isinstance(item, Fact):
                self.KB.kb_assert(item)
        print(len(self.KB.facts))

    def test1(self):
        ask1 = read.parse_input("fact: (inst Ai hero)")
        print(' Asking if', ask1)
        answer = self.KB.kb_ask(ask1)
        self.assertEqual(answer[0].bindings, [])
        # self.assertEqual(answer.list_of_bindings[0][1][0], ask1)

    def test2(self):
        ask1 = read.parse_input("fact: (friendly ?X)")
        print(' Asking if', ask1)
        answer = self.KB.kb_ask(ask1)
        self.assertEqual(str(answer[0]), "?X : Uzna")
        self.assertEqual(str(answer[1]), "?X : Hershey")
        self.assertEqual(str(answer[2]), "?X : Ai")

    def test3(self):
        ask1 = read.parse_input("fact: (inst Nosliw ?Y)")
        print(' Asking if', ask1)
        answer = self.KB.kb_ask(ask1)
        self.assertEqual(str(answer[0]), "?Y : dragon")

    def test4(self):
        ask1 = read.parse_input("fact: (attacks-with ?X ?Y sword)")
        print(' Asking if', ask1)
        answer = self.KB.kb_ask(ask1)
        self.assertEqual(str(answer[0]), "?X : Ai, ?Y : Nosliw")



if __name__ == '__main__':
    unittest.main()
