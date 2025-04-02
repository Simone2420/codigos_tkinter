class Color:
    RESET = "\033[0m"
    NEGRITA = "\033[1m"
    SUBRAYADO = "\033[4m"

    # Colores de texto
    NEGRO = "\033[30m"
    ROJO = "\033[31m"
    VERDE = "\033[32m"
    AMARILLO = "\033[33m"
    AZUL = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    BLANCO = "\033[37m"

    # Colores de fondo
    FONDO_NEGRO = "\033[40m"
    FONDO_ROJO = "\033[41m"
    FONDO_VERDE = "\033[42m"
    FONDO_AMARILLO = "\033[43m"
    FONDO_AZUL = "\033[44m"
    FONDO_MAGENTA = "\033[45m"
    FONDO_CYAN = "\033[46m"
    FONDO_BLANCO = "\033[47m"
def mensaje_con_estilo(texto, color, fondo=None, negrita=False, subrayado=False):
    """Aplica estilos a un mensaje de texto."""
    estilo = ""
    if negrita:
        estilo += Color.NEGRITA
    if subrayado:
        estilo += Color.SUBRAYADO
    if fondo:
        estilo += fondo
    estilo += color
    return f"{estilo}{texto}{Color.RESET}"