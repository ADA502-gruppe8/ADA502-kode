FROM python:3.12
FROM postgres:latest
EXPOSE 5432
RUN echo "host all all 0.0.0.0/0 md5" >> /var/lib/postgresql/data/pg_hba.conf && \
    echo "listen_addresses='*'" >> /var/lib/postgresql/data/postgresql.conf
COPY init-database.d /docker-entrypoint-initdb.d/
COPY kefan .
COPY pyproject.toml .
RUN pip install pipx
RUN pipx install poetry
RUN /root/.local/bin poetry install
CMD ["/root/.local/bin/poetry" , "run" , "uvicorn" , "kefan.web:app"]