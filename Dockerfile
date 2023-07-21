FROM ubuntu

## Perform setup
COPY requirements.txt ./
RUN apt update

## Install python and pip
RUN apt install python3 pip -y
RUN pip install --no-cache-dir -r requirements.txt
RUN pip freeze -l
COPY . .
RUN ls


## Expose port on which exporter runs
EXPOSE 9321


CMD [ "python3", "StardewExporter.py" ]
