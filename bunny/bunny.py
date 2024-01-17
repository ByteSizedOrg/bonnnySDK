import requests
import time
'''
The Main class for the LogBunny logger
'''
class BunnyLogger:
    def __init__(self,app_id,stream_id):
        self.app_id=app_id
        self.stream_id=stream_id
    
    async def _call_api(self,body):
        response=requests.post("https://sabertooth.fly.dev/ingest",data=body)
        return response.status_code
    
    async def info(self,data):
        body={
            "level":"info",
            "data":data,
            "appId":self.app_id,
            "streamId":self.stream_id,
            "timestamp":time.strftime("%Y-%m-%dT%H:%M:%S")
        }
        status=self._call_api(body)
        return status
    async def debug(self,data):
        body={
            "level":"debug",
            "data":data,
            "appId":self.app_id,
            "streamId":self.stream_id,
            "timestamp":time.strftime("%Y-%m-%dT%H:%M:%S")
        }
        status=self._call_api(body)
        return status
    async def error(self,data):
        body={
            "level":"error",
            "data":data,
            "appId":self.app_id,
            "streamId":self.stream_id,
            "timestamp":time.strftime("%Y-%m-%dT%H:%M:%S")
        }
        status=self._call_api(body)
        return status
    async def log(self,data):
        body={
            "level":"info",
            "data":data,
            "appId":self.app_id,
            "streamId":self.stream_id,
            "timestamp":time.strftime("%Y-%m-%dT%H:%M:%S")
        }
        status=self._call_api(body)
        return status