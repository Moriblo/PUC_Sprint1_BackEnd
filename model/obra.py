from sqlalchemy import Column, String, Integer, DateTime, Float, UniqueConstraint
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from  model import Base

class Obra(Base):
    __tablename__ = 'obra'

    id = Column("pk_obra", Integer, primary_key=True)
    nome = Column(String(140))
    artista = Column(String(140))
    estilo = Column(String(140), unique=False)
    tipo = Column(String(140), unique=False)
    link = Column(String(140), unique=False)
    data_insercao = Column(DateTime, default=datetime.now())

    """ Definine o critério de restrição de entrada de valores repetidos para nome e artista.
        Ou seja, não poderá haver uma obra de mesmo nome para um mesmo artista. No entanto, 
        poderá haver um mesmo nome de obra para artistas diferentes.
    """
    __table_args__ = (UniqueConstraint('nome', 'artista', name='_nome_artista_uc'),)


    def __init__(self, nome:str, artista:str, estilo:str, tipo:str, link:str, 
                 data_insercao:Union[DateTime, None] = None):
        """
        Cria uma Obra

        Arguments:
            nome: nome da obra.
            artista: nome do artista que confeccionou a obra
            estilo: estilo de época da obra
            data_insercao: data de quando a obra foi inserida à base
        """
        self.nome = nome
        self.artista = artista
        self.estilo = estilo
        self.tipo = tipo
        self.link = link

        # Se não for informada, será a data exata da inserção no banco
        if data_insercao:
            self.data_insercao = data_insercao

