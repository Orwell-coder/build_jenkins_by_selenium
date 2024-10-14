# main.py

from core.jenkins_bot import JenkinsBot
from config import config


def main():
    # 初始化 Jenkins Bot
    bot = JenkinsBot(config.JENKINS_URL, config.USERNAME, config.PASSWORD)
    
    try:
        # 登录 Jenkins
        bot.login()
        
        # 触发构建任务
        job_name = "灵刃-安装包-0221-zx-test"
        bot.trigger_job_by_install(job_name, config.LR_INSTALL_PARAMS)
    
    finally:
        # 确保无论如何都会关闭浏览器
        bot.close()

if __name__ == "__main__":
    main()
