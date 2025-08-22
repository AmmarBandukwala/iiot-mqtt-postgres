
# IIoT MQTT to PostgreSQL & LoRaWAN Network Server

<!-- Badges example: add your own as needed -->
![Docker](https://img.shields.io/badge/docker-ready-blue)
![Python](https://img.shields.io/badge/python-3.11%2B-blue)

This repository provides two Docker Compose solutions:

- **MQTT to PostgreSQL**: A Python-based service that subscribes to an MQTT broker and inserts received payloads into a PostgreSQL database.
- **LoRaWAN Network Server**: Reference deployment files for [The Things Stack LoRaWAN Network Server](https://www.thethingsindustries.com/docs/the-things-stack/host/docker/configuration/), located in the `lorawan-network-server-deploy` directory.

---

## Features

- End-to-end IIoT data pipeline: MQTT → Python → PostgreSQL
- Easy local or cloud deployment with Docker Compose
- Reference setup for LoRaWAN network server

---

## Prerequisites

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)
- [Python 3.11+](https://www.python.org/downloads/)
- [PostgreSQL](https://www.postgresql.org/)

---

## Getting Started

### 1. Clone the Repository

```sh
git clone https://github.com/yourusername/iiot-mqtt-postgres.git
cd iiot-mqtt-postgres
```

### 2. Build and Start the Services

```sh
docker-compose up --build
```

---

## Usage

### MQTT to PostgreSQL Pipeline

1. Ensure your MQTT broker is running and accessible (update connection details in `src/mqttconnector.py` if needed).
2. The Python service will subscribe to the MQTT broker and insert incoming messages into the PostgreSQL database.
3. You can modify the topic, broker address, and database credentials in the configuration or environment variables as needed.

### LoRaWAN Network Server

1. Navigate to the deployment folder:
    ```sh
    cd lorawan-network-server-deploy
    ```
2. Review and update configuration files as needed (see `NOTES.md` for tips).
3. Start the LoRaWAN stack:
    ```sh
    docker-compose up --build
    ```
4. Follow [The Things Stack documentation](https://www.thethingsindustries.com/docs/the-things-stack/host/docker/configuration/) for advanced setup and security.

---

## Project Structure

```plaintext
.
├── requirements.txt
├── docker-compose.yml
├── Dockerfile
├── src/
│   ├── __init__.py
│   ├── main.py
│   └── mqttconnector.py
└── lorawan-network-server-deploy/
    ├── docker-compose.yml
    ├── NOTES.md
    └── config/
        └── stack/
            └── ttn-lw-stack-docker.yml
```

---

## Configuration

- Edit `src/mqttconnector.py` and `src/main.py` to set MQTT topics, broker address, and database credentials.
- Update environment variables in `docker-compose.yml` as needed.
- For LoRaWAN, see `lorawan-network-server-deploy/NOTES.md` for setup and security tips.

---

## Contributing

Contributions are welcome! Please open issues or submit pull requests for improvements or bug fixes.

---

## License

This project is licensed under the GNU License. See the [LICENSE](LICENSE) file for details.
