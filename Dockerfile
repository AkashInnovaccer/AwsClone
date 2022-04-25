
FROM python

EXPOSE 5000

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD [ "python", "backend.py" ]

# FROM python
# WORKDIR /app
# RUN mkdir download
# RUN mkdir static
# COPY ./requirements.txt .
# RUN pip install -r requirements.txt
# COPY ./app.py .
# RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
# RUN unzip awscliv2.zip
# RUN ./aws/install

# EXPOSE 5000
# CMD ["python3","app.py"] 