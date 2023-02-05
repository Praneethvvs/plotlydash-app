import sys
import traceback

from navbar import header
import logging
from content import *






content = html.Div(id="page-content", children=[])

app.layout = html.Div([
    dcc.Location(id="url"),
    header,
    content
])

if __name__ == "__main__":
    app.run_server(host='0.0.0.0',port=8050,debug=True)
