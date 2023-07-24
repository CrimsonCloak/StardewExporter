![Image of dashboard](/img/Stardew_dashboard.png "Dashboard preview")


# Purpose 

This repository contains the code and other related files for writing a Prometheus exporter in Python that analyses a specific Stardew Valley save file. The goals of this project are mostly learning how to read XML files, using Python to write a Prometheus exporter for them, creating your own metrics of the data and eventually visualising using another software. 


# Usage
For easy deployment, all you need is an environment capable of pulling and running Docker images. In this repository you will find a premade docker-compose.yml file which spins up all 3 required instances and properly connects them.

```console
docker-compose up -d
```

# Structure
This project consists of 3 major parts:
- StardewExporter: the exporter for metrics written in Python
- Prometheus: a Prometheus instance that gathers the metrics from our exporter
- Grafana: a Grafana instance that visualises the data gathered by Prometheus.

The repository contains some other files, such as personal notes, images for documentation and most importantly files related to Docker. These last files will allow for easy deployment and testing on your own system(s) that are capable of running Docker containers.





# Limitations

The exporter is only applied on a static save file, so there is no real-time data updates as you play the game. If you want to analyse your own save file, you need to replace the "SaveGameInfo" file with the one found in your own Stardew Valley files. In the future this could be implemented better. 