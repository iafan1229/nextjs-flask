# #이슈1: 인증되지 않은 경우 코드 보내야되는데 어떻게 할 것인가
from app.routes import create_app

app = create_app()


if __name__ == '__main__':
    app.debug = True
    app.run()


import logging
from logging.config import dictConfig

logging_config = {
    'version': 1,
    'formatters': {
        'simple': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'simple',
            'stream': 'ext://sys.stdout'
        },
        'file': {
            'class': 'logging.FileHandler',
            'level': 'DEBUG',
            'formatter': 'simple',
            'filename': 'app.log',
            'mode': 'w'
        }
    },
    'root': {
        'level': 'DEBUG',
        'handlers': ['console', 'file']
    }
}

dictConfig(logging_config)

logger = logging.getLogger(__name__)

logger.debug('This is a debug message')
logger.info('This is an info message')
logger.error('This is an error message')