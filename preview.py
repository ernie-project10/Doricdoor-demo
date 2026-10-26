from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import threading
import webbrowser

root = Path(__file__).resolve().parent
handler = partial(SimpleHTTPRequestHandler, directory=str(root))
server = None
for port in range(8765, 8796):
    try:
        server = ThreadingHTTPServer(("127.0.0.1", port), handler)
        break
    except OSError:
        continue
if server is None:
    raise SystemExit("No available preview port. Close another preview and try again.")
url = f"http://127.0.0.1:{server.server_port}/"
print("Home:      " + url, flush=True)
print("ME Series: " + url + "collections/me-series/", flush=True)
print("Keep this window open. Press Ctrl+C to stop the preview.", flush=True)
thread = threading.Thread(target=server.serve_forever, daemon=True)
thread.start()
try:
    webbrowser.open_new_tab(url)
    thread.join()
except KeyboardInterrupt:
    pass
finally:
    server.shutdown()
    server.server_close()
