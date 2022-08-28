docker compose exec pyclient python src/ddl.py
docker compose exec pyclient python src/seed.py
docker compose exec pyclient python src/report.py