from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer


class Handler(SimpleHTTPRequestHandler):
    def guess_type(self, path):
        clean_path = path.split("?", 1)[0]
        if clean_path.endswith((".cache", ".appcache", ".manifest")):
            return "text/cache-manifest"
        if clean_path.endswith(".mjs"):
            return "text/javascript"
        if clean_path.endswith(".bin"):
            return "application/octet-stream"
        return super().guess_type(path)


if __name__ == "__main__":
    server = ThreadingHTTPServer(("0.0.0.0", 8000), Handler)
    print("Serving o2JB on http://0.0.0.0:8000/")
    server.serve_forever()
