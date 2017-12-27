---
layout: post
title: "I'm Melting! From Wide to Long Format and Quarterly Groupby"
--- 
Recently, a colleague of mine asked me how one might go about taking a dataset
that is in wide format and converting it into long format so that you could then
perform some groupby operations by quarter.
<br><br>
Here's a quick example to illustrate one way to go about this using the Pandas
melt function. 
<br><br>
 
## Getting Started
<br><br>
Let's import the Pandas package 
<br><br>
{% highlight python %}
import pandas as pd
{% endhighlight %}
 
## Load Some Data
<br><br>
First, we'll create a fake dataframe that contains the name of a state and city
along with some data for each month in the year 2000. For simplicity, imagine
that the data are the number of Canadians spotted eating poutine. 
<br><br>

{% highlight python %}
df = pd.DataFrame([['NY', 'New York', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], 
                   ['MI', 'Ann Arbor', 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17],
                   ['OR', 'Portland', 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21],
                  ],
                  columns=['state', 'city', 
                           '2000-01', '2000-02', '2000-03', '2000-04', '2000-05', '2000-06',
                           '2000-07', '2000-08', '2000-09', '2000-10', '2000-11', '2000-12',
                           '2001-01'
                          ])
df
{% endhighlight %}
<!--more-->
<br><br>
<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>state</th>
      <th>city</th>
      <th>2000-01</th>
      <th>2000-02</th>
      <th>2000-03</th>
      <th>2000-04</th>
      <th>2000-05</th>
      <th>2000-06</th>
      <th>2000-07</th>
      <th>2000-08</th>
      <th>2000-09</th>
      <th>2000-10</th>
      <th>2000-11</th>
      <th>2000-12</th>
      <th>2001-01</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>NY</td>
      <td>New York</td>
      <td>1</td>
      <td>2</td>
      <td>3</td>
      <td>4</td>
      <td>5</td>
      <td>6</td>
      <td>7</td>
      <td>8</td>
      <td>9</td>
      <td>10</td>
      <td>11</td>
      <td>12</td>
      <td>13</td>
    </tr>
    <tr>
      <th>1</th>
      <td>MI</td>
      <td>Ann Arbor</td>
      <td>5</td>
      <td>6</td>
      <td>7</td>
      <td>8</td>
      <td>9</td>
      <td>10</td>
      <td>11</td>
      <td>12</td>
      <td>13</td>
      <td>14</td>
      <td>15</td>
      <td>16</td>
      <td>17</td>
    </tr>
    <tr>
      <th>2</th>
      <td>OR</td>
      <td>Portland</td>
      <td>9</td>
      <td>10</td>
      <td>11</td>
      <td>12</td>
      <td>13</td>
      <td>14</td>
      <td>15</td>
      <td>16</td>
      <td>17</td>
      <td>18</td>
      <td>19</td>
      <td>20</td>
      <td>21</td>
    </tr>
  </tbody>
</table>
</div>
<br><br>
 
