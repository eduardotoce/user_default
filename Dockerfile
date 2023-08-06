FROM python: 3.10.12
COPY conda/create_env.sh create_env.sh
COPY ./* ./src/
WORKDIR /src/
COPY requirements.txt  .ç
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 80
CMD ["python", "main_app.py"]