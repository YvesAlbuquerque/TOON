# Local synthetic-audience pilot

This directory contains a small, reproducible pre-production experiment for T.O.O.N. naming and positioning.

It is research tooling, not game runtime code. Synthetic agents are exploratory simulations and do not validate real market demand, legal name clearance, or player comprehension.

## Local setup

Use Python 3.11+, Ollama, and a virtual environment outside the repository:

```powershell
py -3.11 -m venv .venv-synthetic
$env:GIT_CONFIG_COUNT = '1'
$env:GIT_CONFIG_KEY_0 = 'core.longpaths'
$env:GIT_CONFIG_VALUE_0 = 'true'
.\.venv-synthetic\Scripts\python -m pip install "git+https://github.com/microsoft/TinyTroupe.git@a6244b358a1fe1c71bf751f7ba0f8dfa368ec5a4"
ollama pull qwen3:1.7b
$env:OPENAI_API_KEY = "ollama"
$env:NO_PROXY = "localhost,127.0.0.1"
```

Copy `config.example.ini` to `config.ini` beside the script. Do not commit `config.ini`, virtual environments, model weights, logs, or raw responses.

The tested local configuration used Ollama at `http://localhost:11434/v1`, Qwen3 1.7B Q4_K_M, one concurrent call, and disabled semantic-memory features. TinyTroupe's Ollama support is experimental. The model is an Apache-2.0 weight distribution; verify the model's current license and digest before reuse.

## Experiment boundary

The pilot compares four title hypotheses with identical pitch/questions:

- T.O.O.N.: Studio Tycoon
- T.O.O.N.: Creative Studio
- T.O.O.N.: Cartoon Tycoon
- T.O.O.N. — The Office Of Nonsense

The first pilot used two hypothesized personas and eight conditions. It produced structured output locally, but the responses showed repeated themes and are not evidence of preference. Do not calculate market shares, confidence intervals, TAM, or a winner from this experiment.

For evidence and installation history, see [issue #105](https://github.com/YvesAlbuquerque/TOON/issues/105).
