# Get Started Airflow

A minimal Apache Airflow project to help beginners install, run, and understand their first DAG.

This project works on Linux and provides a simple "Hello World" DAG example.

---

# 📌 Requirements

- Linux (Debian/Ubuntu recommended)
- Python 3.10+
- pip & venv

---

# ⚙️ Installation (Step by Step)

## 1. Update system

```bash
sudo apt update
sudo apt upgrade -y
````

---

## 2. Install Python tools

```bash
sudo apt install python3 python3-pip python3-venv -y
```

Check:

```bash
python3 --version
pip3 --version
```

---

## 3. Clone project

```bash
git clone https://github.com/DavFilsDev/get-started-airflow.git
cd get-started-airflow
```

---

## 4. Create virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 5. Set Airflow home

This makes Airflow use this project folder:

```bash
export AIRFLOW_HOME=$(pwd)
echo $AIRFLOW_HOME
```

---

## 6. Install Apache Airflow

⚠️ Airflow requires constraints file.

Example (adjust Python version if needed):

```bash
export AIRFLOW_VERSION=2.10.5
export PYTHON_VERSION=3.12

export CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"

pip install "apache-airflow==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"
```

---

## 7. Initialize database

```bash
airflow db reset
```

Type `y` when asked.

---

## 8. Create admin user

If `airflow standalone` does NOT create it automatically, run:

```bash
airflow users create \
  --username admin \
  --firstname Admin \
  --lastname User \
  --role Admin \
  --email admin@example.com \
  --password admin
```

---

## 9. Run Airflow

```bash
airflow standalone
```

---

# 🌐 Access UI

Open browser:

```
http://localhost:8080
```

Login:

* username: admin
* password: admin

👉 If you don't know credentials:
Check terminal logs after `airflow standalone`.

---

# 📊 First DAG

This project contains a simple DAG:

```
dags/hello_world.py
```

It prints:

```
Hello Airflow 👋
```

---

# 🧪 How to test

1. Open Airflow UI
2. Enable DAG `hello_world`
3. Click "Trigger"
4. Go to task logs
5. See output

---