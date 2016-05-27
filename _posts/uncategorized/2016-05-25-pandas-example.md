---
layout: post
title: "Pandas Example"
---  

<img class="img-left" align="left" src="{{ site.url }}/images/batting_averages.png">

{% highlight python %}
import pandas as pd
import numpy as np
import datetime
{% endhighlight %}
 
# Purpose 
 
The indexing capabilities that come with Pandas are incredibly useful. However,
I find myself forgetting the concepts beyond the basics when I haven't touched
Pandas in a while. This tutorial serves as my own personal reminder but I hope
others will find it helpful as well.

To motivate this, we we'll explore a baseball dataset and plot batting averages
for some of the greatest players of all time. 
 
# Load Some Data 
  

{% highlight python %}
df = pd.read_csv('Batting.csv')  # Download data from http://seanlahman.com/files/database/lahman-csv_2014-02-14.zip
df['yearID'] = pd.to_datetime(df['yearID'], format='%Y', exact=True)
df.head()
{% endhighlight %}




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>playerID</th>
      <th>yearID</th>
      <th>stint</th>
      <th>teamID</th>
      <th>lgID</th>
      <th>G</th>
      <th>G_batting</th>
      <th>AB</th>
      <th>R</th>
      <th>H</th>
      <th>...</th>
      <th>SB</th>
      <th>CS</th>
      <th>BB</th>
      <th>SO</th>
      <th>IBB</th>
      <th>HBP</th>
      <th>SH</th>
      <th>SF</th>
      <th>GIDP</th>
      <th>G_old</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>aardsda01</td>
      <td>2004-01-01</td>
      <td>1</td>
      <td>SFN</td>
      <td>NL</td>
      <td>11</td>
      <td>11</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>11</td>
    </tr>
    <tr>
      <th>1</th>
      <td>aardsda01</td>
      <td>2006-01-01</td>
      <td>1</td>
      <td>CHN</td>
      <td>NL</td>
      <td>45</td>
      <td>43</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>45</td>
    </tr>
    <tr>
      <th>2</th>
      <td>aardsda01</td>
      <td>2007-01-01</td>
      <td>1</td>
      <td>CHA</td>
      <td>AL</td>
      <td>25</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>aardsda01</td>
      <td>2008-01-01</td>
      <td>1</td>
      <td>BOS</td>
      <td>AL</td>
      <td>47</td>
      <td>5</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>5</td>
    </tr>
    <tr>
      <th>4</th>
      <td>aardsda01</td>
      <td>2009-01-01</td>
      <td>1</td>
      <td>SEA</td>
      <td>AL</td>
      <td>73</td>
      <td>3</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 24 columns</p>
</div>


 
# Basic Indexing 
  

