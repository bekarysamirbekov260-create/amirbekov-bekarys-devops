FROM python:3.12-alpine
WORKDIR /app
COPY app/ /app/
RUN echo "Image built for Bekarys Amirbekov (IT2 2309, 37898)" > /app/build_info.txt
ENV STUDENT_NAME=Bekarys \
    STUDENT_SURNAME=Amirbekov \
    STUDENT_GROUP="IT2 2309" \
    STUDENT_ID=37898
EXPOSE 8080
CMD ["python", "-u", "app.py"]
