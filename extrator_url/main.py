url = "bytebank.com/cambio?moedaDeOrigem=dolar&moedaDeDestino=real&valor=100"

url = url.strip()

if url == "":
    raise ValueError("URL está vazia")

indice_interrogacao = url.find("?")
base_url = url[:indice_interrogacao]

url_paramentros = url[indice_interrogacao+1:]
print(url_paramentros)

paramentro_busca = "valor"
indice_paramentro = url_paramentros.find(paramentro_busca)
indice_valor = indice_paramentro + len(paramentro_busca) + 1
indice_e_comercial = url_paramentros.find("&", indice_valor)

if indice_e_comercial == -1:
    valor = url_paramentros[indice_valor:]
else:
    valor = url_paramentros[indice_valor:indice_e_comercial]

print(valor)