{% highlight python %}
df[df['playerID'] == 'mantlmi01']
{% endhighlight %}




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>playerID</th>
      <th>yearID</th>
      <th>stint</th>
      <th>teamID</th>
      <th>lgID</th>
      <th>G</th>
      <th>G_batting</th>
      <th>AB</th>
      <th>R</th>
      <th>H</th>
      <th>...</th>
      <th>SB</th>
      <th>CS</th>
      <th>BB</th>
      <th>SO</th>
      <th>IBB</th>
      <th>HBP</th>
      <th>SH</th>
      <th>SF</th>
      <th>GIDP</th>
      <th>G_old</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>53662</th>
      <td>mantlmi01</td>
      <td>1951-01-01</td>
      <td>1</td>
      <td>NYA</td>
      <td>AL</td>
      <td>96</td>
      <td>96</td>
      <td>341</td>
      <td>61</td>
      <td>91</td>
      <td>...</td>
      <td>8</td>
      <td>7</td>
      <td>43</td>
      <td>74</td>
      <td>NaN</td>
      <td>0</td>
      <td>2</td>
      <td>NaN</td>
      <td>3</td>
      <td>96</td>
    </tr>
    <tr>
      <th>53663</th>
      <td>mantlmi01</td>
      <td>1952-01-01</td>
      <td>1</td>
      <td>NYA</td>
      <td>AL</td>
      <td>142</td>
      <td>142</td>
      <td>549</td>
      <td>94</td>
      <td>171</td>
      <td>...</td>
      <td>4</td>
      <td>1</td>
      <td>75</td>
      <td>111</td>
      <td>NaN</td>
      <td>0</td>
      <td>2</td>
      <td>NaN</td>
      <td>5</td>
      <td>142</td>
    </tr>
    <tr>
      <th>53664</th>
      <td>mantlmi01</td>
      <td>1953-01-01</td>
      <td>1</td>
      <td>NYA</td>
      <td>AL</td>
      <td>127</td>
      <td>127</td>
      <td>461</td>
      <td>105</td>
      <td>136</td>
      <td>...</td>
      <td>8</td>
      <td>4</td>
      <td>79</td>
      <td>90</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>NaN</td>
      <td>2</td>
      <td>127</td>
    </tr>
    <tr>
      <th>53665</th>
      <td>mantlmi01</td>
      <td>1954-01-01</td>
      <td>1</td>
      <td>NYA</td>
      <td>AL</td>
      <td>146</td>
      <td>146</td>
      <td>543</td>
      <td>129</td>
      <td>163</td>
      <td>...</td>
      <td>5</td>
      <td>2</td>
      <td>102</td>
      <td>107</td>
      <td>NaN</td>
      <td>0</td>
      <td>2</td>
      <td>4</td>
      <td>3</td>
      <td>146</td>
    </tr>
    <tr>
      <th>53666</th>
      <td>mantlmi01</td>
      <td>1955-01-01</td>
      <td>1</td>
      <td>NYA</td>
      <td>AL</td>
      <td>147</td>
      <td>147</td>
      <td>517</td>
      <td>121</td>
      <td>158</td>
      <td>...</td>
      <td>8</td>
      <td>1</td>
      <td>113</td>
      <td>97</td>
      <td>6</td>
      <td>3</td>
      <td>2</td>
      <td>3</td>
      <td>4</td>
      <td>147</td>
    </tr>
    <tr>
      <th>53667</th>
      <td>mantlmi01</td>
      <td>1956-01-01</td>
      <td>1</td>
      <td>NYA</td>
      <td>AL</td>
      <td>150</td>
      <td>150</td>
      <td>533</td>
      <td>132</td>
      <td>188</td>
      <td>...</td>
      <td>10</td>
      <td>1</td>
      <td>112</td>
      <td>99</td>
      <td>6</td>
      <td>2</td>
      <td>1</td>
      <td>4</td>
      <td>4</td>
      <td>150</td>
    </tr>
    <tr>
      <th>53668</th>
      <td>mantlmi01</td>
      <td>1957-01-01</td>
      <td>1</td>
      <td>NYA</td>
      <td>AL</td>
      <td>144</td>
      <td>144</td>
      <td>474</td>
      <td>121</td>
      <td>173</td>
      <td>...</td>
      <td>16</td>
      <td>3</td>
      <td>146</td>
      <td>75</td>
      <td>23</td>
      <td>0</td>
      <td>0</td>
      <td>3</td>
      <td>5</td>
      <td>144</td>
    </tr>
    <tr>
      <th>53669</th>
      <td>mantlmi01</td>
      <td>1958-01-01</td>
      <td>1</td>
      <td>NYA</td>
      <td>AL</td>
      <td>150</td>
      <td>150</td>
      <td>519</td>
      <td>127</td>
      <td>158</td>
      <td>...</td>
      <td>18</td>
      <td>3</td>
      <td>129</td>
      <td>120</td>
      <td>13</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>11</td>
      <td>150</td>
    </tr>
    <tr>
      <th>53670</th>
      <td>mantlmi01</td>
      <td>1959-01-01</td>
      <td>1</td>
      <td>NYA</td>
      <td>AL</td>
      <td>144</td>
      <td>144</td>
      <td>541</td>
      <td>104</td>
      <td>154</td>
      <td>...</td>
      <td>21</td>
      <td>3</td>
      <td>93</td>
      <td>126</td>
      <td>6</td>
      <td>2</td>
      <td>1</td>
      <td>2</td>
      <td>7</td>
      <td>144</td>
    </tr>
    <tr>
      <th>53671</th>
      <td>mantlmi01</td>
      <td>1960-01-01</td>
      <td>1</td>
      <td>NYA</td>
      <td>AL</td>
      <td>153</td>
      <td>153</td>
      <td>527</td>
      <td>119</td>
      <td>145</td>
      <td>...</td>
      <td>14</td>
      <td>3</td>
      <td>111</td>
      <td>125</td>
      <td>6</td>
      <td>1</td>
      <td>0</td>
      <td>5</td>
      <td>11</td>
      <td>153</td>
    </tr>
    <tr>
      <th>53672</th>
      <td>mantlmi01</td>
      <td>1961-01-01</td>
      <td>1</td>
      <td>NYA</td>
      <td>AL</td>
      <td>153</td>
      <td>153</td>
      <td>514</td>
      <td>132</td>
      <td>163</td>
      <td>...</td>
      <td>12</td>
      <td>1</td>
      <td>126</td>
      <td>112</td>
      <td>9</td>
      <td>0</td>
      <td>1</td>
      <td>5</td>
      <td>2</td>
      <td>153</td>
    </tr>
    <tr>
      <th>53673</th>
      <td>mantlmi01</td>
      <td>1962-01-01</td>
      <td>1</td>
      <td>NYA</td>
      <td>AL</td>
      <td>123</td>
      <td>123</td>
      <td>377</td>
      <td>96</td>
      <td>121</td>
      <td>...</td>
      <td>9</td>
      <td>0</td>
      <td>122</td>
      <td>78</td>
      <td>9</td>
      <td>1</td>
      <td>0</td>
      <td>2</td>
      <td>4</td>
      <td>123</td>
    </tr>
    <tr>
      <th>53674</th>
      <td>mantlmi01</td>
      <td>1963-01-01</td>
      <td>1</td>
      <td>NYA</td>
      <td>AL</td>
      <td>65</td>
      <td>65</td>
      <td>172</td>
      <td>40</td>
      <td>54</td>
      <td>...</td>
      <td>2</td>
      <td>1</td>
      <td>40</td>
      <td>32</td>
      <td>4</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>5</td>
      <td>65</td>
    </tr>
    <tr>
      <th>53675</th>
      <td>mantlmi01</td>
      <td>1964-01-01</td>
      <td>1</td>
      <td>NYA</td>
      <td>AL</td>
      <td>143</td>
      <td>143</td>
      <td>465</td>
      <td>92</td>
      <td>141</td>
      <td>...</td>
      <td>6</td>
      <td>3</td>
      <td>99</td>
      <td>102</td>
      <td>18</td>
      <td>0</td>
      <td>0</td>
      <td>3</td>
      <td>9</td>
      <td>143</td>
    </tr>
    <tr>
      <th>53676</th>
      <td>mantlmi01</td>
      <td>1965-01-01</td>
      <td>1</td>
      <td>NYA</td>
      <td>AL</td>
      <td>122</td>
      <td>122</td>
      <td>361</td>
      <td>44</td>
      <td>92</td>
      <td>...</td>
      <td>4</td>
      <td>1</td>
      <td>73</td>
      <td>76</td>
      <td>7</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>11</td>
      <td>122</td>
    </tr>
    <tr>
      <th>53677</th>
      <td>mantlmi01</td>
      <td>1966-01-01</td>
      <td>1</td>
      <td>NYA</td>
      <td>AL</td>
      <td>108</td>
      <td>108</td>
      <td>333</td>
      <td>40</td>
      <td>96</td>
      <td>...</td>
      <td>1</td>
      <td>1</td>
      <td>57</td>
      <td>76</td>
      <td>5</td>
      <td>0</td>
      <td>0</td>
      <td>3</td>
      <td>9</td>
      <td>108</td>
    </tr>
    <tr>
      <th>53678</th>
      <td>mantlmi01</td>
      <td>1967-01-01</td>
      <td>1</td>
      <td>NYA</td>
      <td>AL</td>
      <td>144</td>
      <td>144</td>
      <td>440</td>
      <td>63</td>
      <td>108</td>
      <td>...</td>
      <td>1</td>
      <td>1</td>
      <td>107</td>
      <td>113</td>
      <td>7</td>
      <td>1</td>
      <td>0</td>
      <td>5</td>
      <td>9</td>
      <td>144</td>
    </tr>
    <tr>
      <th>53679</th>
      <td>mantlmi01</td>
      <td>1968-01-01</td>
      <td>1</td>
      <td>NYA</td>
      <td>AL</td>
      <td>144</td>
      <td>144</td>
      <td>435</td>
      <td>57</td>
      <td>103</td>
      <td>...</td>
      <td>6</td>
      <td>2</td>
      <td>106</td>
      <td>97</td>
      <td>7</td>
      <td>1</td>
      <td>1</td>
      <td>4</td>
      <td>9</td>
      <td>144</td>
    </tr>
  </tbody>
