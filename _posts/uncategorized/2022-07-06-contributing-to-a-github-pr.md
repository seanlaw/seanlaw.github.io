---
layout: post
title: Contributing to a Github PR
---

As an open source maintainer, I spend a good amount of time mentoring and providing feedback on pull requests (PRs). In some cases, providing comments to a PR may not be enough and I've had the occasional need to step in and make code contributions back to a contributor's PR. How to accomplish this was a mystery to me but these steps seemed to work well:

1. install the Github CLI (e.g., `conda install -c conda-forge gh`)
2. clone main (parent) repo (owned by me) (e.g., git clone https://github.com/TDAmeritrade/stumpy stumpy.git)
3. navigate to the PR page and copy the Github CLI command provided in the `<> Code>` button in the upper right  (e.g., `gh pr checkout 595`)
4. navigate to the cloned repo in your terminal & execute the CLI cmd
5. finally, change the code (it will already be on the right branch), commit, and push

And that's it! Thank you to all of those who chimed in with useful suggestions.
