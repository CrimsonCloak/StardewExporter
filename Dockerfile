FROM ubuntu

## Perform setup
COPY requirements.txt ./
RUN apt update

## Install Python and pip
RUN apt install python3 pip -y
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

## Install Prometheus


## Install Grafana
##RUN apt-get install -y apt-transport-https software-properties-common wget
##RUN wget -q -O /usr/share/keyrings/grafana.key https://apt.grafana.com/gpg.key
##RUN echo "deb [signed-by=/usr/share/keyrings/grafana.key] https://apt.grafana.com stable main" | tee -a /etc/apt/sources.list.d/grafana.list
##RUN apt-get update
##RUN apt-get install grafana-enterprise
##RUN start grafana-server


## Expose port on which exporter runs
EXPOSE 9321
##EXPOSE 3000
## Run Python script
CMD [ "python3", "StardewExporter.py" ]