</table>
<p>18 rows × 24 columns</p>
</div>


 
# Applying Function to a Groupby Object (Aggregating Multiple Columns) 
 
### Define a Function 
  

{% highlight python %}
def get_batting_avg(group):
    """
    """
    result = 0
    if group['AB'].sum() > 0:
        #result = 100.0*group['H'].sum()/group['AB'].sum()
        result = 100.0*(group['H']/group['AB']).mean()
    
    return result
{% endhighlight %}
 
### Groupby Year and Player 
  

{% highlight python %}
grouped = df.groupby(['yearID', 'playerID'])
{% endhighlight %}
 
### Get Annual Batting Averages for Each Player 
  

{% highlight python %}
batting_avg = grouped.apply(get_batting_avg)
{% endhighlight %}
  

{% highlight python %}
batting_avg.head()
{% endhighlight %}



  


 
### Get Annual Batting Averages for Mickey Mantle, Roger Maris, and Babe Ruth 
  

{% highlight python %}
player = 'mantlmi01'
idx = pd.IndexSlice
mantle_batting_avg = pd.DataFrame(batting_avg.loc[idx[:], idx[player]], columns=['avg'])
mantle_batting_avg.head()
{% endhighlight %}




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>avg</th>
    </tr>
    <tr>
      <th>yearID</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1951-01-01</th>
      <td>26.686217</td>
    </tr>
    <tr>
      <th>1952-01-01</th>
      <td>31.147541</td>
    </tr>
    <tr>
      <th>1953-01-01</th>
      <td>29.501085</td>
    </tr>
    <tr>
      <th>1954-01-01</th>
      <td>30.018416</td>
    </tr>
    <tr>
      <th>1955-01-01</th>
      <td>30.560928</td>
    </tr>
  </tbody>
