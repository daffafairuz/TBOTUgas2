import nltk
from nltk import CFG
from nltk.parse import EarleyChartParser
from nltk.tree import Tree

grammar = CFG.fromstring(
"""
    S -> FN FK
    FK -> K FN | K FN FP | K B Penj PR B
    FP -> PR FN
    K -> "melihat" | "memakan" | "berjalan"
    FN -> "Aku" | "Dia" | "Daffa" | "Faishal" | "Adri" | Penj B | B | Penj B FP
    Penj -> "sebuah" | "seekor" | "itu" | "punyaku"
    B -> "anjing" | "kucing" | "teleskop" | "taman"
    PR -> "di" | "pada" | "oleh" | "dengan"
"""
)

parser = EarleyChartParser(grammar)

def parsing_tree(sentence):
    print(f"Parsing sentence: {' '.join(sentence)}")
    parses = list(parser.parse(sentence))
    if parses:
        for tree in parses:
            print(tree)
            tree.pretty_print()
    else:
        print("Frasa yang valid tidak ditemukan.")

sentence = ["Aku", "melihat", "kucing"]

parsing_tree(sentence)