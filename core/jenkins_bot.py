# jenkins_bot.py

import time
import config

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select


class JenkinsBot:
    def __init__(self, jenkins_url, username, password):
        """初始化 JenkinsBot 并设置登录信息"""
        self.jenkins_url = jenkins_url
        self.username = username
        self.password = password
        self.driver: webdriver.Chrome

    def _setup_browser(self):
        """启动浏览器，配置好 WebDriver"""
        options = webdriver.ChromeOptions()
        # options.add_argument("--headless")  # 无头模式
        # options.add_argument("--disable-gpu")  # 禁用 GPU 加速
        # options.add_argument("--no-sandbox")  # 禁用沙盒模式
        # options.binary_location= "C:\\Users\\attem\\.wdm\\drivers\\chromedriver\\win64\\129.0.6668.100\\chromedriver-win32\\chromedriver.exe"
        options.browser_version = 'stable'
        options.platform_name = 'any'
        options.accept_insecure_certs = True
        # options.executable_path = ChromeDriverManager().install()
        # options.page_load_strategy = 'normal'
        self.driver = webdriver.Chrome(options)
        self.driver.maximize_window()

    def login(self):
        """登录 Jenkins"""
        self._setup_browser()
        self.driver.get(f"{self.jenkins_url}/login")

        # 输入用户名
        self.driver.find_element(By.ID, "j_username").send_keys(self.username)

        # 输入密码
        self.driver.find_element(By.NAME, "j_password").send_keys(self.password)

        # 提交表单
        self.driver.find_element(By.NAME, "Submit").click()

        # 等待页面加载
        time.sleep(3)

        # 检查登录是否成功
        if "Dashboard" in self.driver.page_source:
            print("登录成功")
        else:
            print("登录失败")
            self.driver.quit()
            raise Exception("Failed to login to Jenkins")

    def trigger_job_by_upgrade(self, job_name:str, params:list):
        """触发 Jenkins 构建任务"""
        job_url = f"{self.jenkins_url}/job/{job_name}/build?delay=0sec"
        self.driver.get(job_url)
        time.sleep(5)
        print("find element")
        
        for param in params:
            print(f"param: {param['tag']} {param['value']}")
            
            # 普通参数
            if not param['is_option'] and not param['is_package']:
                if param['tag'] == "version_num":
                    self.driver.find_element(By.CSS_SELECTOR, f"input[value={param['tag']}]+input").clear()
                self.driver.find_element(By.CSS_SELECTOR, f"input[value={param['tag']}]+input").send_keys(param['value'])
            # 可选项参数+打包
            if param['is_option'] and param['is_package']:
                select_ele = self.driver.find_element(By.CSS_SELECTOR, f"input[value={param['tag']}]+select")
                option_list = Select(select_ele).options
                is_find = False
                for option in option_list:
                    if option.text == param['value']:
                        is_find = True
                        option.click()
                if not is_find:
                    print(f"Failed to find option: {param['value']}")
                    raise Exception(f"Failed to find option: {param['value']}")
                # Select(self.driver.find_element(By.CSS_SELECTOR, f"input[value={param['tag']}]+select")).select_by_visible_text(param['value'])
                Select(self.driver.find_element(By.CSS_SELECTOR, f"input[value={param['package_tag']}]+select")).select_by_visible_text("true")
            # 普通参数+打包
            if not param['is_option'] and param['is_package']:
                self.driver.find_element(By.CSS_SELECTOR, f"input[value={param['tag']}]+input").send_keys(param['value'])
                Select(self.driver.find_element(By.CSS_SELECTOR, f"input[value={param['package_tag']}]+select")).select_by_visible_text("true")
            
            time.sleep(1)


        self.driver.find_element(By.NAME, "Submit").click()

        time.sleep(10)
        
        # 检查任务是否成功启动
        if "构建结果" in self.driver.page_source:
            print(f"Job '{job_name}' 构建启动成功")
        else:
            print(f"Job '{job_name}' 构建启动失败")
    
    def trigger_job_by_install(self, job_name:str, params:list):
        """触发 Jenkins 构建任务"""
        job_url = f"{self.jenkins_url}/job/{job_name}/build?delay=0sec"
        self.driver.get(job_url)
        time.sleep(5)
        print("find element")
        
        for param in params:
            print(f"param: {param['tag']} {param['value']}")
            
            # 普通参数
            if param['is_option']:
                select_ele = self.driver.find_element(By.CSS_SELECTOR, f"input[value={param['tag']}]+select")
                option_list = Select(select_ele).options
                is_find = False
                for option in option_list:
                    if option.text == param['value']:
                        is_find = True
                        option.click()
                if not is_find:
                    print(f"Failed to find option: {param['value']}")
                    raise Exception(f"Failed to find option: {param['value']}")
            # if param['tag'] == "version_num":
            else:
                self.driver.find_element(By.CSS_SELECTOR, f"input[value={param['tag']}]+input").clear()
                self.driver.find_element(By.CSS_SELECTOR, f"input[value={param['tag']}]+input").send_keys(param['value'])
            
            time.sleep(1)


        self.driver.find_element(By.NAME, "Submit").click()

        time.sleep(10)
        
        # 检查任务是否成功启动
        if "构建结果" in self.driver.page_source:
            print(f"Job '{job_name}' 构建启动成功")
        else:
            print(f"Job '{job_name}' 构建启动失败")

    def close(self):
        """关闭浏览器"""
        if self.driver:
            self.driver.quit()

    def __del__(self):
        """确保在对象销毁时关闭浏览器"""
        self.close()