</table>
</div>


  

{% highlight python %}
player = 'ruthba01'
ruth_batting_avg = pd.DataFrame(batting_avg.loc[idx[:], idx[player]], columns=['avg'])
player = 'marisro01'
maris_batting_avg = pd.DataFrame(batting_avg.loc[idx[:], idx[player]], columns=['avg'])
{% endhighlight %}
 
### Get Annual Batting Averages for Mickey Mantle, Roger Maris, and Babe Ruth 
  

{% highlight python %}
players = ['mantlmi01', 'ruthba01', 'marisro01']
idx = pd.IndexSlice
legends_batting_avg = pd.DataFrame(batting_avg.loc[idx[:], idx[players]], columns=['avg'])
legends_batting_avg
{% endhighlight %}




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>avg</th>
    </tr>
    <tr>
      <th>yearID</th>
      <th>playerID</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1914-01-01</th>
      <th>ruthba01</th>
      <td>20.000000</td>
    </tr>
    <tr>
      <th>1915-01-01</th>
      <th>ruthba01</th>
      <td>31.521739</td>
    </tr>
    <tr>
      <th>1916-01-01</th>
      <th>ruthba01</th>
      <td>27.205882</td>
    </tr>
    <tr>
      <th>1917-01-01</th>
      <th>ruthba01</th>
      <td>32.520325</td>
    </tr>
    <tr>
      <th>1918-01-01</th>
      <th>ruthba01</th>
      <td>29.968454</td>
    </tr>
    <tr>
      <th>1919-01-01</th>
      <th>ruthba01</th>
      <td>32.175926</td>
    </tr>
    <tr>
      <th>1920-01-01</th>
      <th>ruthba01</th>
      <td>37.636761</td>
    </tr>
    <tr>
      <th>1921-01-01</th>
      <th>ruthba01</th>
      <td>37.777778</td>
    </tr>
    <tr>
      <th>1922-01-01</th>
      <th>ruthba01</th>
      <td>31.527094</td>
    </tr>
    <tr>
      <th>1923-01-01</th>
      <th>ruthba01</th>
      <td>39.272031</td>
    </tr>
    <tr>
      <th>1924-01-01</th>
      <th>ruthba01</th>
      <td>37.807183</td>
    </tr>
    <tr>
      <th>1925-01-01</th>
      <th>ruthba01</th>
      <td>28.969359</td>
    </tr>
    <tr>
      <th>1926-01-01</th>
      <th>ruthba01</th>
      <td>37.171717</td>
    </tr>
    <tr>
      <th>1927-01-01</th>
      <th>ruthba01</th>
      <td>35.555556</td>
    </tr>
    <tr>
      <th>1928-01-01</th>
      <th>ruthba01</th>
      <td>32.276119</td>
    </tr>
    <tr>
      <th>1929-01-01</th>
      <th>ruthba01</th>
      <td>34.468938</td>
    </tr>
    <tr>
      <th>1930-01-01</th>
      <th>ruthba01</th>
      <td>35.907336</td>
    </tr>
    <tr>
      <th>1931-01-01</th>
      <th>ruthba01</th>
      <td>37.265918</td>
    </tr>
    <tr>
      <th>1932-01-01</th>
      <th>ruthba01</th>
      <td>34.135667</td>
    </tr>
    <tr>
      <th>1933-01-01</th>
      <th>ruthba01</th>
      <td>30.065359</td>
    </tr>
    <tr>
      <th>1934-01-01</th>
      <th>ruthba01</th>
      <td>28.767123</td>
    </tr>
    <tr>
      <th>1935-01-01</th>
      <th>ruthba01</th>
      <td>18.055556</td>
    </tr>
    <tr>
      <th>1951-01-01</th>
      <th>mantlmi01</th>
      <td>26.686217</td>
    </tr>
    <tr>
      <th>1952-01-01</th>
      <th>mantlmi01</th>
      <td>31.147541</td>
    </tr>
    <tr>
      <th>1953-01-01</th>
      <th>mantlmi01</th>
      <td>29.501085</td>
    </tr>
    <tr>
      <th>1954-01-01</th>
      <th>mantlmi01</th>
      <td>30.018416</td>
    </tr>
    <tr>
      <th>1955-01-01</th>
      <th>mantlmi01</th>
      <td>30.560928</td>
    </tr>
    <tr>
      <th>1956-01-01</th>
      <th>mantlmi01</th>
      <td>35.272045</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">1957-01-01</th>
      <th>mantlmi01</th>
      <td>36.497890</td>
    </tr>
    <tr>
      <th>marisro01</th>
      <td>23.463687</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">1958-01-01</th>
      <th>mantlmi01</th>
      <td>30.443160</td>
    </tr>
    <tr>
      <th>marisro01</th>
      <td>23.607876</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">1959-01-01</th>
      <th>mantlmi01</th>
      <td>28.465804</td>
    </tr>
    <tr>
      <th>marisro01</th>
      <td>27.251732</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">1960-01-01</th>
      <th>mantlmi01</th>
      <td>27.514231</td>
    </tr>
    <tr>
      <th>marisro01</th>
      <td>28.256513</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">1961-01-01</th>
      <th>mantlmi01</th>
      <td>31.712062</td>
    </tr>
    <tr>
      <th>marisro01</th>
      <td>26.949153</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">1962-01-01</th>
      <th>mantlmi01</th>
      <td>32.095491</td>
    </tr>
    <tr>
      <th>marisro01</th>
      <td>25.593220</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">1963-01-01</th>
      <th>mantlmi01</th>
      <td>31.395349</td>
    </tr>
    <tr>
      <th>marisro01</th>
      <td>26.923077</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">1964-01-01</th>
      <th>mantlmi01</th>
      <td>30.322581</td>
    </tr>
    <tr>
      <th>marisro01</th>
      <td>28.070175</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">1965-01-01</th>
      <th>mantlmi01</th>
      <td>25.484765</td>
    </tr>
    <tr>
      <th>marisro01</th>
      <td>23.870968</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">1966-01-01</th>
      <th>mantlmi01</th>
      <td>28.828829</td>
    </tr>
    <tr>
      <th>marisro01</th>
      <td>23.275862</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">1967-01-01</th>
      <th>mantlmi01</th>
      <td>24.545455</td>
    </tr>
    <tr>
      <th>marisro01</th>
      <td>26.097561</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">1968-01-01</th>
      <th>mantlmi01</th>
      <td>23.678161</td>
    </tr>
    <tr>
      <th>marisro01</th>
      <td>25.483871</td>
    </tr>
  </tbody>
