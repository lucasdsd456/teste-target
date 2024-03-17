
def pertence_fibonacci(n): #Função que gera a sequência e verifica se o número digitado pertence a ela.

    primeiro_n_seq = 0 #primeiro número da sequência
    segundo_n_seq = 1 #segundo número da sequência
    temp=0            #variavel temporária que vou utilizar para formar a sequência
    while primeiro_n_seq < n: # Inicia um loop while que vai continuar enquanto o primeiro_n_seq for menor que o número digitado pelo usuário.
        temp=primeiro_n_seq #Aqui, armazenamos temporariamente o valor de primeiro_n_seq em uma variável chamada temp. Isso é necessário porque, na próxima linha, vamos atualizar o valor de primeiro_n_seq com o valor de segundo_n_seq, e precisamos preservar o valor original de primeiro_n_seq para calcular o próximo número da sequência.
        primeiro_n_seq=segundo_n_seq #Agora, atualizamos o valor de primeiro_n_seq para ser igual ao valor atual de segundo_n_seq. Isso é feito porque, na sequência de Fibonacci, o próximo número é sempre a soma dos dois números anteriores, então o valor atual de segundo_n_seq se torna o próximo primeiro_n_seq.
        segundo_n_seq=temp+segundo_n_seq #Aqui, atualizamos o valor de segundo_n_seq para ser a soma do valor original de primeiro_n_seq (armazenado em temp) com o valor atual de segundo_n_seq. Isso calcula o próximo número da sequência de Fibonacci, onde segundo_n_seq se torna o próximo número na sequência.
    print(primeiro_n_seq == n) #Verifica se o número "n" pertence à sequência de Fibonacci até o ponto em que o primeiro número da sequência é igual ou ultrapassa "n". Se for verdadeiro, então o número pertence à sequência e retorna true; caso contrário, ele não pertence à sequência e retorna false.


numero = int(input("Informe um número: "))
pertence_fibonacci(numero)