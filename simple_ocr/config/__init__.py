# encoding: utf-8
import os
import environs


env = environs.Env()
try:
    env.read_env('.env.local')
except OSError:
    pass

try:
    env.read_env('.env')
except OSError:
    pass

# Postgres
POSTGRES_SERVER = dict(
    host=env.str("POSTGRES_HOST"),
    port=env.int("POSTGRES_PORT"),
    user=env.str("POSTGRES_USER"),
    password=env.str("POSTGRES_PASSWORD"),
    database=env.str("POSTGRES_DATABASE"),
)

#
ROOT_DIR = os.path.abspath(os.path.dirname(__name__)) + "/../"

# picture path
RESOURCE_PATH = f"{ROOT_DIR}/resources"
if not os.path.exists(RESOURCE_PATH):
    os.mkdir(RESOURCE_PATH)

# Tencent OCR
# TENCENT_APP_ID = env.str("TENCENT_APP_ID")
# TENCENT_OCR_URL = env.str("TENCENT_OCR_URL")
# TENCENT_OCR_APP_ID = env.str("TENCENT_OCR_APP_ID")
# TENCENT_OCR_APP_KEY = env.str("TENCENT_OCR_APP_KEY")
# TENCENT_SIGN_STRING = env.str("TENCENT_SIGN_STRING")
BAIDU_APP_ID = env.str("BAIDU_APP_ID")
BAIDU_APP_KEY = env.str("BAIDU_APP_KEY")
BAIDU_APP_SECRET = env.str("BAIDU_APP_SECRET")
BAIDU_GET_TOKEN_URL = env.str("BAIDU_GET_TOKEN_URL")
BAIDU_OCR_URL = env.str("BAIDU_OCR_URL")
