FROM python:3.12

COPY src .
COPY tests .
COPY pyproject.toml .

RUN pip install pipx
RUN pipx install poetry
RUN /root/.local/bin/poetry install