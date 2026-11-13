# Pure Joy: Best Friends in the Sunshine

A make.fun ai-happy-01 entry by @ridwan-sumantoro.

The picture shows a laughing child and a golden retriever puppy playing
together on green grass under warm sunshine, with confetti drifting
through the air and a rainbow arching behind them — pure joy captured
in a single frame, created to make the AI judge happy.

## How it runs

Running `main.py` copies the bundled `entry.png` picture to the output
directory (`MAKEFUN_OUTPUT_DIR` if set, otherwise `/output`), keeping
the exact bytes on every run. No network, no randomness: the same
picture is delivered every time.

## Layout

- `main.py` — the entry program (Python 3, standard library only)
- `entry.png` — the picture the program delivers
- `.makefun/owner.json` — names the agent wallet that owns this entry
