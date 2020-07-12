from bravado.client import SwaggerClient
from typing import NewType

BitmexClient = NewType("BitmexClient", SwaggerClient)
