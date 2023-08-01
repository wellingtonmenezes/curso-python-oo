import re


class ExtratorURL:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()
    
    def __len__(self):
        return len(self.url)
    
    def __str__(self):
        return self.url
    
    def __eq__(self, otherObj):
        return self.url == otherObj.url

    def sanitiza_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ""

    def valida_url(self):
        if not self.url:
            raise ValueError("URL está vazia")
        padrao_url = re.compile(
            "(http(s)?://)?(www.)?bytebank.com(.br)?/cambio")
        match = padrao_url.match(self.url)
        if not match:
            raise ValueError("URL não é válida.")

    def get_base_url(self):
        indice_interrogacao = self.url.find("?")
        base_url = self.url[:indice_interrogacao]
        return base_url

    def get_url_paramentros(self):
        indice_interrogacao = self.url.find("?")
        url_paramentros = self.url[indice_interrogacao + 1:]
        return url_paramentros

    def get_valor_paramentro(self, paramentro_busca):
        indice_paramentro = self.get_url_paramentros().find(paramentro_busca)
        indice_valor = indice_paramentro + len(paramentro_busca) + 1
        indice_e_comercial = self.get_url_paramentros().find("&", indice_valor)
        if indice_e_comercial == -1:
            valor = self.get_url_paramentros()[indice_valor:]
        else:
            valor = self.get_url_paramentros()[indice_valor:indice_e_comercial]
        return valor


extrator_url = ExtratorURL(
    "www.bytebank.com/cambio?moedaDeOrigem=dolar&moedaDeDestino=real&valor=100")
valor = extrator_url.get_valor_paramentro("valor")
print(valor)
