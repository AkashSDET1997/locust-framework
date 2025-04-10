How to Run
🧪 Option 1: Interactive Mode
locust -f locustfile.py --host=https://reqres.in
Then go to http://localhost:8089.

⚙️ Option 2: Headless Mode
locust -f locustfile.py \
  --host=https://reqres.in \
  --users 10 \
  --spawn-rate 2 \
  --run-time 1m \
  --csv=reports/load_test \
  --html=reports/report.html \
  --headless


💾 Command Line Config
You can pass custom configurations like this:
locust -f locustfile.py --host=https://api.yourdomain.com --env=staging
📈 InfluxDB/Grafana Integration
If monitoring is set up:
locust -f locustfile.py \
  --host=https://reqres.in \
  --influx-host=http://localhost:8086 \
  --influx-database=locustdb \
  --influx-user=admin \
  --influx-password=admin \
  --headless -u 10 -r 2 \
  --run-time 1m


📦 Installation
pip install -r requirements.txt