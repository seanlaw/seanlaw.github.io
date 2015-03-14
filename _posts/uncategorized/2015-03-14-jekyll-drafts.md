---
layout: post
title: Drafts in Jekyll
---

<!--
<img class="img-left" align="left" src="{{ site.url }}/images/">
-->

The great thing about Jekyll is that you can start writing a draft without publishing it and still be able to see the post locally.

1. Create a draft directory called `_drafts` in the root directory
2. Create a new post in this directory but omit the date in the file name
3. Serve up the page locally using `jekyll serve --drafts`

Then, Jekyll will automatically adjust the date of the post to today's and display the post as the most recent post. Note that this post won't be displayed on your github pages since they aren't using the `--drafts` option. So, you'll be able to save all of your drafts without worrying about them showing up on your live site.  Once the post is ready for the prime time, then simply move it over to the `_posts` directory and prepend a date to the file name. That's it!
