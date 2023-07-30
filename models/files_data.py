from sqlalchemy import Column, Integer, String

from .database import Base


class Files_Data(Base):
    __tablename__ = 'files'

    id = Column(Integer, primary_key=True)
    file = Column(String, nullable=True)
    code = Column(String, nullable=True)

    def __repr__(self):
        info: str = f'Пользователь [ID: {self.id}, Имя: {self.file}, Code: {self.code}]'

        return info