</table>
</div>


 
# Get Aggregated Annual Batting Averages 
  

{% highlight python %}
all_batting_avg = batting_avg.groupby(level=['yearID']).agg({'avg': np.mean})
all_batting_avg.head()
{% endhighlight %}




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>avg</th>
    </tr>
    <tr>
      <th>yearID</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1871-01-01 00:00:00</th>
      <td>25.431261</td>
    </tr>
    <tr>
      <th>1872-01-01 00:00:00</th>
      <td>24.555224</td>
    </tr>
    <tr>
      <th>1873-01-01 00:00:00</th>
      <td>24.974896</td>
    </tr>
    <tr>
      <th>1874-01-01 00:00:00</th>
      <td>24.023281</td>
    </tr>
    <tr>
      <th>1875-01-01 00:00:00</th>
      <td>22.016575</td>
    </tr>
  </tbody>
</table>
</div>


 
# Plot Batting Averages Over Time 
  

{% highlight python %}
def get_timestamp(time):
    """
    """
    
    delta = (pd.to_datetime(time).to_datetime() - datetime.datetime(1970, 1, 1))
    return 1000*delta.total_seconds()
{% endhighlight %}
  

{% highlight python %}
# Get xlim, ylim
minx = min(all_batting_avg.index.values.min(), ruth_batting_avg.index.values.min())
maxx = max(all_batting_avg.index.values.max(), ruth_batting_avg.index.values.max())
miny = min(all_batting_avg.values.min(), ruth_batting_avg.values.min())
maxy = max(all_batting_avg.values.max(), ruth_batting_avg.values.max())