## The Goal
<br><br>
The problem was to take this dataset and try to find the average number of
Canadians eating poutine in each city and state for each quarter in the year
2000.
<br><br>
First, we need to convert the original dataframe into long format and then make
sure that the resulting months are understood to be a datetime column. 
<br><br>
{% highlight python %}
long_df = pd.melt(df, id_vars=['state', 'city'], var_name='month', value_name='number of poutine eaters')
long_df['month'] = pd.to_datetime(long_df['month'])
long_df
{% endhighlight %}
<br><br>
<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>state</th>
      <th>city</th>
      <th>month</th>
      <th>number of poutine eaters</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>NY</td>
      <td>New York</td>
      <td>2000-01-01</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>MI</td>
      <td>Ann Arbor</td>
      <td>2000-01-01</td>
      <td>5</td>
    </tr>
    <tr>
      <th>2</th>
      <td>OR</td>
      <td>Portland</td>
      <td>2000-01-01</td>
      <td>9</td>
    </tr>
    <tr>
      <th>3</th>
      <td>NY</td>
      <td>New York</td>
      <td>2000-02-01</td>
      <td>2</td>
    </tr>
    <tr>
      <th>4</th>
      <td>MI</td>
      <td>Ann Arbor</td>
      <td>2000-02-01</td>
      <td>6</td>
    </tr>
    <tr>
      <th>5</th>
      <td>OR</td>
      <td>Portland</td>
      <td>2000-02-01</td>
      <td>10</td>
    </tr>
    <tr>
      <th>6</th>
      <td>NY</td>
      <td>New York</td>
      <td>2000-03-01</td>
      <td>3</td>
    </tr>
    <tr>
      <th>7</th>
      <td>MI</td>
      <td>Ann Arbor</td>
      <td>2000-03-01</td>
      <td>7</td>
    </tr>
    <tr>
      <th>8</th>
      <td>OR</td>
      <td>Portland</td>
      <td>2000-03-01</td>
      <td>11</td>
    </tr>
    <tr>
      <th>9</th>
      <td>NY</td>
      <td>New York</td>
      <td>2000-04-01</td>
      <td>4</td>
    </tr>
    <tr>
      <th>10</th>
      <td>MI</td>
      <td>Ann Arbor</td>
      <td>2000-04-01</td>
      <td>8</td>
    </tr>
    <tr>
      <th>11</th>
      <td>OR</td>
      <td>Portland</td>
      <td>2000-04-01</td>
      <td>12</td>
    </tr>
    <tr>
      <th>12</th>
      <td>NY</td>
      <td>New York</td>
      <td>2000-05-01</td>
      <td>5</td>
    </tr>
    <tr>
      <th>13</th>
      <td>MI</td>
      <td>Ann Arbor</td>
      <td>2000-05-01</td>
      <td>9</td>
    </tr>
    <tr>
      <th>14</th>
      <td>OR</td>
      <td>Portland</td>
      <td>2000-05-01</td>
      <td>13</td>
    </tr>
    <tr>
      <th>15</th>
      <td>NY</td>
      <td>New York</td>
      <td>2000-06-01</td>
      <td>6</td>
    </tr>
    <tr>
      <th>16</th>
      <td>MI</td>
      <td>Ann Arbor</td>
      <td>2000-06-01</td>
      <td>10</td>
    </tr>
    <tr>
      <th>17</th>
      <td>OR</td>
      <td>Portland</td>
      <td>2000-06-01</td>
      <td>14</td>
    </tr>
    <tr>
      <th>18</th>
      <td>NY</td>
      <td>New York</td>
      <td>2000-07-01</td>
      <td>7</td>
    </tr>
    <tr>
      <th>19</th>
      <td>MI</td>
      <td>Ann Arbor</td>
      <td>2000-07-01</td>
      <td>11</td>
    </tr>
    <tr>
      <th>20</th>
      <td>OR</td>
      <td>Portland</td>
      <td>2000-07-01</td>
      <td>15</td>
    </tr>
    <tr>
      <th>21</th>
      <td>NY</td>
      <td>New York</td>
      <td>2000-08-01</td>
      <td>8</td>
    </tr>
    <tr>
      <th>22</th>
      <td>MI</td>
      <td>Ann Arbor</td>
      <td>2000-08-01</td>
      <td>12</td>
    </tr>
    <tr>
      <th>23</th>
      <td>OR</td>
      <td>Portland</td>
      <td>2000-08-01</td>
      <td>16</td>
    </tr>
    <tr>
      <th>24</th>
      <td>NY</td>
      <td>New York</td>
      <td>2000-09-01</td>
      <td>9</td>
    </tr>
    <tr>
      <th>25</th>
      <td>MI</td>
      <td>Ann Arbor</td>
      <td>2000-09-01</td>
      <td>13</td>
    </tr>
    <tr>
      <th>26</th>
      <td>OR</td>
      <td>Portland</td>
      <td>2000-09-01</td>
      <td>17</td>
    </tr>
    <tr>
      <th>27</th>
      <td>NY</td>
      <td>New York</td>
      <td>2000-10-01</td>
      <td>10</td>
    </tr>
    <tr>
      <th>28</th>
      <td>MI</td>
      <td>Ann Arbor</td>
      <td>2000-10-01</td>
      <td>14</td>
    </tr>
    <tr>
      <th>29</th>
      <td>OR</td>
      <td>Portland</td>
      <td>2000-10-01</td>
      <td>18</td>
    </tr>
    <tr>
      <th>30</th>
      <td>NY</td>
      <td>New York</td>
      <td>2000-11-01</td>
      <td>11</td>
    </tr>
    <tr>
      <th>31</th>
      <td>MI</td>
      <td>Ann Arbor</td>
      <td>2000-11-01</td>
      <td>15</td>
    </tr>
    <tr>
      <th>32</th>
      <td>OR</td>
      <td>Portland</td>
      <td>2000-11-01</td>
      <td>19</td>
    </tr>
    <tr>
      <th>33</th>
      <td>NY</td>
      <td>New York</td>
      <td>2000-12-01</td>
      <td>12</td>
    </tr>
    <tr>
      <th>34</th>
      <td>MI</td>
      <td>Ann Arbor</td>
      <td>2000-12-01</td>
      <td>16</td>
    </tr>
    <tr>
      <th>35</th>
      <td>OR</td>
      <td>Portland</td>
      <td>2000-12-01</td>
      <td>20</td>
    </tr>
    <tr>
      <th>36</th>
      <td>NY</td>
      <td>New York</td>
      <td>2001-01-01</td>
      <td>13</td>
    </tr>
    <tr>
      <th>37</th>
      <td>MI</td>
      <td>Ann Arbor</td>
      <td>2001-01-01</td>
      <td>17</td>
    </tr>
    <tr>
      <th>38</th>
      <td>OR</td>
      <td>Portland</td>
      <td>2001-01-01</td>
      <td>21</td>
    </tr>
  </tbody>
