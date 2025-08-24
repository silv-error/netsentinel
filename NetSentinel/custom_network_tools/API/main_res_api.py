from typing import List
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or specify: ["http://127.0.0.1:8000"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define the IncomingData model
class IncomingData(BaseModel):
    interface: str
    status: str
    ip: str
    protocol: str

# This will hold the received data
Received_data = []

@app.post("/api/send_status")
async def receive_status(data: List[IncomingData]):
    Received_data.clear()
    for item in data:
        Received_data.append({
            'interface': item.interface,
            'status': item.status,
            'ip': item.ip,
            'protocol': item.protocol
        })
        
        print("Received data:")
        print("Interface name:", item.interface)
        print("Status:", item.status)
        print("Ip:", item.ip)
        print("Protocol:", item.protocol)
        
    print("received data:",Received_data)

    # Return the received data
    return {"received": Received_data}


@app.get("/api/device_data")
async def device_dataget_status():
    print("received request")
    return Received_data
