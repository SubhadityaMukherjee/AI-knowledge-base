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
dict_files = {x: [] for x in files}
print(len(files))
# %%
