

class TransformaData:
    """Transforma o formato das datas."""

    def dataExtensoBr(self, data):
        """Pega uma data e a retorna por extenso."""
        self.meses = [
                'Janeiro',
                'Fevereiro',
                'Março',
                'Abril',
                'Maio',
                'Junho',
                'Julho',
                'Agosto',
                'Setembro',              
                'Outubro',
                'Novembro',
                'Dezembro',
            ]
        self.data = data
        self.dia, self.mes, self.ano = self.data.split('-')
        return f'{self.dia}_de_{self.meses[int(self.mes)-1]}'