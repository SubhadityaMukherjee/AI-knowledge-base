#%%
import os
from glob import glob
from pathlib import Path
from tqdm import tqdm
import re
#%%
main_dir = Path("./docs/")
# %%
files = glob(str(main_dir) + "/**/*.md", recursive=True)
files.sort()
#%%
files
# %%

for i in files:
    line_end = ""
    with open(i, "r") as f:
        text = f.readlines()
        for line in text:
            if "## Backlinks" in line:
                break
            else:
                line_end += line
    line_end += "\n\n"
    print(line_end)
    # break
    with open(i, "w+") as f:
        f.write(line_end)
    # break

# %%
