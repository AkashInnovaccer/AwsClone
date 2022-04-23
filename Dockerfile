
FROM python

EXPOSE 5000

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD [ "python", "backend.py" ]
