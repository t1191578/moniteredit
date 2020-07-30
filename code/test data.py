import requests,json
r = requests.get('http://3.7.183.103:8080/metrics')
val = (json.dumps(r.text)).split('\\n')
print(val)
#val = val.split('\\n')
messagecontent = val[121:145:3]
d = dict(x.split(" ") for x in messagecontent)
print(d)

global:

  external_labels:
    dc: europe1
alerting:
  alert_relabel_configs:
    - source_labels: [dc]
      regex: (.+)\d+
      target_label: dc
  alertmanagers:
    - static_configs:
      - targets: ['prom1:9093', 'prom2:9093']

remote_write:
  - url: "http://15.206.42.79:8086/api/v1/prom/write?db=hpcmetrics"
  - url: "http://13.232.15.89:8080/receive"

remote_read:
  - url: "http://15.206.42.79:8086/api/v1/prom/read?db=hpcmetrics"

  -----------------

# my global config
global:
  scrape_interval:     15s # Set the scrape interval to every 15 seconds. Default is every 1 minute.
  evaluation_interval: 15s # Evaluate rules every 15 seconds. The default is every 1 minute.
  # scrape_timeout is set to the global default (10s).

# Alertmanager configuration
alerting:
  alertmanagers:
  - static_configs:
    - targets:
      # - alertmanager:9093

# Load rules once and periodically evaluate them according to the global 'evaluation_interval'.
rule_files:
  # - "first_rules.yml"
  # - "second_rules.yml"

# A scrape configuration containing exactly one endpoint to scrape:
# Here it's Prometheus itself.
scrape_configs:
  # The job name is added as a label `job=<job_name>` to any timeseries scraped from this config.
  - job_name: 'gcp_slurm_cluster'

    # metrics_path defaults to '/metrics'
    # scheme defaults to 'http'.

    static_configs:
    - targets: ['35.208.120.32:8080']
  - job_name: 'slurm2'
    static_configs:
    - targets: ['35.209.219.226:8080']
remote_write:
  - url: "http://15.206.42.79:8086/api/v1/prom/write?db=prom1metrics&u=pr&p=111"

remote_read:
  - url: "http://15.206.42.79:8086/api/v1/prom/read?db=prom1metrics&u=pr&p=111"

  -----------------------

  another yml

# my global config
global:
  scrape_interval:     15s # Set the scrape interval to every 15 seconds. Default is every 1 minute.
  evaluation_interval: 15s # Evaluate rules every 15 seconds. The default is every 1 minute.
  # scrape_timeout is set to the global default (10s).

  external_labels:
    dc: shahpcprom1

# Alertmanager configuration
alerting:
  alert_relabel_configs:
    - source_labels: [dc]
      regex: (.+)\d+
      target_label: dc
  alertmanagers:
    - static_configs:
      - targets: ['prom1:9093', 'prom2:9093']

# Load rules once and periodically evaluate them according to the global 'evaluation_interval'.
rule_files:
  # - "first_rules.yml"
  # - "second_rules.yml"

# A scrape configuration containing exactly one endpoint to scrape:
# Here it's Prometheus itself.
scrape_configs:
  # The job name is added as a label `job=<job_name>` to any timeseries scraped from this config.
  - job_name: 'prometheus'

    # metrics_path defaults to '/metrics'
    # scheme defaults to 'http'.

    static_configs:
    - targets: ['3.7.183.103:8080']

remote_write:
  - url: "http://15.206.42.79:8086/api/v1/prom/write?db=hpcmetrics&u=admin&p=123"
  - url: "http://13.232.15.89:8080/receive"

remote_read:
  - url: "http://15.206.42.79:8086/api/v1/prom/read?db=hpcmetrics"

steps in writing to db: if all cluster info write to same db 
create user  and password
grant auth to user -> eg: GRANT [READ,WRITE,ALL] ON prom1metrics TO 'pr'  , SHOW USERS  , REVOKE ALL PRIVILEGES FROM pr , CREATE USER pr WITH PASSWORD [REDACTED]  WITH ALL PRIVILEGES ,show databases
use those credentials and add write setting in promconf.yml


prom config:
Add external lable ,