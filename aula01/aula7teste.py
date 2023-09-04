#Teste1
"""
pontos_perdidos = 11 / 3
type(pontos_perdidos)
<class 'float'>
print(pontos_perdidos)
3.6666666666666665
"""

#Teste2
"""
3 // 2
O operador // também é chamado integer division e sempre devolve o valor inteiro (sem arredondar).
"""
#Teste3
"""
def executa():
    print("Executando a")

if(__name__ == "__main__"):
    executa()
"""

"""O senso comum é que o Python é uma linguagem interpretada. Interpretado significa que não há um processo de compilação que traduz o código fonte em algum código nativo, que o seu computador entende. A documentação do Python confirma isso, no entanto também menciona a presença de um compilador:

"Python is an interpreted language, as opposed to a compiled one, though the distinction can be blurry because of the presence of the bytecode compiler."

"Python source code is automatically compiled into Python byte code by the CPython interpreter. Compiled code is usually stored in PYC (or PYO) files, and is regenerated when the source is updated, or when otherwise necessary."

"First off, interpreted/compiled is not a property of the language but a property of the implementation (...) Python is compiled. Not compiled to machine code ahead of time (i.e. "compiled" by the restricted and wrong, but also common definition), "only" compiled to bytecode"""