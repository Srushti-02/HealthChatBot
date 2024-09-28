FROM python:3.8-alpine
RUN pip install flask
COPY . .
CMD ["python3", "-m" , "flask", "run", "--host=0.0.0.0"]
#write in terminal to run app
# docker run -d -p 5000:5000 basic-app