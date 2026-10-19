# reaction-speed-clicker
A Python automation script that automatically clicks the screen when a specific color changes, built for passing reaction speed tests.

# reaction-speed-clicker

A Python script that clicks the moment the pixel under your mouse turns a target color. It was built for online reaction speed tests.

> Work in progress: a GUI and a standalone .exe are planned.

## Setup

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Usage

```powershell
python click.py
```

Hover over the area that changes color, then start the test. To stop, press `Ctrl+C` or move the mouse into a screen corner.

Target colors are set in `TARGET_COLORS` at the top of `click.py`.