</table>
</div>
<br><br>
## The First Attempt
<br><br>
Let's see what happens when we simply groupby the city and state: 
<br><br>
{% highlight python %}
long_df.groupby(['state', 'city']).mean()
{% endhighlight %}
<br><br>
<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>number of poutine eaters</th>
    </tr>
    <tr>
      <th>state</th>
      <th>city</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>MI</th>
      <th>Ann Arbor</th>
      <td>11</td>
    </tr>
    <tr>
      <th>NY</th>
      <th>New York</th>
      <td>7</td>
    </tr>
    <tr>
      <th>OR</th>
      <th>Portland</th>
      <td>15</td>
    </tr>
  </tbody>
</table>
</div>
<br><br> 
But this only gives you the annual average by city and state. Instead, we want
to be able to split the months out by quarter. Now, you can do some special
tricks by mapping each month into a quarter (i.e., 01, 02, and 03 are mapped to
Q1 while 10, 11, and 12 are mapped to Q4) and then using that new column to
groupby. However, we can make use of the fantastic built in PeriodIndex function
to do all of the work for us. 
<br><br>
## The Final Step 
<br><br>  
{% highlight python %}
long_df.groupby(['state', 'city', pd.PeriodIndex(long_df.month, freq='Q')]).mean()
{% endhighlight %}
<br><br>
<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th></th>
      <th>number of poutine eaters</th>
    </tr>
    <tr>
      <th>state</th>
      <th>city</th>
      <th>month</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="5" valign="top">MI</th>
      <th rowspan="5" valign="top">Ann Arbor</th>
      <th>2000Q1</th>
      <td>6</td>
    </tr>
    <tr>
      <th>2000Q2</th>
      <td>9</td>
    </tr>
    <tr>
      <th>2000Q3</th>
      <td>12</td>
    </tr>
    <tr>
      <th>2000Q4</th>
      <td>15</td>
    </tr>
    <tr>
      <th>2001Q1</th>
      <td>17</td>
    </tr>
    <tr>
      <th rowspan="5" valign="top">NY</th>
      <th rowspan="5" valign="top">New York</th>
      <th>2000Q1</th>
      <td>2</td>
    </tr>
    <tr>
      <th>2000Q2</th>
      <td>5</td>
    </tr>
    <tr>
      <th>2000Q3</th>
      <td>8</td>
    </tr>
    <tr>
      <th>2000Q4</th>
      <td>11</td>
    </tr>
    <tr>
      <th>2001Q1</th>
      <td>13</td>
    </tr>
    <tr>
      <th rowspan="5" valign="top">OR</th>
      <th rowspan="5" valign="top">Portland</th>
      <th>2000Q1</th>
      <td>10</td>
    </tr>
    <tr>
      <th>2000Q2</th>
      <td>13</td>
    </tr>
    <tr>
      <th>2000Q3</th>
      <td>16</td>
    </tr>
    <tr>
      <th>2000Q4</th>
      <td>19</td>
    </tr>
    <tr>
      <th>2001Q1</th>
      <td>21</td>
    </tr>
  </tbody>
</table>
</div>
<br><br>
That's it! Pretty Wicked, right? Let me know what you think in the comments below. 
