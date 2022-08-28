import csv
import pathlib
from loguru import logger

from database import get_mysql_cnxn


def csv_iter(csv_path):
    with open(csv_path,'r',newline='') as fh:
        reader = csv.reader(fh)
        for row in reader:
            yield row


def insert_record_on_sale_tb(cnxn,data):
    sql = "INSERT INTO sales VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    cursor = cnxn.cursor()
    try:
        cursor.execute(sql, data)
        cnxn.commit()
    except Exception as e:
        logger.error(e)
    finally:
        cursor.close()


def process_sales_csv(csv_path):
    cnxn = get_mysql_cnxn()
    csv_iter_items = csv_iter(csv_path)
    try:
        [insert_record_on_sale_tb(cnxn,data) for data in csv_iter_items]
        logger.info('data load complete')
    except Exception as e:
        logger.warning('error loading data')


def main():
    csv_path = list(pathlib.Path('/data').rglob('*.csv'))[0]
    process_sales_csv(csv_path)


if __name__ == "__main__":
    main()