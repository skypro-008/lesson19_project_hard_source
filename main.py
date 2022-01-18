from app import create_app
import os
from dotenv import load_dotenv

# https://flask.palletsprojects.com/en/1.1.x/cli/#environment-variables-from-dotenv
# берем конфиг из .env
load_dotenv('.env')

app = create_app(config_name=os.environ.get("APP_CONFIG") or 'dev')

if __name__ == '__main__':
    app.run()
