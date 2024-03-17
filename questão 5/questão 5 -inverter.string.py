def inverter(s):
    inverted = "" #armazenar string invertida
    indice = 0
    while s[indice:]:  
        indice = indice + 1 # Neste trecho, você usa um loop while para percorrer a string s a partir do índice até o final. Isso serve para encontrar o tamanho da string.
    indice = indice- 1  # Depois de encontrar o tamanho da string, você decrementa o valor de indice em 1 para obter o índice do último caractere válido na string.
    while indice >= 0:
        inverted = inverted + s[indice]
        indice = indice - 1 #Este é o loop principal que inverte os caracteres da string. Enquanto o indice for maior ou igual a 0 (ou seja, enquanto houver caracteres na string original para percorrer), o loop continuará executando. Em cada iteração do loop, o caractere na posição indice da string original s é adicionado à string invertida inverted. Em seguida, o indice é decrementado em 1 para passar para o próximo caractere da direita para a esquerda.
    return inverted #retorna a string invertida.

string = "teste"
print("String invertida:", inverter(string))