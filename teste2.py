import sys

teste = ''

while not teste == "/":
    teste = sys.stdin.read(1)
    print(teste)
