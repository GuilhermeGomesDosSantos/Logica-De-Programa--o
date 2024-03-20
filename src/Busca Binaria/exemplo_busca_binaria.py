def pesquisa_binaria(lista, item): # lista é a lista ordenada, e item é o elemento que você deseja
    baixo = 0 # representa o indice mais baixo da lista posição 0
    alto = len(lista) - 1 # retorna o tamanho total da lista
    while baixo <= alto:
        meio = (baixo + alto) / 2 # pega o meio do indice, ex: baix: 0 e alto: 5 -1, meio = 4.0
        meio = int (meio)
        chute = lista[meio] # chute vai receber o valor do indice do meio da lista que nesse caso o indice é: 2 e o valor é: 5
        if chute == item: # chute for igual ao valor do item então encontrou o dado e finaliza
            return meio
        elif chute > item: # se o chute for maior do que o valor do item, então vai subtrair uma posição do indice da lista, atualmente o chute está no indice 2 da lista, então 2 - 1, alto agora passa a ter o indice 1
            alto = meio - 1 # e vai voltar para a etapa de cima, o while
        else:
            baixo = meio + 1
            # nesse caso, meio é igual a 0, então vai passar pelo else, aonde baixo vai passar a ser 1
            # e logo em seguida, o meio vai ser igual a 1, e assim chute é igual a lista que é o indice 1
    return None
    
minha_lista = [1, 3, 5, 7, 9]
print(pesquisa_binaria(minha_lista, 3))