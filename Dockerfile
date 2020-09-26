FROM kumar1996/stack:latest
RUN pip install requests
WORKDIR /app
COPY . /app
EXPOSE 8000
ENTRYPOINT ["python"]
CMD ["application.py"]
