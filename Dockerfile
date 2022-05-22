FROM python:3.9.13-alpine3.15

#copy
COPY . /py-demo

#defining work directory 
WORKDIR /py-demo

RUN pip install -r python_req.txt 
#--no-cache-dir
# can also added for  no cache in dir  

#I used 5656 that's why otherwise flask default port 5000 then need to expose the same port 
EXPOSE 5000 

#if not executable than have to use ENTERYPOINT LIKE
#ENTRYPOINT [ "python" ]

#CMD [ "executable", "parameter", ... ]
#if ENTRYPOINT not the need to define executable like python,npm depending upon application,....
CMD [ "python", "main.py" ]  