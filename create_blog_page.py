# %%
from pathlib import Path
from glob import glob
from datetime import datetime
import re

from collections import OrderedDict

# %%


# %%


def format_today() -> str:
    """Get todays date in a nice format"""
    dt = datetime.today()
    day = dt.day
    if 11 <= day <= 13:
        suffix = "th"
    else:
        suffix = {1: "st", 2: "nd", 3: "rd"}.get(day % 10, "th")

    return dt.strftime(f"%A {day}{suffix} %B %Y, %a")


# %%
def parse_custom_date(line) -> datetime:
    """Get datetime object from obsidian date created field"""
    # Extract date part using regex
    match = re.search(r"(\w+)\s+(\d{1,2})(st|nd|rd|th)\s+(\w+)\s+(\d{4})", line)
    if not match:
        return datetime(3000, 10, 10)
    day = int(match.group(2))
    month = match.group(4)
    year = int(match.group(5))

    # Parse to datetime
    date_str = f"{day} {month} {year}"
    return datetime.strptime(date_str, "%d %B %Y")


# %%
def get_date_created(text) -> datetime:
    """Get date created line and return an absurd year (3000) if no date is found.
    This would let us sort by date even if it doesnt exist"""
    date_created: datetime = datetime(3000, 10, 10)
    for line in text:
        if "date created" in line:
            date_created = parse_custom_date(line)
            break
    return date_created


# %%
def get_first_few_lines(text, max_lines=5) -> str:
    """Get first couple of lines a little smartly. Check if theres a table of contents,
    get the text below it, check for H1 and apply logic based on this. Get a max of max_lines
    Snippets per article are in a "code" block
    Add some basic cleaning.
    """
    toc_line = None
    header_line = None

    for no, line in enumerate(text):
        if "```toc" in line:
            toc_line = no
            break

    for no, line in enumerate(text):
        if line.strip().startswith("#"):
            header_line = no
            break

    if toc_line is not None:
        snippet_start = toc_line + 3
        snippet = text[snippet_start : snippet_start + max_lines]
    elif header_line is not None:
        snippet_start = header_line + 1
        snippet = text[snippet_start : snippet_start + max_lines]
    else:
        snippet = text[:max_lines]

    cleaned = [line.strip().replace("```", "") for line in snippet]
    text_ret = "\n".join(cleaned) + "\n..."

    return f"\n```md\n{text_ret}\n```\n"


# %%
def should_skip(text):
    """If publish is false, then skip showing it here for obvious reasons."""
    return any('publish: "false"' in line or "publish: false" in line for line in text)


def generate_page(
    generated_page_template: str,
    all_articles,
    save_dir="docs/My Blogs.md",
) -> None:
    """
    Generate the final page and write it to save_dir
    """
    for article in all_articles:
        category_dict = OrderedDict()
        process_single_article(article, category_dict)
        sorted_category_dict = OrderedDict(
            sorted(category_dict.items(), key=lambda x: x[1]["date_created"])
        )

        for fle, info in sorted_category_dict.items():
            if not info.get("skip"):
                template = f"- [[{Path(fle).stem}]]\n{info.get('summary')}\n"
                generated_page_template += template

    with open(save_dir, "w+") as fp:
        fp.write(generated_page_template)


def process_single_article(article, category_dict):
    with open(article, "r") as fp:
        text = fp.readlines()
        date_created = get_date_created(text=text)
        summary = get_first_few_lines(text=text)
        skip_publish = should_skip(text=text)
        category_dict[article] = {
            "date_created": date_created,
            "summary": summary,
            "skip": skip_publish,
        }


if __name__ == "__main__":
    message = """
- Here are my articles sorted by recency. Feel free to click whatever seems interesting
- If you want to see something of a particular topic, send me an [email](mailto:msubhaditya@gmail.com)
"""

    generated_page_template: str = f"""---
title: Blogs
toc: true
tags: 
date modified: {format_today()}
date created: Wednesday 16th July 2025, Wed
---\n
# My Blogs
{message}
\n
    """
    path_to_articles = Path("docs/Articles/*/*.md")
    path_to_articles = glob(str(path_to_articles), recursive=True)
    filter_out = ["__Index", "index"]
    all_articles = [
        Path(file)
        for file in path_to_articles
        if not any([filter in file for filter in filter_out])
    ]

    generate_page(
        generated_page_template=generated_page_template,
        all_articles=all_articles,
        save_dir="docs/My Blogs.md",
    )
