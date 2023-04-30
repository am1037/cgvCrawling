from selenium import webdriver
from selenium.webdriver.common.by import By
import datetime

# URL of the theater page
#CGV_THEATER_URL = 'http://www.cgv.co.kr/theaters/?areacode=01&theaterCode=0013'     # CGV 용산아이파크몰
CGV_THEATER_URL = 'http://www.cgv.co.kr/theaters/?areacode=02&theaterCode=0004&date=' #오리
DATE = '20230505' #datetime.datetime.now().strftime('%Y%m%d') # 날짜

option = webdriver.ChromeOptions()
option.add_experimental_option("useAutomationExtension", False)
option.add_experimental_option("excludeSwitches", ['enable-automation'])
driver = webdriver.Chrome(executable_path='chromedriver', options=option)
driver.delete_all_cookies()

#1. 날짜를 가져와야.. -> 날짜가 바뀌도록 할 수 있어야.. OK!
#2. 영화 제목을 가져와야.. -> OK!
#3. 상영관, 상영 시간을 가져와야.. -> OK!

driver.get(url=CGV_THEATER_URL+DATE)
innerIframe = driver.find_element(By.ID, "ifrm_movie_time_table")
driver.switch_to.frame(innerIframe)


movies = driver.find_element(By.CLASS_NAME, "showtimes-wrap").find_element(By.CLASS_NAME, "sect-showtimes").find_elements(By.CLASS_NAME, "col-times")
for m in movies:
    print("----------")
    print(m.find_element(By.CLASS_NAME, "info-movie").find_element(By.TAG_NAME, "strong").text) #영화 제목
    halls = m.find_elements(By.CLASS_NAME, "type-hall")
    for h in halls:
        hall_list = h.find_element(By.CLASS_NAME, "info-hall").find_elements(By.TAG_NAME, "li")
        hall_name = hall_list[1].text #상영관
        timetable = h.find_element(By.CLASS_NAME, "info-timetable").find_elements(By.TAG_NAME, "em") #상영 시간
        for t in timetable:
            print(f"{hall_name} {t.text}")