FROM python:2.7

MAINTAINER Michael Palmer <michael@michaeldpalmer.com>

# Environment variables
ENV PYTHONUNBUFFERED 1
ENV FLASK_SETTINGS_MODULE 'hotel.settings.prod'

# Setup environment
RUN mkdir /code
WORKDIR /code
ADD . /code/

# Install python requirements
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose the port
EXPOSE 80

# Start the server
CMD ["python", "hotel.wsgi"]

