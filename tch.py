def determinar_anemia(edad, sexo, nivel_hemoglobina):
    # Definir los rangos de hemoglobina para determinar la anemia
    # Los rangos son basados en la Organización Mundial de la Salud (OMS)
    rangos_anemia = {
        'hombre': {
            'mayor_15': 13.8,
        },
        'mujer': {
            'mayor_15': 12.1,
        }
    }
    
    # Determinar si la persona tiene anemia
    if sexo.lower() == 'hombre':
        if edad > 15 and nivel_hemoglobina < rangos_anemia['hombre']['mayor_15']:
            return 'La persona tiene anemia.'
        else:
            return 'La persona no tiene anemia.'
    elif sexo.lower() == 'mujer':
        if edad > 15 and nivel_hemoglobina < rangos_anemia['mujer']['mayor_15']:
            return 'La persona tiene anemia.'
        else:
            return 'La persona no tiene anemia.'
    else:
        return 'Sexo no reconocido. Por favor ingrese "hombre" o "mujer".'

# Ejemplo de uso de la función
resultado = determinar_anemia(30, 'mujer', 11.5)
print(resultado)
