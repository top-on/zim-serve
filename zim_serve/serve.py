import subprocess
import webbrowser
from pathlib import Path


ZIM_PATH = Path("~/Downloads/wikipedia_en_100_mini_2022-10.zim")
SERVER_URL = "http://172.17.0.2:8080"

docker_run = f"""
    docker run -d \
    --name kiwix-serve \
    -v {ZIM_PATH}:/data/{ZIM_PATH.name} \
    kiwix/kiwix-serve \
    {ZIM_PATH.name}
    """
# TODO: add --rm??

subprocess.call(docker_run, shell=True)

webbrowser.open(SERVER_URL)
