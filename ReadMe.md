# 调用API接口完成构建

- 主要是为了实现对参数的复用,无需每次都重新写参数

# 通过selenium模拟用户点击构建jenkins任务

```bash
# 安装依赖
pip install selenium

# 安装驱动器
from webdriver_manager.chrome import ChromeDriverManager
path = ChromeDriverManager().install()
print(path)

# 初始化
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

```
