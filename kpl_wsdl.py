from zeep import Client

class Kpl():
  def __init__(self):
    self.wsdl = "http://ws.kpl.onclick.com.br/AbacosWsPlataforma.asmx?wsdl"
    self.chave = {'ChaveIdentificacao': ''}
    self.client = Client(wsdl=self.wsdl)
    self.protocolo()
    
  def protocolo(self):
    lista_protocolos = []
    response_body = self.client.service.PedidosDisponiveis(**self.chave)
    if response_body['ResultadoOperacao']['Codigo'] == 20002:
      dados = response_body['Rows']['DadosPedidosDisponiveisWeb']
     
      for dador in dados:
        lista_protocolos.append(dado['ProtocoloPedido'])
        
      self.protocoloPedidoRecebido(lista_protocolos)

    else:
      print(response_body['ResultadoOperacao']['Codigo'])
      print(response_body['ResultadoOperacao']['Descricao'])
      
  def protocoloPedidoRecebido(self, lista_protocolos):
      with self.client.settings(strict=False):
        for lista_protocolo in lista_protocolos:
          key = {'ProtocoloPedido':lista_protocolo}
          response_body = self.client.service.ConfirmarRecebimentoPedido(**key)

Kpl()
