from fastapi import FastAPI
from app.aws.ec2 import get_ec2_instances
from app.aws.billing import get_cost_data
from app.kubernetes.metrics import get_kubernetes_metrics

app = FastAPI()


@app.get("/")
def home():
    return {"message": "AI Multi-Cloud Cost Optimization Agent"}


@app.get("/ec2")
def ec2():
    return get_ec2_instances()


@app.get("/billing")
def billing():
    return get_cost_data()


@app.get("/kubernetes")
def kubernetes():
    return get_kubernetes_metrics()