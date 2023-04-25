from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect, request
from urllib.parse import unquote

from sqlalchemy.exc import IntegrityError

from model import Session, Obra
from logger import logger
from schemas import *
from flask_cors import CORS

info = Info(title="Obras de Arte", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# Definindo tags
home_tag = Tag(name="Documentação", description="Documentação via Swagger.")
obra_tag = Tag(name="Obra", description="Adição, visualização e remoção de obras da base")

# ========================================================================================
""" Rota /openapi para geração da documentação via Swagger
"""
# ========================================================================================
@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi/swagger.
    """
    return redirect('/openapi/swagger')

# ========================================================================================
""" Rota /obra para tratar o fetch de `POST` do script.js.
"""
# ========================================================================================
@app.post('/obra', tags=[obra_tag],
          responses={"200": ObraViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_obra(form: ObraSchema):
    """Adiciona uma nova obra à base de dados.
    """
    obra = Obra(
        nome=form.nome,
        artista=form.artista,
        estilo=form.estilo,
        tipo=form.tipo,
        link=form.link)
    
    logger.debug(f"Adicionando obra de nome: '{obra.nome}' e artista '{obra.artista}'")
    
    try:
        # Criando conexão com a base
        session = Session()
        # Adicionando obra
        session.add(obra)
        # Efetivando o comando de adição de novo item na tabela
        session.commit()
        
        logger.debug(f"Adicionada obra de nome: '{obra.nome}' e artista '{obra.artista}'")
        
        return apresenta_obra(obra), 200

    except IntegrityError as e:
        """ A duplicidade é verificada pela obra e pelo artista. Vide "UniqueConstraint"
            no model.obra.py.
        """
        error_msg = "Obra de mesmo nome já salva na base para este artista :/"
        logger.warning(f"Erro ao adicionar obra '{obra.nome}' e artista '{obra.artista}'. {error_msg}")
        return {"mesage": error_msg}, 409

    except Exception as e:
        # Caso um erro fora do previsto
        error_msg = "Não foi possível salvar nova obra :/"
        logger.warning(f"Erro: {error_msg}")
        return {"mesage": error_msg}, 400

    # Comando de fechamento da sessão.
    finally:
        session.close()

# ========================================================================================
""" Rota /obras para tratar o fetch de `GET` do script.js para função getList().
"""
# ========================================================================================
@app.get('/obras', tags=[obra_tag],
         responses={"200": ListagemObrasSchema, "404": ErrorSchema})
def get_obras():
    """Faz a busca por todas as obras cadastradas.
    """
    logger.debug(f"Coletando obras ")
    # Criando conexão com a base
    session = Session()
    # Fazendo a busca
    obras = session.query(Obra).all()

    if not obras:
        # Se não há obras cadastradas
        return {"obras": []}, 200
    else:
        logger.debug(f"%d obras econtradas" % len(obras))
        # Retorna a representação de obra
        print(obras)
        return apresenta_obras(obras), 200

# ========================================================================================
""" Rota /obra para tratar o fetch de `DELETE` do script.js.
"""
# ========================================================================================
@app.delete('/obra', tags=[obra_tag],
            responses={"200": ObraDelSchema, "404": ErrorSchema})
def del_obra(query: ObraBuscaSchema):
    """Deleta uma obra a partir da obra e do artista informados.
    """
    obra_nome = unquote(query.nome)
    obra_artista = unquote(query.artista)

    print(obra_nome, obra_artista)
    logger.debug(f"Deletando dados sobre obra {obra_nome} e artista {obra_artista}")
    # Criando conexão com a base
    session = Session()
    
    # Fazendo a deleção da obra relacionada ao artista especificado
    count = session.query(Obra).filter(Obra.nome == obra_nome, Obra.artista == obra_artista).delete()
    session.commit()

    if count:
        # Retorna a representação da mensagem de confirmação
        logger.debug(f"Deletada obra {obra_nome} e {obra_artista}")
        return {"mesage": "Obra removida", "nome": obra_nome, "artista" : obra_artista}
    else:
        # Se a obra não foi encontrada
        error_msg = "Obra não encontrada na base :/"
        logger.warning(f"Erro ao deletar obra '{obra_nome}' e artista '{obra_artista}', {error_msg}")
        return {"mesage": error_msg}, 404
