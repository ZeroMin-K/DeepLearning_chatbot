import pymysql

db = None
try:
    db = pymysql.connect(
        host='127.0.0.1',
        user='homestead',
        passwd='secret',
        db='homestead',
        charset='utf8'
    )

    # 데이터 삽입 sql 정의
    id = 1  # 데이터 id ( Primary Key)
    sql = '''
        UPDATE tb_student set name="케이", age=36 where id=%d
    ''' % id

    # 데이터 수정
    with db.cursor() as cursor:
        cursor.execute(sql)
    db.commit()

except Exception as e:
    print(e)
finally:
    if db is not None:
        db.close()
