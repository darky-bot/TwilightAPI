from typing import Callable

from fastapi import APIRouter

from .base import BaseRouter

class RootRouter(BaseRouter):

    def __init__(self,
                 stop_command: Callable = None):

        self.router = APIRouter(
            tags=["Root"],
            prefix="/root"
        )

        self.stop_command = stop_command
        
        self.router.add_api_route("/ping", self.ping, methods=["GET"], 
                                  name="Pings the API",
                                  description="Method for API status check. Should return \"pong\" if alive.")
        self.router.add_api_route("/stop", self.stop, methods=["GET"],
                                  name="Stops the API",
                                  description="Stops all routers of API and API itself")
    
    async def ping(self) -> dict:
        return {"response": "Pong OwO!"}
    
    async def stop(self) -> dict:
        await self.stop_command()
        return {"response": "Shutdown initiated!"}