# -*- coding: utf-8 -*-

import os
import datetime


def new_post():
    """Creates a empty post file"""
    currentDT = datetime.datetime.now()
    title = "Title: Blank Post"
    dtvalue = "Date: {}".format(currentDT.strftime("%Y-%m-%d %H:%M"))
    cat = "Category: Holder"
    tags = "Tags: Holder"
    summary = "Summary: summary."
    author = "Summary: Laird Streak"
    line_list = [title, dtvalue, cat, tags, summary, author]
    with open("content/post_template.md", "w") as writer:
        for item in line_list:
            writer.write("%s\n" % item)


if __name__ == "__main__":
    new_post()
