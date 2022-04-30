import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ed
class chose1(object):
    def __init__(self):
        self.base_url = "http://xxxxx.cn/student/base/index.html"
        self.login_url="http://xxxxxxx.cn/base/login"
        self.driver=webdriver.Chrome(executable_path="D:\QIANG\chromedriver_win32\chromedriver.exe")
        """那个地址就是你安装的驱动的所在的地址"""
        self.time = str(datetime.datetime.now())
    def login(self):
        """""打开登陆的那个界面"""""
        self.driver.get(self.login_url)

        self.login_User()
        """你就在那个函数里再创建一个函数写那个验证码识别好了"""
        """函数就在后面"""


        """等待，直到到达self.base_url里存的那个url时运行下面的程序，说明登陆成功了，print（success）"""
        WebDriverWait(self.driver,10000).until(
            ed.url_to_be(self.base_url)
        )
        print("Login success!")
        #self.timer()
        """感觉有了那个clickable判断时间定时就不用了"""

        search = self.driver.find_element(by=By.XPATH,value="/html/body/div/div/section[2]/div[1]/div[2]/div[2]/div/a")  # 找到学生成长导师那个按钮
        search.click()  # 事件 点击


    def order(self):
        WebDriverWait(self.driver,1000).until(
            ed.element_to_be_clickable((By.XPATH,"//*[@title='顾飞燕']"))#要改人就改这个


        )
        search=self.driver.find_element(by=By.XPATH,value="//*[@title='顾飞燕']")#要改人就改这个
        search.click()

        """到时间那个按钮可以按了就运行"""
        WebDriverWait(self.driver,10000).until(
            ed.element_to_be_clickable((By.XPATH,"//*[@id='btnSubmitFrm2']"))
        )
        search = self.driver.find_element(by=By.XPATH, value="//*[@id='btnSubmitFrm2']")
        search.click()
        print("click success!")

    def login_User(self):
        self.driver.find_element_by_id("usrname").click()
        self.driver.find_element_by_id("usrname").send_keys("01636")
        self.driver.find_element_by_id("passwd").click()
        self.driver.find_element_by_id("passwd").send_keys("Nao2004.")
        self.driver.find_element_by_id("vercode").click()

        """运行验证码填充程序"""
        self.checkfill()



    def timer(self):
        while 1:
            self.time=str(datetime.datetime.now())
            if self.time[14:19]=='00:00':
                break
            else:
                print(self.time[10:19])
                continue

    def checkfill(self):
        pass



    def run(self):
        self.login()
        self.order()


if __name__=='__main__':
    go=chose1()
    go.run()

