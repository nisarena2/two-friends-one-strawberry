import os, shutil
from pathlib import Path

src = Path(__file__).with_name("entry.png")
out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
out.mkdir(parents=True, exist_ok=True)
shutil.copyfile(src, out / "entry.png")
