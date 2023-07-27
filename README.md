# Stardew exporter
![Docker Image Version (latest semver)](https://img.shields.io/docker/v/aleksandur24/stardewexporter)  ![Docker Pulls](https://img.shields.io/docker/pulls/aleksandur24/stardewexporter) 


![Image of dashboard](/img/Stardew_dashboard.png "Dashboard preview")


# Purpose 

This repository contains the code and other related files for writing a Prometheus exporter in Python that analyses a specific Stardew Valley save file. The goals of this project are mostly learning how to read XML files using Python, to write a Prometheus exporter for them, creating your own metrics of the data and eventually visualising using Grafana. 


# Usage
For easy deployment, all you need is an environment capable of pulling and running Docker images. In this repository you will find a premade docker-compose.yml file which spins up all 3 required instances and properly connects them in a docker network.

```console
docker-compose up -d
```
Simply visit localhost:3000 or \<IP-ADDRESS>:3000 (depending on how and where you deploy) to access the Grafana instance. Log in with username "admin" with the secure password "admin". The dashboard will automatically be shown upon logging in.

# Structure
This project consists of 3 major parts:
- Stardew-exporter: the exporter for metrics written in Python
- Prometheus: a Prometheus instance that gathers the metrics from our exporter
- Grafana: a Grafana instance that visualises the data gathered by Prometheus.

The repository contains some other files, such as personal notes, images for documentation and most importantly files related to Docker. These last files will allow for easy deployment and testing on your own system(s) that are capable of running Docker containers.

## Stardew exporter
This is the main focus of the project. The exporter (and subsequent docker image) mainly exists of a Python script and a special "SaveGameInfo" file (written in XML). This XML-file can be found in your local files for Stardew Valley on Windows, which will be located at:
```console
 C:\\Users\\USER\\AppData\\Roaming\\StardewValley\\Saves\\PLAYERNAME_NUMBERSTRING\\SaveGameInfo
```

For example, the XML-file for my character "Prom" on my computer where I am user "alexa" will be located at: 
```console
*C:\\Users\\alexa\\AppData\\Roaming\\StardewValley\\Saves\\Prom_347722748\\SaveGameInfo*
```

The Python script is responsible for processing this XML-file in such a way that specific tags (of your choice) and their contents get transformed into metrics. Using a specific package for Prometheus, we can then allow these metrics to be made available over an HTTP-server on a specific port. Whereas a standard node-exporter for Prometheus is usually exposed on port 9100, here we creatively expose the metrics on port 9321. Once run, the HTTP-server will serve the metrics in the following way:

![Image of exporter](/img/Stardew_Exporter.png "Metrics as seen served by HTTP-server")


## Prometheus instance
In order to scrape the metrics from our Stardew-exporter, we will need a Prometheus instance. For simplicity's sake, we will make use of a dockerised Prometheus instance with a specific configuration file that is set to scrape the exporter on the shared docker network. For transparancy and testing purposes, ports are exposed and you can access this Prometheus instance at localhost:9090 or \<IP-ADDRESS>:9090. To ensure the configuration file is set up properly, we can navigate to Status -> Targets, where we should see the following:
![Image of Prometheus instance](/img/Prometheus.png "Prometheus instance with targets to be scraped and status of said targets")

## Grafana instance
Lastly, we want to visualise the metrics scraped from our Stardew-exporter. For this, we will use a Grafana instance, once again using a Docker image. Because of the volume binding in the docker-compose file and the existing grafana-files, relevant configurations such as the dashboard-JSON as well as the home dashboard are carried over. It is enough to simply clone the repository and run the compose file.

# Limitations
## Static and limited data
The exporter is only applied on a static save file, so there is no real-time data updates as you play the game. If you want to analyse your own save file, you need to replace the "SaveGameInfo" file with the one found in your own Stardew Valley files. In the future this could be implemented better. 


## Unencrypted and excess HTTP
Another aspect is security. While this is only for testing purposes, all traffic and served metrics occur over HTTP, not HTTPS. Furthermore, the ports for the Prometheus exporter and Stardew-exporter (respectively 9090 and 9321) are currently exposed outside of the Docker containers. This step is unnecessary, as the internal Docker network already provides access for the Grafana-instance. It would be sufficient to expose the Grafana-instance (port 3000) and forego the exposure of ports 9090 and 9321. In this use case and for testing/demonstration purposes, however, it does have its uses.

## Massive size of docker image
This was the first time I built a Docker-image that is hosted on Docker Hub. Because of this inexperience, the way the Dockerfile works is most likely highly inefficient and most certainly *not* following best practices. The resulting docker image can therefore most likely be reduced in size by addressing these problems and optimizing this build. 

## Docker image base
As of right now, the image is built with FROM UBUNTU.This can be adapted to a smaller image, such as using FROM python.