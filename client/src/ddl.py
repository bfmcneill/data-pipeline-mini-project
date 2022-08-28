from database import get_mysql_cnxn
from loguru import logger

DROP_SALES_TABLE = "DROP TABLE IF EXISTS `springboardopt`.`sales`;"

CREATE_SALES_TABLE = """
CREATE TABLE springboardopt.sales (
	ticket_id INT,
	trans_date DATETIME,
	event_id INT,
	event_name VARCHAR(50),
	event_date DATE,
	event_type VARCHAR(10),
	event_city VARCHAR(20),
	customer_id INT,
	price DECIMAL,
	num_tickets INT
)
"""

def ddl_create_tables():
    cnxn = get_mysql_cnxn()
    cursor = cnxn.cursor()
    logger.info('dropping sales table')
    cursor.execute(DROP_SALES_TABLE)
    cnxn.commit()
    logger.info('creating sales table')
    cursor.execute(CREATE_SALES_TABLE)
    cnxn.commit()
    cursor.close()


if __name__ == "__main__":
    ddl_create_tables()