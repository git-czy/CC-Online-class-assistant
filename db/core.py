# -*- coding: utf-8 -*-
# File: core.py
# @Author: 陈志洋
# @Email:  chenzhiyang@sinontt.com
# @Time: 2021/12/24 13:49
import sqlite3


class DBCore:
    init_user_table_sql = """
    create table user
    (
        id integer primary key autoincrement ,
        number varchar unique ,
        password varchar ,
        r_pas varchar ,
        show_window varchar ,
        course_type varchar ,
        last_chapter varchar ,
        last_course varchar ,
        last varchar
    )  
    """

    conn = None
    cursor = None

    def __init__(self):
        self._init_db()

    def _init_db(self, db_path: str = 'cc.db'):
        try:
            self.conn = sqlite3.connect(db_path)  # 建立数据库连接
            self.cursor = self.conn.cursor()  # 创建游标
            self.cursor.execute(self.init_user_table_sql)  # 执行sql语句
        except sqlite3.OperationalError as e:
            # todo 日志
            pass

    def flush(self):
        self.conn.commit()  # 提交

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.commit()  # 表提交
        self.cursor.close()
        self.conn.close()


class DMLSqlite(DBCore):
    def __init__(self):
        super().__init__()

    @staticmethod
    def _insert_serializer(kwargs):
        keys = kwargs.keys()
        values = kwargs.values()
        key_str = ','.join(keys)
        values = [f"'{item}'" for item in values]
        values_str = ','.join(values)
        return key_str, values_str

    @staticmethod
    def _select_serializer(kwargs):
        kwargs.pop('course_type', None)
        kwargs.pop('last_chapter', None)
        kwargs.pop('last_course', None)
        key = [f'{k} = {v}' for k, v in kwargs.items()]
        return ' AND '.join(key)

    @staticmethod
    def _update_serializer(kwargs):
        key = [f"{k} = '{v}'" for k, v in kwargs.items()]
        return ','.join(key)

    def select_user(self, **kwargs):
        """
        查找用户
        :param kwargs:查询参数
        :return: 用户信息
        """
        key = self._select_serializer(kwargs)
        sql = f"select * from user where {key};"
        data = self.cursor.execute(sql)
        data = data.fetchone()
        return {
            "id": data[0],
            "number": data[1],
            "password": data[2],
            "r_pas": data[3],
            "show_window": data[4],
            "course_type": data[5],
            "last_chapter": data[6],
            "last_course": data[7],
            "last": data[8]
        } if data else None

    def insert_or_update_user(self, **kwargs):
        """
        插入或者创建用户
        :param kwargs: 用户数据
        """
        number = kwargs.get('number', None)
        res = self.select_user(number=number)
        if res:
            user = self.update_user(res['id'], **kwargs)
        else:
            user = self.insert_user(**kwargs)
        return user

    def insert_user(self, **kwargs):
        """
        插入用户
        :param kwargs:插入数据
        :return: 用户数据
        """
        k, v = self._insert_serializer(kwargs)
        sql = f"insert into user({k}) values({v});"
        self.cursor.execute(sql)
        return self.select_user(**kwargs)

    def update_user(self, user_id, **kwargs):
        """
        更新用户
        :param user_id:用户id
        :param kwargs: 更新数据
        :return: 用户数据
        """
        set_value = self._update_serializer(kwargs)
        sql = f"update user set {set_value} where id = {user_id};"
        self.cursor.execute(sql)
        return self.select_user(id=user_id)


# if __name__ == '__main__':
# user = {
#     "number": "11",
#     "password": "123",
#     "r_pas": "1",
#     "course_type": "超星学习通",
#     "last_chapter": "毛概第一章",
#     "last_course": "毛概"
# }
# with DMLSqlite() as db:
#     data = db.insert_user(**user)
#     print(data)
    # res = db.select_user(number="123", r_pas="1")
    # print(res)
