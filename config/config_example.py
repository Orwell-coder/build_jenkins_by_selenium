# config.py

JENKINS_URL = "xxxx"
USERNAME = "xxxx"
PASSWORD = "xxxxx"

############## version management  #############
GOSCAN_VERSION = "xxxx"
GOBOT_VERSION = "xxxx"
###############################################

################ upgrade ######################
UPGRADE_DESCRIBE_VERSION = "xxxx"
UPGRADE_VERSION = "xxxx"
###############################################

############### install #######################
INSTALL_MISC_TAG_VERSION = 'xxxx'
INSTALL_VERSION = 'xxxx'
###############################################

LR_SWARM_UPGRADE_PARAMS = [
    {
        "tag": "describe",
        "value": UPGRADE_DESCRIBE_VERSION,
        "next": False,
        "is_package": False,
        "is_option": False
    },
    {
        "tag": "version_num",
        "value": UPGRADE_VERSION,
        "next": False,
        "is_package": False,
        "is_option": False
    },
    {
        "tag": "xxxx",
        "package_tag": "xxxx",
        "value": GOSCAN_VERSION,
        "next": True,
        "is_package": True,
        "is_option": True
    },
    {
        "tag": "xxxx",
        "package_tag": "xxxx",
        "value": GOBOT_VERSION,
        "next": True,
        "is_package": True,
        "is_option": True
    },
    
]

LR_INSTALL_PARAMS = [
    {
        'tag': 'aiscan_misc_tag',
        'value': INSTALL_MISC_TAG_VERSION,
        'is_option': True
    },
    {
        'tag': 'versions',
        'value': INSTALL_VERSION,
        'is_option': False
    },
    {
        'tag': 'uias_server_cloud',
        'value': 'mutiuser',
        'is_option': False
    }
]