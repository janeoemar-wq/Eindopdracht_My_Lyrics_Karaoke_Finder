import json
import requests
import musicbrainzngs

from datetime import datetime

from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from M04_Config import EMAIL

console = Console()