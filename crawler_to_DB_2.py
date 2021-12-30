import pymysql as my



def count_BZ_NUMBER(insert_data):
    connection = None
    rows       = None 
    try:
        connection = my.connect(host='localhost', # 디비 주소
                            user='root',      # 디비 접속 계정
                            password='12312312', # 디지 접속 비번
                            db='TPAP',   # 데이터베이스 이름
                            #port=3306,        # 포트     
                            charset='utf8',
                            cursorclass=my.cursors.DictCursor) # 커서타입지정
        # 쿼리수행
        with connection.cursor() as cursor: 
            print('COMPANY DB OPEN')           
            sql    = '''
                SELECT Count(*)
                FROM   CPN_DATA
                WHERE  CD_BZ_NB = "%s"
                '''%insert_data
            cursor.execute( sql )
            rows    = cursor.fetchone()           
    except Exception as e:
        print('->', e)
        rows = None
    finally:
        if connection:
            connection.close()
            print('COMPANY DB CLOSE')
    return rows

def cwl_company_data_insert(insert_data):
    # 아마 insert_data가 tuple로 들어가야 했던거 같음
    connection = None
    result = 0 # 로그인 결과를 담는 변수
    try:
        connection = my.connect(host='localhost', # DB 주소
                                user='root',      # DB 접속 계정
                                password='12312312', # DB 접속 비번
                                db='TPAP',   # Database 이름
                                #port=3306,        # Port     
                                charset='utf8',
                                cursorclass=my.cursors.DictCursor) # Cursor Type

        if connection:
            print('COMPANY DB OPEN')
            #####################################################
            with connection.cursor() as cursor:
                sql    ='''
                    INSERT INTO CPN_DATA
                                (CD_CPN_NM,
                                CD_BZ_NB,
                                CD_CPN_RPST_NM,
                                CD_CPN_ADRS,
                                CD_CPN_BZ_TP,
                                CD_CPN_BZ_SCT,
                                CD_CPN_BZ_EM)
                    VALUES      ('%s', '%s', '%s', '%s', '%s', '%s', '%s')'''%insert_data
                # 업체명, 업체 사업자 번호, 업체 대표명, 업체 주소, 업체 업태, 업체 업종목, 업체 이메일
                
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
            print('COMPANY DB CLOSE')
    return result

def cwl_trade_data_insert(insert_data):
    # 아마 insert_data가 tuple로 들어가야 했던거 같음
    connection = None
    result = 0 # 로그인 결과를 담는 변수
    try:
        connection = my.connect(host='localhost', # DB 주소
                                user='root',      # DB 접속 계정
                                password='12312312', # DB 접속 비번
                                db='TPAP',   # Database 이름
                                #port=3306,        # Port     
                                charset='utf8',
                                cursorclass=my.cursors.DictCursor) # Cursor Type

        if connection:
            print('TRADE DB OPEN')
            #####################################################
            with connection.cursor() as cursor:
                sql    ='''
                        INSERT INTO CWL_TRD_DATA
                                    (CTD_ARV_NB,
                                    CTD_SPLR_BZ_NB,
                                    CTD_PCS_BZ_NB,
                                    CTD_TRD_DT,
                                    CTD_PRD_NM,
                                    CTD_PRD_STD,
                                    CTD_PRD_NB,
                                    CTD_PRD_PRV_PRC,
                                    CTD_PRD_FUL_PRC,
                                    CTD_PRD_TAX_AMT)
                        VALUES      ( '%s', '%s', '%s', '%s', '%s',
                                    '%s', %s, %s, %s, %s)'''%insert_data
                # 승인번호, 공급자 사업자번호, 공급받는자 사업자 번호, 거래일자, 제품명, 제품 규격, 제품 수량, 공급 가격, 제품 단가, 세액
                
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
            print('TRADE DB CLOSE')
    return result



# 승인번호, 공급자 사업자번호, 공급받는자 사업자 번호, 거래일자, 제품명, 제품 규격, 제품 수량, 공급 가격, 제품 단가, 세액





