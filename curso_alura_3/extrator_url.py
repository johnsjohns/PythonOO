import re
class ExtratorURL:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()

    def sanitiza_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ""

    def valida_url(self):
        if not self.url:
            raise ValueError("A URL está vazia")
        padrao_url = re.compile('(http(s)?: //)?(www.)?bytebank.com(.br)?/cambio')
        match = padrao_url.match(self.url)
        if not match:
            raise ValueError("A URL não é válida.")

    def get_url_base(self):
        indice_interrogacao = self.url.find("?")
        url_base = url[:indice_interrogacao]
        return url_base

    def get_url_paremetros(self):
        indice_interrogacao = self.url.find("?")
        url_parametros = self.url[indice_interrogacao+1:]
        return url_parametros

    def get_valor_parametro(self, parametro):
        indice_parametro = self.get_url_paremetros().find(parametro)
        indice_valor = indice_parametro + len(parametro)+1
        indice_e_comercial = self.get_url_paremetros().find('&', indice_valor)
        if indice_e_comercial == -1:
            valor = self.get_url_paremetros()[indice_valor:]
        else:
            valor = self.get_url_paremetros()[indice_valor:indice_e_comercial]
        return valor

    def __len__(self):
        return len(self.url)

    def __str__(self):
        return self.url

    def __eq__(self, other):
        return self.url == other.url

extrator = ExtratorURL("bytebank.com/cambio?quantidade=100&,moedaOrigem=real&moedaDestino=dolar")
valor_quantidade = extrator.get_valor_parametro("quantidade")
print(valor_quantidade)