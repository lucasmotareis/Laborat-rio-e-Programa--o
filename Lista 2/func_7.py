def converterSegundos(segundos):
    horas = segundos // 3600
    segundos = segundos%3600
    minutos = segundos // 60
    segundos = segundos%60
    segundo = segundos
    # str(horas)
    # str(minutos)
    # str(segundos)
    return f"{horas}:{minutos}:{segundo}"

segundos = int(input("Digite os segundos para serem transformados: "))
print(converterSegundos(segundos))