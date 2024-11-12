def resolver_ec(a, b, c):
    """
    Resuelve una ecuación lineal de la forma ax + b = c.
    
    Args:
        a (float): Coeficiente de x.
        b (float): Término independiente.
        c (float): Término constante.
        
    Returns:
        float: La solución para x.
    """
    x = (c - b) / a
    return x

def main():
    x = resolver_ec(2, 3, 7)  # Aquí puedes cambiar los valores de a, b y c según lo necesites
    print("El valor de 'x' es:", x)

if __name__ == "__main__":
    main()


