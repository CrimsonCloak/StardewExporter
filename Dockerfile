FROM ubuntu

## Perform setup
COPY StardewExporter.py requirements.txt ./
ADD Savefiles_Samples ./Savefiles_Samples/
RUN apt update

## Install Python and pip
RUN apt install python3 pip -y
RUN pip install --no-cache-dir -r requirements.txt


## Expose port on which exporter runs
EXPOSE 9321
## Run Python script
CMD [ "python3", "StardewExporter.py" ]
