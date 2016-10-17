---
layout: post
title: "Select Rows with Keys Matching Multiple Columns in Subquery"
--- 
When you query a database table using SQL, you might find the need to:
<br><br>
1. select rows from <b><u>table A</u></b> using a certain criteria (i.e., a
[<i>WHERE</i>](http://www.w3schools.com/sql/sql_where.asp) clause)
2. then, use one or more columns from result set (coming from the above query)
as a subquery to subselect from <b><u>table B</u></b>
<br><br>
You can do this quite easily in SQL 
<br><br>

{% highlight python %}
import pandas as pd
from pandasql import sqldf  # pip install pandasql from Yhat
{% endhighlight %}

<br><br>
{% highlight python %}
df_vals = pd.DataFrame({'key1': ['A', 'A','C', 'E', 'G'], 
                        'key2': ['B', 'Z', 'D', 'F', 'H'], 
                        'val': ['2','3','4','5','6']})

df_vals
{% endhighlight %}
<br><br>
<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>key1</th>
      <th>key2</th>
      <th>val</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>A</td>
      <td>B</td>
      <td>2</td>
    </tr>
    <tr>
      <th>1</th>
      <td>A</td>
      <td>Z</td>
      <td>3</td>
    </tr>
    <tr>
      <th>2</th>
      <td>C</td>
      <td>D</td>
      <td>4</td>
    </tr>
    <tr>
      <th>3</th>
      <td>E</td>
      <td>F</td>
      <td>5</td>
    </tr>
    <tr>
      <th>4</th>
      <td>G</td>
      <td>H</td>
      <td>6</td>
    </tr>
  </tbody>
</table>
</div>
<br><br>

{% highlight python %}
df_colors = pd.DataFrame({'key1': ['A', 'A','C', 'E', 'G'], 
                          'key2': ['B', 'Z', 'D', 'F', 'H'], 
                          'color': ['red','orange','yellow','green','blue']})

df_colors
{% endhighlight %}
<br><br>
<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>color</th>
      <th>key1</th>
      <th>key2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>red</td>
      <td>A</td>
      <td>B</td>
    </tr>
    <tr>
      <th>1</th>
      <td>orange</td>
      <td>A</td>
      <td>Z</td>
    </tr>
    <tr>
      <th>2</th>
      <td>yellow</td>
      <td>C</td>
      <td>D</td>
    </tr>
    <tr>
      <th>3</th>
      <td>green</td>
      <td>E</td>
      <td>F</td>
    </tr>
    <tr>
      <th>4</th>
      <td>blue</td>
      <td>G</td>
      <td>H</td>
    </tr>
  </tbody>
</table>
</div>
<br><br> 
So, if we wanted to grab all rows from df_colors where the value in df_vals is
inclusively between 2 and 6, then: 
<br><br>

{% highlight python %}
query = '''
        SELECT a.* FROM df_colors a
        INNER JOIN (
            SELECT key1, key2 FROM df_vals
            WHERE val > 2 and val < 6
        ) b
        ON a.key1 = b.key1 and a.key2 = b.key2
        '''
sqldf(query, locals())
{% endhighlight %}
<br><br>
<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>color</th>
      <th>key1</th>
      <th>key2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>orange</td>
      <td>A</td>
      <td>Z</td>
    </tr>
    <tr>
      <th>1</th>
      <td>yellow</td>
      <td>C</td>
      <td>D</td>
    </tr>
    <tr>
      <th>2</th>
      <td>green</td>
      <td>E</td>
      <td>F</td>
    </tr>
  </tbody>
</table>
</div>
<br><br> 
Notice that the inner subquery produces the keys where the values are between 2
and 6 
<br><br>

{% highlight python %}
query = '''
        SELECT key1, key2 FROM df_vals
        WHERE val > 2 and val < 6
        '''
sqldf(query, locals())
{% endhighlight %}
<br><br>
<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>key1</th>
      <th>key2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>A</td>
      <td>Z</td>
    </tr>
    <tr>
      <th>1</th>
      <td>C</td>
      <td>D</td>
    </tr>
    <tr>
      <th>2</th>
      <td>E</td>
      <td>F</td>
    </tr>
  </tbody>
</table>
</div>
<br><br> 
Then, each <b><u>pair</u></b> of keys are used to subselect rows from df_colors.
So, the <i>ON</i> keyword:
<br><br>
1. Grabs the <b><u>first</u></b> pair of keys (A, B) from df_colors and compares
them to each pair of keys returned by the subquery [(A, Z), (C,D), (E, F)]
2. If there is a match, then that row from df_colors is returned
3. This process (Steps 1-2) is repeated for the remaining rows in df_colors [(A,
Z), (C, D), (E, F), (G, H)] 
<br><br>
The query above is equivalent to the following: 
<br><br>

{% highlight python %}
query = """
        SELECT a.* from df_colors a
        WHERE (a.key1, a.key2) in (
            SELECT key1, key2 from df_vals where val > 2 and val < 6
        ) 
        """
{% endhighlight %}
<br><br> 
Note: This latter query doesn't work in sqlite3 since tuples aren't supported
but it should work fine for a real database. Note that it might be slower than
the first query and is a bit less obvious. So, it is advised that you stick with
the first query. 
<br><br>  

{% highlight python %}

{% endhighlight %}
