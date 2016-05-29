---
layout: post
title: "Pandas Split-Apply-Combine"
--- 
There are times when I want to use split-apply-combine to save the results of a
groupby to a json file while preserving the resulting column values as a list.
Before we start, let's import Pandas and generate a dataframe with some example
email data 
<br><br>

## Import Pandas and Create an Email DataFrame 
<br><br>
{% highlight python %}
import pandas as pd
import numpy as np
{% endhighlight %}
{% highlight python %}
df = pd.DataFrame({'Sender': ['Alice', 'Alice', 'Bob', 'Carl', 'Bob', 'Alice'],
                   'Receiver': ['David', 'Eric', 'Frank', 'Ginger', 'Holly', 'Ingrid'],
                   'Emails': [9, 3, 5, 1, 6, 7]
                  })
df
{% endhighlight %}
<!--more-->
<br><br>
<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Emails</th>
      <th>Receiver</th>
      <th>Sender</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>9</td>
      <td>David</td>
      <td>Alice</td>
    </tr>
    <tr>
      <th>1</th>
      <td>3</td>
      <td>Eric</td>
      <td>Alice</td>
    </tr>
    <tr>
      <th>2</th>
      <td>5</td>
      <td>Frank</td>
      <td>Bob</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1</td>
      <td>Ginger</td>
      <td>Carl</td>
    </tr>
    <tr>
      <th>4</th>
      <td>6</td>
      <td>Holly</td>
      <td>Bob</td>
    </tr>
    <tr>
      <th>5</th>
      <td>7</td>
      <td>Ingrid</td>
      <td>Alice</td>
    </tr>
  </tbody>
</table>
</div>
<br><br>
 
## Purpose
<br><br>
Here, the goal is to generate a list of e-mail receivers for each sender. To
accomplish this, we can first group the data by sender: 
<br><br>
{% highlight python %}
grouped = df.groupby('Sender')
{% endhighlight %}
<br><br>
And if we examine the groups for each sender then we'll see the row indices that
are associated with each sender: 
<br><br>
{% highlight python %}
grouped.groups
{% endhighlight %}
{% highlight python %}
{'Alice': [0, 1, 5], 'Bob': [2, 4], 'Carl': [3]}
{% endhighlight %}
<br><br>
We usually follow a groupby call by aggregating data along the other columns.
For example: 
<br><br>
{% highlight python %}
grouped.aggregate(np.sum)
{% endhighlight %}
<br><br>
<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Emails</th>
    </tr>
    <tr>
      <th>Sender</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Alice</th>
      <td>19</td>
    </tr>
    <tr>
      <th>Bob</th>
      <td>11</td>
    </tr>
    <tr>
      <th>Carl</th>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>
<br><br> 
However, notice that the e-mail receiver column doesn't get aggregated since it
isn't obvious how to sum up text together or what that would even mean. In this
case, we could provide a custom aggregator that simply concatenates all of the
receivers into a single string. 
<br><br>
{% highlight python %}
grouped['Receiver'].agg(lambda x: x.sum())
{% endhighlight %}
<br><br> 
But how can we end up with a list of receivers? 
<br><br>

## The Secret Sauce 
<br><br> 
Well, we could take the custom aggregator a step further and have it return a
list instead of a concatenated string. 
<br><br>
{% highlight python %}
grouped['Receiver'].agg({'Receivers':(lambda x: list(x))})
{% endhighlight %}
<br><br>
<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Receivers</th>
    </tr>
    <tr>
      <th>Sender</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Alice</th>
      <td>[David, Eric, Ingrid]</td>
    </tr>
    <tr>
      <th>Bob</th>
      <td>[Frank, Holly]</td>
    </tr>
    <tr>
      <th>Carl</th>
      <td>[Ginger]</td>
    </tr>
  </tbody>
</table>
</div>
<br><br>
But note that we've excluded the number of e-mails for clarity. Putting it all
together, we can incorporate all of the data and do something like this: 
<br><br>
{% highlight python %}
grouped.agg({'Receiver': {'Receiver_List': (lambda x: list(x))},
             'Emails': {'Total_Emails': np.sum}
            })
{% endhighlight %}
<br><br>
<div>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th>Emails</th>
      <th>Receiver</th>
    </tr>
    <tr>
      <th></th>
      <th>Total_Emails</th>
      <th>Receiver_List</th>
    </tr>
    <tr>
      <th>Sender</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Alice</th>
      <td>19</td>
      <td>[David, Eric, Ingrid]</td>
    </tr>
    <tr>
      <th>Bob</th>
      <td>11</td>
      <td>[Frank, Holly]</td>
    </tr>
    <tr>
      <th>Carl</th>
      <td>1</td>
      <td>[Ginger]</td>
    </tr>
  </tbody>
</table>
</div>
<br><br>
Above, the `agg` function takes on the format `{column: {name: agg_func}}` where
`column` is the dataframe column, `name` is the column name of the resulting
aggregation result, and `agg_func` is the name of the aggregation function to
use. Note that we can simplify things by omitting the `name` completely and
breaking free of the inner `dict` with: 
<br><br>
{% highlight python %}
out = grouped.agg({'Receiver': (lambda x: list(x)),
                   'Emails': np.sum
                  })
out
{% endhighlight %}
<br><br>
<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Emails</th>
      <th>Receiver</th>
    </tr>
    <tr>
      <th>Sender</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Alice</th>
      <td>19</td>
      <td>[David, Eric, Ingrid]</td>
    </tr>
    <tr>
      <th>Bob</th>
      <td>11</td>
      <td>[Frank, Holly]</td>
    </tr>
    <tr>
      <th>Carl</th>
      <td>1</td>
      <td>[Ginger]</td>
    </tr>
  </tbody>
</table>
</div>
<br><br>
Finally, the dataframe can be written to a json file 
<br><br>
{% highlight python %}
out.to_json('easy_as_pie.json')
{% endhighlight %}
 <br><br>
{% highlight python %}
{"Emails": {"Alice":19,"Bob":11,"Carl":1},
 "Receiver": {"Alice":["David","Eric","Ingrid"],
              "Bob":["Frank","Holly"],
              "Carl":["Ginger"]}
}
{% endhighlight %}
<br><br>

## Easy-As-Pie!
