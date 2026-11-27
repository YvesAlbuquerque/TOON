import ipaddress
import json
import socket
import time

from tinytroupe.agent import TinyPerson

_original_connect = socket.socket.connect
_connections = []


def _loopback_only(sock, address):
    host = address[0] if isinstance(address, tuple) else address
    try:
        local = ipaddress.ip_address(host).is_loopback
    except ValueError:
        local = host == "localhost"
    if not local:
        raise RuntimeError(f"External connection blocked: {host}")
    _connections.append(str(host))
    return _original_connect(sock, address)


socket.socket.connect = _loopback_only

PITCH = "Run an eccentric cartoon studio across history, manage recurring creators, and publish works you can read or watch."
NAMES = [
    ("studio_tycoon", "T.O.O.N.: Studio Tycoon"),
    ("creative_studio", "T.O.O.N.: Creative Studio"),
    ("cartoon_tycoon", "T.O.O.N.: Cartoon Tycoon"),
    ("office_of_nonsense", "T.O.O.N. — The Office Of Nonsense"),
]
PERSONAS = [
    ("management_player", "You play management simulations and want clear decisions with visible consequences."),
    ("creative_media_player", "You enjoy comics, animation and creative tools, but dislike generic business spreadsheets."),
]


def run():
    rows = []
    for persona_id, context in PERSONAS:
        for candidate_id, candidate in NAMES:
            person = TinyPerson(f"{persona_id}_{candidate_id}")
            person.define("occupation", {"title": "game player", "description": context})
            person.define("personality", {"traits": ["Answer briefly and critically.", "Separate management from creative authorship."]})
            question = (
                f'Imagine a store page titled "{candidate}" with this pitch: "{PITCH}" '
                "In one sentence, what would you do in the game, and what would you expect to create?"
            )
            started = time.perf_counter()
            row = {"persona": persona_id, "candidate": candidate_id}
            try:
                person.listen(question, communication_display=False)
                actions = person.act(until_done=False, n=1, return_actions=True, communication_display=False)
                row.update({"status": "ok", "elapsed_seconds": round(time.perf_counter() - started, 2), "actions": actions})
            except Exception as exc:
                row.update({"status": "error", "elapsed_seconds": round(time.perf_counter() - started, 2), "error": f"{type(exc).__name__}: {exc}"})
            rows.append(row)
    print(json.dumps({"connections": _connections, "rows": rows}, ensure_ascii=False, default=str))


if __name__ == "__main__":
    run()
