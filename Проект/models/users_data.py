from sqlalchemy import Column, Integer, String, DateTime, ForeignKey

from sqlalchemy import orm

from .database import Base


class Data(Base):
    __tablename__ = 'data'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=True)
    surname = Column(String, nullable=True)
    hashed_password = Column(String, nullable=True)
    created_date = Column(DateTime, nullable=True)
    user_id = Column(Integer, ForeignKey('reg.id'))
    user = orm.relationship('Reg')

    def __repr__(self):
        info: str = f'Пользователь [ID: {self.id}, Имя: {self.name}' \
                    f'Фамилия: {self.surname}, Пароль: {self.hashed_password}, ' \
                    f'Фото: {self.avatar}, Время: {self.created_date}]'

        return info