p = figure(width=800, height=500, x_axis_type="datetime")

# Draw lines
p.set(x_range=Range1d(minx, maxx), y_range=Range1d(-1, maxy+5), title='Annual Batting Averages')
p.line(all_batting_avg.index.values, all_batting_avg.values.flatten(), line_width=3, line_color='green', line_join='round', line_dash=[5,5])
p.line(mantle_batting_avg.index.values, mantle_batting_avg.values.flatten(), line_width=3, line_color='blue', line_join='round')
p.line(maris_batting_avg.index.values, maris_batting_avg.values.flatten(), line_width=3, line_color='red', line_join='round')
p.line(ruth_batting_avg.index.values, ruth_batting_avg.values.flatten(), line_width=3, line_color='black', line_join='round')

# Draw shapes
p.square(all_batting_avg.index.values, all_batting_avg.values.flatten(), size=5, line_color='green', fill_color='green')
p.circle(mantle_batting_avg.index.values, mantle_batting_avg.values.flatten(), size=5, line_color='blue', fill_color='blue')
p.circle(maris_batting_avg.index.values, maris_batting_avg.values.flatten(), size=5, line_color='red', fill_color='red')
p.circle(ruth_batting_avg.index.values, ruth_batting_avg.values.flatten(), size=5, line_color='black', fill_color='black')

# Write text on plot
p.text(get_timestamp(mantle_batting_avg.index.values.min()), mantle_batting_avg.values.max(), text=["Mickey Mantle"], text_color='blue')
p.text(get_timestamp(maris_batting_avg.index.values.max()), maris_batting_avg.values.max(), text=["Roger Maris"], text_color='red')
p.text(get_timestamp(ruth_batting_avg.index.values.min()), ruth_batting_avg.values.max(), text=["Babe Ruth"], text_color='black')

show(p)
{% endhighlight %}


<img align="center" src="{{ site.url }}/images/batting_averages.png">
