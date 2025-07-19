from api import db
from ..models import formacao_model

class Curso(db.Model):
    # Nome da tabela
    __tablename__ = 'curso'
    # Variável id corresponde a uma coluna de inteiros, sendo a chave primaria da tabela com autoincremento e não podendo ser vazio
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    # Variável nome corresponde a uma coluna de String (Limitada a 50 caracteres) não podendo ser falsa.
    nome = db.Column(db.String(50), nullable=False)
    descricao = db.Column(db.String(100), nullable=False)
    data_publicacao = db.Column(db.Date, nullable=False)

    formacao_id = db.Column(db.Integer, db.ForeignKey("formacao.id"))
    formacao = db.relationship(formacao_model.Formacao, backref=db.backref("curso", lazy="dynamic"))