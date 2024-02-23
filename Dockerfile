FROM python:3.12
COPY kefan .
COPY pyproject.toml .
RUN pip install pipx
RUN pipx install poetry
RUN /root/.local/bin poetry install
CMD ["/root/.local/bin/poetry" , "run" , "uvicorn" , "kefan.web:app"]