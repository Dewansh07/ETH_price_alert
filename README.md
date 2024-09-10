# ETH Monitoring Tool

The Ethereum Deposit Tracker is a real-time monitoring tool designed to observe deposit events on the Ethereum Beacon Chain. 

It listens for deposit events, stores data in MongoDB, and provides visualization and metrics collection using Prometheus and Grafana. Additionally, the tracker sends instant notifications to a Telegram chat when new deposits are detected, making it a valuable tool for blockchain analysts and Ethereum enthusiasts.<br>

**Features**

*Real-Time Deposit Monitoring:* Continuously listens for deposit events from the Ethereum Beacon Chain contract.<br>

*Telegram Notifications:* Sends alerts to a list of registered chat IDs via Telegram for every new deposit event.

*Detailed Logging:* Logs critical actions like deposit detection, errors, and notifications.

*Metrics Collection:* Tracks key metrics with Prometheus for data analysis.

*Data Storage:* Stores detailed deposit data in MongoDB for historical analysis.

*Visualization:* Creates real-time visual dashboards with Grafana for easy monitoring.

## Prerequisites
- Python 3.8 or higher
- Web3.py
- Alchemy/Infura API Key

## Setup Instructions
1. Clone the repository:
   ```
   git clone <repo-url>
   cd ethereum-deposit-tracker
   ```
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Configure your Alchemy/Infura API key and Telegram Bot (optional) in the script.
4. Run the tracker:
   ```
   python tracker.py
   ```


## Project Structure
```plaintext
ETH_monitor/
│
│
├── alerts.py             # Handles alerting functionality; sends alerts via Telegram.
├── config.yaml           # Configuration file for the application; contains settings for validator and alerts.
├── config.yaml           # Configuration file for the application; contains settings for validator and alerts.
├── Dockerfile            # Dockerfile to build a container image for the application.
├── main.py               # Main entry point of the application; orchestrates monitoring and alerting.
├── monitor.py            # Contains core monitoring functionality; checks validator status and sync progress.
│
└── requirements.txt      # Lists Python dependencies required for the application.
```



## File Descriptions

- **`main.py`**: 
  - The main entry point of the application. By invoking functions from other modules, it coordinates the monitoring process and manages alert logic according to the validator's state.

- **`monitor.py`**: 
  - Includes the essential monitoring features that ascertain the Polygon validator's state and whether it is in sync with the blockchain.

- **`alerts.py`**: 
  - Oversees the alerting procedure by notifying a designated Telegram chat when problems with the validator are found.

- **`config.py`**: 
  - In charge of loading configuration parameters from the `config.yaml` file so that managing application settings is simple.

- **`config.yaml`**: 
  - A YAML configuration file including alert levels, the Telegram bot token, the Ethereum RPC endpoint, and other crucial variables.

- **`Dockerfile`**: 
  - A file that is used to build the application's Docker image, enabling simple deployment and scalability in various settings.
  
- **`requirements.txt`**: 
  - A text file that ensures all relevant packages are installed and lists all the Python dependencies needed for the program to function.


## Additional Resources
Ethereum Beacon Chain Deposit Contract

Web3.py Documentation

Prometheus Documentation

Grafana Documentation
