from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy import orm

from .database import Base


class Reg(Base):
    __tablename__ = 'reg'

    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=True)
    code_ver = Column(Integer, nullable=True)
    data = orm.relation("Data", back_populates='user')
    data_page = orm.relation('PData', back_populates='page')

    def __repr__(self):
        info: str = f'Пользователь [ID: {self.id}, Почта: {self.email}' \
                    f', Код: {self.code_ver}]'

        return info