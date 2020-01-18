# counter-strike-kills-deaths
Inserts Counter-Strike kill and death data into an InfluxDB database. This is useful for visualization through Chronograf.

## Setup
- python3 -m venv /path/to/virtual/environment
- . venv_folder/bin/activate
- pip install -r requirements.txt
- download and upzip the tick stack sandbox https://github.com/influxdata/sandbox
- go to sandbox-master, run ./sandbox up
- to enter the InfluxDB CLI run influx in terminal
