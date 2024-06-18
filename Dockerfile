FROM python:3.11 as python-base
RUN mkdir python_tutorial
WORKDIR  /python_tutorial
COPY /pyproject.toml /python_tutorial
RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install 
COPY . .
CMD ["uvicorn", "run:server", "--host", "0.0.0.0", "--port", "5000"]
