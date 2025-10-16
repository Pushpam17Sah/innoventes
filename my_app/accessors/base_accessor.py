import logging
logger = logging.getLogger(__name__)


class HttpRequest:
    def __init__(self, builder):
        self.url = builder.url
        self.method = builder.method
        self.headers = builder.headers
        self.query_params = builder.query_params
        self.body = builder.body
        self.timeout = builder.timeout

    def __str__(self):
        return (f"HttpRequest(url={self.url}, method={self.method}, " f"headers={self.headers}, "
                f"query_params={self.query_params}, body={self.body}, "
                f"timeout={self.timeout})")

    def execute(self):
        """Execute the HTTP request and return actual response"""
        import requests
        from urllib.parse import urlencode
        # Build full URL with query params
        full_url = self.url
        if self.query_params:
            full_url = f"{self.url}?{urlencode(self.query_params)}"
        try:
            # Make actual HTTP request
            response = requests.request(
                method=self.method,
                url=full_url,
                headers=self.headers,
                json=self.body if self.body else None,
                timeout=self.timeout / 1000  # Convert ms to seconds
            )
            # Return JSON response if possible
            if response.headers.get('content-type', '').startswith('application/json'):
                api_response = response.json()
                logger.info(f"Response from: {full_url} - {api_response}")
                return api_response
            else:
                api_response = response.text
                logger.info(f"Response from: {full_url} - {api_response}")
                return api_response
        except Exception as e:
            logger.error(f"Request failed: {str(e)}")
            return {"error": str(e)}


class Builder:
    def __init__(self, url):
        self.url = url
        self.method = "GET"
        self.headers = {}
        self.query_params = {}
        self.body = None
        self.timeout = 30000

    def set_method(self, method):
        self.method = method
        return self

    def add_header(self, key, value):
        self.headers[key] = value
        return self

    def add_query_param(self, key, value):
        self.query_params[key] = value
        return self

    def body(self, body):
        self.body = body
        return self

    def timeout(self, timeout):
        self.timeout = timeout
        return self

    def build(self):
        return HttpRequest(self)
