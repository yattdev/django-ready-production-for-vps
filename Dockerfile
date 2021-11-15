# Pull base image
FROM python:3.8

# Set environment variable
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# add new user
RUN useradd -ms /bin/bash alassane
USER alassane

# Set work directory
WORKDIR /home/alassane/yattblog/

# Copy pipfile and change ower from host alassane to vm alassane
COPY --chown=alassane:alassane Pipfile Pipfile.lock /home/alassane/yattblog/

ENV PATH="/home/alassane/.local/bin:${PATH}"

# Update pip
RUN pip install --upgrade pip

# install dependencies
RUN pip install --user pipenv && pipenv install --system

# Copy project, period dot (.) meant current dir
COPY --chown=alassane:alassane . /home/alassane/yattblog/

USER root
RUN chown alassane:alassane /home/alassane/
RUN chown alassane:alassane /home/alassane/yattblog/
USER alassane
