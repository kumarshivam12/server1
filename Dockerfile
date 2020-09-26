FROM kumar1996/stack:latest
RUN pip install requests
WORKDIR /app
COPY . /app
EXPOSE 5000
ENTRYPOINT ["python"]
CMD ["application.py"]