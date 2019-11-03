FROM python3.7.5-alpine 
WORKDIR /app/server
RUN python -m pip install -r requirements.txt
COPY .  .
ENTRYPOINT [ "python" "main.py"]