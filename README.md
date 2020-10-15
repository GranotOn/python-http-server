# Python http server

A simple http server, opening a TCP socket and using the `SimpleHttpRequestHandler` module.    
Using `urllib.parse` parses incoming get requests and logs them using `pprint`

## Usage

```
git clone https://github.com/OwenGranot
cd python-http-server
python3 server.py
```

Then send get request to `localhost:8080` or change port if needed.
