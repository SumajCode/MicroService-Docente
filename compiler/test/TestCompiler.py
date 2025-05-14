from ...compiler.hooks.Compiler import Compilador

compilador = Compilador()
compilador.Compilar('''
def imprimir():
    print('hola')
imprimir(
''',"python")