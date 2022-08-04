from sqlalchemy import Column, Integer, String, DateTime, ForeignKey

from sqlalchemy import orm

from .database import Base


class PData(Base):
    __tablename__ = 'page_data'

    id = Column(Integer, primary_key=True)
    avatar = Column(String, nullable=True)
    status = Column(String, nullable=True)
    photos = Column(String, nullable=True)
    page_id = Column(Integer, ForeignKey('reg.id'))
    page = orm.relationship('Reg')

    def __repr__(self):
        info: str = f'Пользователь [ID: {self.id}, Имя: {self.avatar}' \
                    f'Фамилия: {self.status}, Пароль: {self.photos}]'

        return info