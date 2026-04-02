import logging

logging.basicConfig(
    filename='app.log',
    level=logging.INFO,  # исправлено loggin → logging
    format='%(asctime)s - %(levelname)s - %(message)s',
    encoding='utf-8'
)

print("fdfdf")
logging.info("Program run successfully")  # чтобы что-то реально в лог писалось