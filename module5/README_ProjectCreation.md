# Notes for Bruin Project
* Install bruin using the command `curl -LsSf https://getbruin.com/install/cli | sh`
* Add the Bruin extension in VSCode
* Initialize bruin zoomcamp project using the command `bruin init zoomcamp`
* Adding Bruin MCP
    * Goto `~/.vscode-server/data/User/mcp.json`
    * add the below to the json file
    ```json
    {
    "servers": 
            {
            "bruin":{
                    "command": "bruin",
                    "args": ["mcp"]
                    }   
            }
    }
    ```
* Modify the following files in order
    1. [bruin.yml](./zoomcamp/.bruin.yml) file (move it here if not at the right location)
    2. [pipeline.yml](./zoomcamp/pipeline/pipeline.yml)
    3. [trips.py](./zoomcamp/pipeline/assets/ingestion/trips.py)