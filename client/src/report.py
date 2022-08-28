from database import get_mysql_cnxn

TICKETS_BY_EVENT = """
select event_name, sum(num_tickets) as event_ticket_total
from sales
group by event_name
order by event_ticket_total desc
limit 3
"""

def query_popular_tickets(connection):
    # Get the most popular ticket in the past month
    cursor = connection.cursor()
    cursor.execute(TICKETS_BY_EVENT)
    records = cursor.fetchall()
    cursor.close()
    return records

def popular_tickets():
    cnxn = get_mysql_cnxn()
    data = query_popular_tickets(cnxn)
    line1 = "Here are the most popular tickets in the past month:"
    lines = [line1]
    for line in data:
        lines.append(f'- {line[0]}')

    print('\n'.join(lines))


if __name__ == "__main__":
    popular_tickets()