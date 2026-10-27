#Alle veelgebruikte libraries en Rich-componenten zijn gecentraliseerd in m00_imports.py. Hierdoor worden dubbele imports voorkomen en blijft de code in de overige modules overzichtelijk.

import json
import requests
import webbrowser
from urllib.parse import quote_plus
import logging
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()