FROM python:3.7
ARG pkg
ARG dev=false
WORKDIR /app
ENV HTTP_PROXY http://10.8.0.1:8080
ENV HTTPS_PROXY http://10.8.0.1:8080
RUN pip install gitpython
COPY ./script.py script.py
RUN chmod +x script.py
RUN python3 ./script.py $dev $pkg
CMD python
