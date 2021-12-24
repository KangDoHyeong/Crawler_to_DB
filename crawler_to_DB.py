import pymysql as my


def cwl_data_insert(insert_data):
    # 아마 insert_data가 tuple로 들어가야 했던거 같음
    connection = None
    result = 0 # 로그인 결과를 담는 변수
    try:
        connection = my.connect(host='192.168.1.39', # DB 주소
                                user='song',      # DB 접속 계정
                                password='12341234', # DB 접속 비번
                                db='tpapdb',   # Database 이름
                                #port=3306,        # Port     
                                charset='utf8',
                                cursorclass=my.cursors.DictCursor) # Cursor Type

        if connection:
            print('user DB OPEN')
            #####################################################
            with connection.cursor() as cursor:
                sql    ='''
                INSERT INTO cwl_trd_data 
                values (NULL,'%s',
                '%s','%s','%s','%s','%s','%s','%s',
                '%s','%s','%s','%s','%s','%s','%s',
                '%s','%s','%s',%d,%d,%d,%d)'''%insert_data
                # print(sql)
                
                
                cursor.execute( sql )
                connection.commit()
                result = connection.affected_rows() # 1이 되야지 성공
            #####################################################
    except Exception as e:
        print('ERROR!!! -> ', e)
        result = 0
    finally:
        if connection:
            connection.close()
            print('user DB CLOSE')
    return result


### 예시
crawled_data = ('700-1234-12345-12345',
'123-45-12345',  '활빈당', '홍길동', '서울시 서초구', 'IT', '소프트웨어 개발','sample@gmail.com', 
'678-90-67890', '활빈당2', '홍길동2', '서울시 서초구2', 'IT2', '소프트웨어 개발2','sample2@gmail.com', 
'231201', '대시보드개발외주', 'NULL', 1, 1000000, 100000, 1100000)

cwl_data_insert(crawled_data)
