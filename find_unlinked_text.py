#%%
import os
import difflib
from pathlib import Path
from tqdm import tqdm
import re
#%%
files = os.listdir("docs/")
files_names= [i.split(".md")[0] for i in files if i.endswith(".md")]
full_paths = [Path("docs/") / f for f in files]
#%%

apps = []
full_paths = full_paths[:10]
for i in tqdm(full_paths, total=len(full_paths)):
    try:
        with open(i, "r") as f:
            text = f.read()
        # # only one word matches
        # for j in text:
        #     if len(j)> 3:
        #         diffs = [difflib.get_close_matches(j, files_names)]
        #         diffs = [x for x in diffs if len(x)>1]
        #         if len(diffs)>0:
        #             apps.append(diffs)
        # break
        for j in files_names:
            # regs = re.findall(re.escape(j), re.escape(text), re.IGNORECASE)
            # apps.append(regs)

    except IsADirectoryError:
        pass
    
print(apps)

# %%