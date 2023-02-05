FROM python:3.9
COPY . .
EXPOSE 8050
RUN cat requirements.txt | xargs -n 1 -L 1 python -m pip install
ENTRYPOINT ["python", "main.py"]