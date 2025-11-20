import sys
import socket

def print_usage():
    print("Usage: python rtsp_sdp_parser.py <server ip> <port> <url>")
    print("ex: python rtsp_sdp_parser.py rtsp://{server_ip}:{port}/live_st1")


def get_rtsp_describe(server_ip, port, url):
    url = f"rtsp://{server_ip}:{port}/{url}"

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((server_ip, port))

            req = (
                f"DESCRIBE {url} RTSP/1.0\r\n"
                f"CSeq: 1\r\n"
                f"Accept: application/sdp\r\n"
                f"\r\n"
            )

            s.send(req.encode("utf-8"))
            resp = s.recv(4096).decode("utf-8", errors="ignore")

            print("=== RTSP Response ===")
            print(resp)

    except Exception as e:
        print(f"Error: {e}")
        return


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print_usage()
        sys.exit(1)

    server_ip = sys.argv[1]
    port = int(sys.argv[2])
    url = sys.argv[3]
    get_rtsp_describe(server_ip, port, url)
    