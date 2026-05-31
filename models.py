'''
Author: Telliex telliexyuzo@gmail.com
Date: 2026-05-30 21:00:27
LastEditors: Telliex telliexyuzo@gmail.com
LastEditTime: 2026-05-30 21:03:24
FilePath: /week-04-api/models.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from database import Base
from sqlalchemy import Column, Integer, String

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    status = Column(String, nullable=False, default="unread")
    rating = Column(Integer, nullable=True)