from crawler_to_DB_2 import *




crawled_data = ('700-1234-12345-12345',
'123-45-12345',  '활빈당', '홍길동', '서울시 서초구', 'IT', '소프트웨어 개발','sample@gmail.com', 
'678-90-67890', '활빈당2', '홍길동2', '서울시 서초구2', 'IT2', '소프트웨어 개발2','sample2@gmail.com', 
'231201', '대시보드개발외주', 'NULL', 1, 1000000, 100000, 1100000)

# 승인번호, 공급자 사업자번호, 공급받는자 사업자 번호, 거래일자, 제품명, 제품 규격, 제품 수량, 공급 가격, 제품 단가, 세액

crawled_company_data_1 = (crawled_data[2], crawled_data[1], crawled_data[3], crawled_data[4], crawled_data[5],crawled_data[6],crawled_data[7])
crawled_company_data_2 = (crawled_data[9], crawled_data[8], crawled_data[10], crawled_data[11], crawled_data[12],crawled_data[13],crawled_data[14])
crawled_trade_data = (crawled_data[0], crawled_data[1], crawled_data[8], crawled_data[15], crawled_data[16], crawled_data[17],crawled_data[18], crawled_data[19], crawled_data[20], crawled_data[21])


tmp_count=count_BZ_NUMBER(crawled_company_data_1[1])['Count(*)']
if tmp_count==0:
    cwl_company_data_insert(crawled_company_data_1)
elif tmp_count > 1:
    print("먼가 잘못되었습니다.")

tmp_count=count_BZ_NUMBER(crawled_company_data_2[1])['Count(*)']
if tmp_count==0:
    cwl_company_data_insert(crawled_company_data_2)
elif tmp_count > 1:
    print("먼가 잘못되었습니다.")

cwl_trade_data_insert(crawled_trade_data)