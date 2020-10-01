# style: 0 ; 1 ; 4 ; 7 = none ; bold; underline; negative
# text: 30; 31; 32; 33; 34; 35; 36; 37 = branco, vermelho, verde, amarelo, azul, roxo, azul claro, cinza
# background: Igual ao texto porém na quarta dezena.
# \033[0;33;44m
print('\033[1;36;40mOlá mundo!\033[m')
print('a formatação pode ser feita assim: {}{}{}'.format('\033[1;33;41m', 'variavel ou texto', '\033[m'))
