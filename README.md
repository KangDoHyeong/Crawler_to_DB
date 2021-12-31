# Crawler_to_DB

import time

## 코드 맨 앞에 작성
f = open("%s.txt"%(time.strftime('%Y-%m-%d', time.localtime(time.time()))), 'w')
f.close()


f = open("%s.txt"%(time.strftime('%Y-%m-%d', time.localtime(time.time()))), 'a')
# 크롤링
f.write(crawled_data)
f.close()
