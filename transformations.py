import numpy as np


def translation(coords: list, tx: int, ty: int) -> list:
    """
    Translada uma figura geométrica para outro lugar do espaço

    Argumentos:
        coords = lista de coordenadas (representadas por tuplas pares) da figura a ser translada
        tx = fator de translação para x, que indica quantas unidades a figura deve se mover no eixo das abscissas
        ty = fator de translação para y, que indica quantas unidades a figura deve se mover no eixo das ordenadas

    Retorno:
        new_coords = uma lista que contém as novas coordenadas da figura após a translação (em tuplas)

    A função opera realizando uma soma dos fatores de translação para cada vértice da figura
    """

    return [(c[0] + tx, c[1] + ty) for c in coords]


def scale(coords: list, sx: int, sy: int) ->list:
    """
    Escala uma figura para que ela fique maior ou menor, pode também alterar suas medidas

    Argumentos:
        coords = lista de coordenadas (representadas por tuplas pares) da figura a ser escalada
        sx = fator de escala para x, que indica o quanto a figura deve ser escalada nas abscissas
        sy = fator de escala para y, que indica o quanto a figura deve ser escalada nas ordenadas

    Retorno:
        new_coords = uma lista que contém as novas coordenadas da figura após a escala (em tuplas)

    Opera multiplicando cada coordenada dos vértices da figura pelos fatores de escala
    """

    return [(c[0] * sx, c[1] * sy) for c in coords]


def rotation(coords: list, angle: float, pivot: tuple = (0,0)) -> list:
    """
    Rotaciona uma figura geométrica em torno de um ponto específico ou um de seus vértices

    Argumentos:
        coords = lista de coordenadas (representadas por tuplas pares) da figura a ser rotacionada
        angle = um número ponto flutuante que representa a angulação da rotação da figura (em graus)
        pivot = o ponto de referência para a rotação da figura (padronizada na origem)

    Retorno:
        new_coords = uma lista que contém as novas coordenadas da figura após a rotação (em tuplas)

    Para funcionar, o ângulo é convertido de graus para radianos e é feita a verificação da posição do pivô
    (se ele está dentro ou fora da figura), e para cada vértice da figura as coordenadas do pivô são subtraídas
    em uma translação, para então esses valores translados serem multiplicados pela matriz de rotação R. Após mais
    uma translação que soma os valores obtidos da multiplicação com o pivô obtém-se as coordenadas finais
    """

    new_coords = []
    r = np.radians(angle)
    try:
        coords.remove(pivot)
    except ValueError:
        pass

    R = np.array([[np.cos(r), -np.sin(r)],
                      [np.sin(r), np.cos(r)]])

    for c in coords:
        translated = np.array((c[0] - pivot[0], c[1] - pivot[1]))
        rotated = tuple(R @ translated)
        new_c = (rotated[0] + pivot[0], rotated[1] + pivot[1])
        new_coords.append(new_c)

    return new_coords
