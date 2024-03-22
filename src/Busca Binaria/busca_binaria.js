function buscaBinaria(lista, item) {
    let baixo = 0;
    let alto = lista.length - 1;

        while (baixo <= alto) {
            let meio;
            let chute;
            meio = parseInt((baixo + alto) / 2)
            chute = lista[meio];
    
            if (chute === item) {
                return meio
            } else if (chute > item) {
                console.log(`O Chute ${chute} é maior que o item ${item}`)
                alto = meio - 1;
            } else if (chute < item) {
                console.log(`O Chute ${chute} é menor que o Item ${item}`)
                baixo = meio + 1;
            }
        }
        console.log(`O Chute não está na Lista [${lista}], e o Índice do Item ${item} seria o Índice ${baixo}`)
        return 'Indice: ' + baixo
    }
    
    let lista = [1,3,5,6]
    console.log(buscaBinaria(lista, 6))
