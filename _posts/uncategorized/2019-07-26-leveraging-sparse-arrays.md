---
layout: post
title: "Leveraging Sparse Arrays for Large-ish (Feature) Data Sets"
--- 

When building a machine learning model, you'll often have your feature data
stored in one or more database tables (e.g., with a couple of million rows and
maybe a thousand columns) where each row represents, say, an individual user and
each column represents some feature that you've engineered (i.e., number of
logins to your site, number of daily purchases, number of ads clicked on, 52
consecutive columns storing a weekly moving average over a year, etc). Since
storage is cheap and you can't afford to pay for a compute cluster, your
instinct might be to download the full table onto your laptop as a quick and
dirty CSV file or, possibly, in a more portable and compact parquet format.
However, depending on your local computer hardware, trying to load that full
data set into a Pandas DataFrame might consume all of your memory and cause your
system to grind to a halt!
<br><br>
Luckily, there is one approach that a lot of people often overlook but that
might work wonderfully for you. The secret is to exploit the inherent sparsity
that likely exists within your large data set!
<!--more-->
As an illustrative example, let's consider the following list of ones and zeros:
<br><br>
`[0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]`
<br><br>
To capture all of the information to represent this list, all that you really
need is:
<br><br>
1. The total length of the list
2. The exact position of each `1` (the position of each `0` is implied)
<br><br>
In other words, since the majority of the list is full of zeros, we can start by
assuming that the entire list is full of zeros with the exception of the
locations of the `1`s. In doing so, we end up only needing to record a few bits
of information and thereby saving us a ton of memory to do other interesting
things. The number of nonzero elements that exist in your matrix/array also
defines the `density` of your matrix. That is, the more nonzero elements that
you have (relative to the total number of elements) then the higher the density.
A sparse matrix/array would have very low density (i.e., less than 25% dense)
but, in the case of machine learning, you run the risk of not having enough
information to learn from if your matrix/array is too sparse (i.e., less than 5%
dense). This philisophical discussion is probably beyond the scope of this blog
post, which is to explain how to take your data and to create a sparse
matrix/array that can be used for building a machine learning model.
<br><br>
In fact, SciPy already offers fantastic support for building your own [sparse
matrices](https://docs.scipy.org/doc/scipy/reference/sparse.html). However, to
future-proof ourselves from a soon-to-be deprecated 2D numpy matrix format,
we'll be leveraging the [PyData
Sparse](https://sparse.pydata.org/en/latest/index.html) package for all of our
sparse nd-array needs. So, in places below where you see "sparse matrix", know
that we really mean a "2D array" but, unlike a matrix, the array can be
generalized to higher dimensions. 
<br><br>
## So What?
<br><br>
If you already have your data in hand then, most of the time, converting that
numpy array or pandas dataframe into a sparse matrix is pretty trivial. However,
where things get really tricky is when your data is stored within one giant
table/file that you can't load into memory all at once or it is stored across
multiple medium sized tables that you'll then need to figure out how to stitch
back together in Python. In the latter case, each chunk/table/file will contain
the same number of rows (i.e., each row represents the same user) but each
chunk/table/file will only contain a different subset of feature columns.
<br><br>
So, the pseudocode for converting this data into a sparse matrix might look
something like:
<br><br>
{% highlight python %}
sparse_matrix_list = []
db_cnxn = connect_to_db()
for chunk in db_cnxn.get(chunks):
    sparse_chunk = convert_chunk_to_sparse(chunk)
    sparse_matrix_list.append(sparse_chunk)
{% endhighlight %}
<br><br>
At first glance, this seems pretty straightforward. You retrieve only one chunk
at a time, process each chunk, convert that chunk into a sparse matrix, and
append it to a growing list so that it can be combined into a single large
sparse matrix. But once you dig into it, you'll discover all the ways that
things can go wrong! Below, we'll show you one relatively clean approach that
will help to keep everything in order. 
<br><br>
## Getting Started 
<br><br>  
{% highlight python %}
import sparse
import pandas as pd
import numpy as np
{% endhighlight %}
<br><br>
## Large Wide Data
<br><br>
Let's pretend that the dataframe below represents our large data which is stored
in some remote database or chunked up. Remember, since the data is "big", the
database only allows you to fetch, say, five columns of data at a time and,
realistically, you don't want to have to write any of this data to disk if at
all possible. 
<br><br>
{% highlight python %}
all_df = pd.DataFrame([['x', 1, 2, 3, 6, 0, 0, 7, 0, 0], 
                       ['y', 2, 3, 0, 0, 0, 4, 8, 0, 5], 
                       ['z', 3, 0, 1, 0, 1, 2, 0, 0, 9], 
                       ['w', 0, 0, 0, 0, 3, 0, 1, 0, 0]], 
                      columns=['user_id', 
                               'feature_a', 
                               'feature_b', 
                               'feature_c', 
                               'feature_d', 
                               'feature_e', 
                               'feature_f', 
                               'feature_g', 
                               'feature_h', 
                               'feature_i'])
all_df
{% endhighlight %}
<br><br>
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>user_id</th>
      <th>feature_a</th>
      <th>feature_b</th>
      <th>feature_c</th>
      <th>feature_d</th>
      <th>feature_e</th>
      <th>feature_f</th>
      <th>feature_g</th>
      <th>feature_h</th>
      <th>feature_i</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>x</td>
      <td>1</td>
      <td>2</td>
      <td>3</td>
      <td>6</td>
      <td>0</td>
      <td>0</td>
      <td>7</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>y</td>
      <td>2</td>
      <td>3</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>4</td>
      <td>8</td>
      <td>0</td>
      <td>5</td>
    </tr>
    <tr>
      <th>2</th>
      <td>z</td>
      <td>3</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>9</td>
    </tr>
    <tr>
      <th>3</th>
      <td>w</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>
<br><br>
## Mimic a Chunked Data Source
<br><br>
Here, we use a Python generator to pretend like we are accessing our fictitious
database one subset of columns at a time. But, in the real world, this will be
replaced by your database connection of choice. 
<br><br>
{% highlight python %}
def get_df_chunks(df):
    for chunk in [['user_id', 'feature_a', 'feature_b', 'feature_c'], 
                  ['user_id', 'feature_d', 'feature_e', 'feature_f', 'feature_g'], 
                  ['user_id', 'feature_h', 'feature_i']]:
        
        yield df[chunk]
{% endhighlight %}
<br><br>
Now, we could retrieve our first chunk directly from our databse but there are a
couple of issues:
<br><br>
1. The chunk itself is too big as it contains a lot of zeros
2. SciPy expects the data to be a long format instead of a wide format
<br><br>
So, we should try to get the database to do as much of the heavy lifting as
possible such as to pivot the wide tables into a long format and then to remove
all zeros and only return a long table with nonzero entries. Let's modify our
`get_df_chunks` generator from above to reflect this: 
<br><br>
{% highlight python %}
def get_df_chunks(df):
    for chunk in [['user_id', 'feature_a', 'feature_b', 'feature_c'], 
                  ['user_id', 'feature_d', 'feature_e', 'feature_f', 'feature_g'], 
                  ['user_id', 'feature_h', 'feature_i']]:
        
        long_df = df[chunk].melt(id_vars='user_id', var_name='feature')  # Pivot to long format
        long_df = long_df[long_df['value'] != 0]  # Remove nonzero elements
        
        yield long_df
{% endhighlight %}
<br><br>  
{% highlight python %}
for long_df in get_df_chunks(all_df):
    print(long_df, end="\n\n")
{% endhighlight %}
<br><br>
{% highlight python %}
       user_id    feature  value
    0        x  feature_a      1
    1        y  feature_a      2
    2        z  feature_a      3
    4        x  feature_b      2
    5        y  feature_b      3
    8        x  feature_c      3
    10       z  feature_c      1
    
       user_id    feature  value
    0        x  feature_d      6
    6        z  feature_e      1
    7        w  feature_e      3
    9        y  feature_f      4
    10       z  feature_f      2
    12       x  feature_g      7
    13       y  feature_g      8
    15       w  feature_g      1
    
      user_id    feature  value
    5       y  feature_i      5
    6       z  feature_i      9
{% endhighlight %}
<br><br>
Additionally, we'll want to convert the `user_id` and `feature` columns to a
categorical dtype and, to further reduce the memory footprint of our sparse
matrix, we'll force the `value` to be `np.float32`: 
<br><br>
{% highlight python %}
for long_df in get_df_chunks(all_df):
    long_df[['user_id', 'feature']] = long_df[['user_id', 'feature']].astype('category')
    long_df['value'] = long_df['value'].astype(np.float32)
    
    # Convert to sparse
{% endhighlight %}
<br><br> 
## Breaking Things Down
<br><br>
### Keeping Track of the Data Chunks
<br><br>
Since each `long_df` chunk may contain a different/overlapping set of `user_id`
and `feature`, we'll need to keep track of them in the order in which they are
observed so that we can cross reference our index-less sparse matrix with a nice
`user_id` or `feature` lookup table. So, as each chunk is retrieved, we'll need
to:
<br><br>
1. Start with an empty `user_id` list of categories `all_user_ids`
2. Get an ordered list of all of the `user_id` categories from the incoming
`long_df`
3. Append the incoming (ordered) `user_id` list to the (ordered) categories from
the existing `all_user_ids` list and remove redundant categories
4. Repeat steps 2-3 for all other chunks
<br><br>
This is also done for `feature` as well. Now, you might be tempted use Python's
built-in `set` operations to help identify a non-redundant list of `user_id` and
`feature` but this is insufficient since order isn't maintained! So, instead, we
initialize a couple of Pandas series for better bookkeeping: 
<br><br>
{% highlight python %}
all_user_ids = pd.Series([], dtype='category')
all_features = pd.Series([], dtype='category')
{% endhighlight %}
<br><br>
And we'll define a helper function to help us determine if we've already "seen"
a certain category type before. 
<br><br>  
{% highlight python %}
def return_new_categories(add_cat, old_cat):
    old_cat_set = set(old_cat)  # this reduces the lookup time from O(n) to O(1)
    return [cat for cat in add_cat if cat not in old_cat_set]
{% endhighlight %}
<br><br>
So, as each chunk comes in, we'll update the observed `all_user_ids` and
`all_features` categories on the fly: 
<br><br>
{% highlight python %}
all_user_ids = pd.Series([], dtype='category')
all_features = pd.Series([], dtype='category')

for i, long_df in enumerate(get_df_chunks(all_df)):
    
    long_df[['user_id', 'feature']] = long_df[['user_id', 'feature']].astype('category')
    long_df['value'] = long_df['value'].astype(np.float32)

    new_ids = return_new_categories(list(long_df['user_id'].cat.categories), list(all_user_ids.cat.categories))
    all_user_ids.cat.add_categories(new_ids, inplace=True)
    
    new_features = return_new_categories(list(long_df['feature'].cat.categories), list(all_features.cat.categories))
    all_features.cat.add_categories(new_features, inplace=True)
    
    long_df['user_id'].cat.set_categories(all_user_ids.cat.categories, inplace=True)
{% endhighlight %}
<br><br>
### Creating a Sparse Array Using the PyData Sparse Package
<br><br>
[Installing the PyData Sparse
package](https://sparse.pydata.org/en/latest/install.html) should be as
straigtforward as: 
<br><br>
{% highlight python %}
pip install sparse
{% endhighlight %}
<br><br>
According to their
[documentation](https://sparse.pydata.org/en/latest/construct.html), you can
construct a sparse nd-array (2D in our case) by doing: 
<br><br>
{% highlight python %}
import sparse

coords = [[0, 1, 2, 3, 4],
          [0, 1, 2, 3, 4]]
data = [10, 20, 30, 40, 50]
s = sparse.COO(coords, data, shape=(5, 5))

s.todense()
# array([[10,  0,  0,  0,  0],
#       [ 0, 20,  0,  0,  0],
#       [ 0,  0, 30,  0,  0],
#       [ 0,  0,  0, 40,  0],
#       [ 0,  0,  0,  0, 50]]) 
{% endhighlight %}
<br><br>
In our case, we can do something similar with our incoming long dataframe: 
<br><br>
{% highlight python %}
nrow = all_df.shape[0]  # This is the number of rows of user_id in the original dataframe
ncol = long_df['feature'].cat.categories.shape[0]  # This is the number of unique features in this long_df

coords = (long_df['user_id'].cat.codes.copy(), long_df['feature'].cat.codes.copy())
data = long_df['value']

some_sparse_array = sparse.COO(coords, data, shape=(nrow, ncol)).astype(np.float32)
{% endhighlight %}
<br><br> 
And, voila, we have sparse 2D array! And as we process each incoming new
`long_df`, we can add the new sparse array to our existing sparse array via the
`concatenate` [function](https://sparse.pydata.org/en/latest/generated/sparse.co
ncatenate.html#sparse.concatenate): 
<br><br>
{% highlight python %}
existing_sparse_array = sparse.concatenate([existing_sparse_array, new_sparse_array], axis=1) 
{% endhighlight %}
<br><br>
## Putting Things Altogether
<br><br>
This is the workhorse so please review it carefully. A lot of this stuff might
seem obvious or trivial but there are actually a lot of "gotchas" and one needs
to take care and be mindful of the pitfalls of their approach. The biggest thing
is making sure that the rows and columns our sparse array can be referenced
correctly after we've stitched things back together. 
<br><br> 
{% highlight python %}
all_user_ids = pd.Series([], dtype='category')
all_features = pd.Series([], dtype='category')

for i, long_df in enumerate(get_df_chunks(all_df)):
    
    long_df[['user_id', 'feature']] = long_df[['user_id', 'feature']].astype('category')
    long_df['value'] = long_df['value'].astype(np.float32)

    new_ids = return_new_categories(list(long_df['user_id'].cat.categories), list(all_user_ids.cat.categories))
    all_user_ids.cat.add_categories(new_ids, inplace=True)
    new_features = return_new_categories(list(long_df['feature'].cat.categories), list(all_features.cat.categories))
    all_features.cat.add_categories(new_features, inplace=True)
    
    long_df['user_id'].cat.set_categories(all_user_ids.cat.categories, inplace=True)
    
    nrow = all_df.shape[0]
    ncol = long_df['feature'].cat.categories.shape[0]
    
    coords = (long_df['user_id'].cat.codes.copy(), long_df['feature'].cat.codes.copy())
    data = long_df['value']
    
    new_sparse_array = sparse.COO(coords, data, shape=(nrow, ncol)).astype(np.float32)
    
    if i == 0:
        existing_sparse_array = new_sparse_array
    else:
        existing_sparse_array = sparse.concatenate([existing_sparse_array, new_sparse_array], axis=1)
{% endhighlight %}
<br><br>
Indeed, our final `existing_sparse_array` is sparse and has the correct
dimensions: 
<br><br>
{% highlight python %}
existing_sparse_array
{% endhighlight %}
<br><br> 
To confirm that our sparse array is the same as our original `all_df` dataframe,
we can convert it back to dense form: 
<br><br>  
{% highlight python %}
existing_sparse_array.todense()
{% endhighlight %}
<br><br> 
And we see that it is nearly identical to `all_df`:
<br><br>
{% highlight python %}
all_df
{% endhighlight %}
<br><br>
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>user_id</th>
      <th>feature_a</th>
      <th>feature_b</th>
      <th>feature_c</th>
      <th>feature_d</th>
      <th>feature_e</th>
      <th>feature_f</th>
      <th>feature_g</th>
      <th>feature_h</th>
      <th>feature_i</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>x</td>
      <td>1</td>
      <td>2</td>
      <td>3</td>
      <td>6</td>
      <td>0</td>
      <td>0</td>
      <td>7</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>y</td>
      <td>2</td>
      <td>3</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>4</td>
      <td>8</td>
      <td>0</td>
      <td>5</td>
    </tr>
    <tr>
      <th>2</th>
      <td>z</td>
      <td>3</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>9</td>
    </tr>
    <tr>
      <th>3</th>
      <td>w</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>
<br><br> 
The observant individual will notice that `existing_sparse_array` has a missing
column. That is, `feature_h`, which contains all zeros is completely missing and
this is by design since that column contains no useful information from which to
learn from. If you recall, this was handled earlier by our fake database
generator, `get_df_chunks`, when we removed all nonzero elements before
returning `long_df`: 
<br><br>
{% highlight python %}
long_df = long_df[long_df['value'] != 0]  # Remove nonzero elements
{% endhighlight %}
<br><br>
We can also check to make sure that our stored `all_features` categories did not
accidentally capture `feature_h` and that the order of the categories should be
retained: 
<br><br>
{% highlight python %}
all_features.cat.categories
{% endhighlight %}
<br><br>
Success! You can also access the ordered list of `all_user_ids` via: 
<br><br>
{% highlight python %}
all_user_ids.cat.categories
{% endhighlight %}
<br><br>
Or save the list to a CSV file: 
<br><br>
{% highlight python %}
all_user_ids.cat.categories.to_series().to_csv("all_user_ids.csv", header=False)
{% endhighlight %}
<br><br>
Finally, if you wanted to, say, build an scikit-learn or XGBoost model then all
you need to do is hand this sparse COO matrix over to the XGBoost model builder
in `Compressed Sparse Row` format just as if it were a dense `numpy` array: 
<br><br>
{% highlight python %}
clf.fit(existing_sparse_array.tocsr(), responses) 
{% endhighlight %}
<br><br>
## Conclusion
<br><br>
From our experience, and depending on your local hardware resources, we've been
able to leverage this approach for data that contain around a million rows x a
thousand features (or you can have many more rows if you decrease the number of
features by an order of magnitude). Additionally, if your data is even bigger
than this, then, depending on the type of model that you are trying to build,
you may be able to use the scikit-learn's `partial_fit` (or sometimes called
`warm_start`) function by breaking your data up into a smaller number of rows
and feeding the chunks back in an iterative fashion.
<br><br>
Hopefully, this approach will work for you as you venture down your data science
journey! Let me know what you think in the comments below. 
<br><br>
