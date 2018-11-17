# -*- coding: utf-8 -*-

from sqlalchemy import Column, String, Text, Integer, create_engine
from sqlalchemy.orm import sessionmaker , scoped_session
from sqlalchemy.ext.declarative import declarative_base

# engine = create_engine('sqlite:///./test.db', convert_unicode=True)  # 创建数据库引擎( 当前目录下保存数据库文件)
engine = create_engine('mysql+mysqlconnector://user:pass@192.168.123.20:3306/teammatchKing?charset=utf8mb4')

db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    # 在这里导入所有的可能与定义模型有关的模块，这样他们才会合适地
    # 在 metadata 中注册。否则，您将不得不在第一次执行 init_db() 时
    # 先导入他们。
    import models
    Base.metadata.create_all(bind=engine)
