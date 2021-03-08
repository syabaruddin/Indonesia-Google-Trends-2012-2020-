# Google Trends in Indonesia (2012-2020) 

This is a curated dataset of Google Trends over the years. Every year, Google releases the trending search queries all over the world in various categories.It has trends from 2001 to 2020



```python
# Data sourced from https://www.kaggle.com/dhruvildave/google-trends-dataset

import pandas as pd 
import matplotlib as plt

googletrends = pd.read_csv('C:/SyabaruddinFolder/Work/DATA/GoogleTrendsAnalysis/archive/trends.csv')
googletrends.head()
```




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
      <th>location</th>
      <th>year</th>
      <th>category</th>
      <th>rank</th>
      <th>query</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Global</td>
      <td>2001</td>
      <td>Consumer Brands</td>
      <td>1</td>
      <td>Nokia</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Global</td>
      <td>2001</td>
      <td>Consumer Brands</td>
      <td>2</td>
      <td>Sony</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Global</td>
      <td>2001</td>
      <td>Consumer Brands</td>
      <td>3</td>
      <td>BMW</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Global</td>
      <td>2001</td>
      <td>Consumer Brands</td>
      <td>4</td>
      <td>Palm</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Global</td>
      <td>2001</td>
      <td>Consumer Brands</td>
      <td>5</td>
      <td>Adobe</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Dimension of the dataframe
googletrends.shape
```




    (26955, 5)




```python
#Unique values from 'location column'. It shows where are the locations in every trends.

googletrends['location'].value_counts()
```




    United States         2070
    Global                1135
    Japan                  765
    Canada                 690
    Brazil                 675
                          ... 
    Kuwait                   5
    Honduras                 5
    Dominican Republic       5
    El Salvador              5
    Sudan                    5
    Name: location, Length: 83, dtype: int64




```python
#Unique values from 'year' column. It shows in what year that the trends occured

googletrends['year'].value_counts()
```




    2016    3040
    2020    2980
    2013    2890
    2015    2790
    2017    2610
    2019    2605
    2018    2560
    2014    2320
    2012    2225
    2008     895
    2011     890
    2009     445
    2003     155
    2004     145
    2002     110
    2010      90
    2006      75
    2001      60
    2007      60
    2005      10
    Name: year, dtype: int64




```python
#Unique values from 'year' column. It shows the terms that the trends in google form 2001 to 2021

googletrends['query'].value_counts()
```




    Paul Walker        84
    Donald Trump       83
    Facebook           62
    Robin Williams     61
    Whitney Houston    56
                       ..
    Poodle              1
    豪雨                  1
    中国                  1
    How old net         1
    Vild Med Dans       1
    Name: query, Length: 18431, dtype: int64




```python
#We subset the location to Indonesia. This is to check what trends in Indonesia in Google search during 2001-2020 

indonesia = googletrends[googletrends['location']=='Indonesia']
indonesia = indonesia.loc[:,['year','category','rank','query']]
indonesia
```




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
      <th>year</th>
      <th>category</th>
      <th>rank</th>
      <th>query</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>3685</th>
      <td>2012</td>
      <td>Car Models</td>
      <td>1</td>
      <td>Toyota Agya</td>
    </tr>
    <tr>
      <th>3686</th>
      <td>2012</td>
      <td>Car Models</td>
      <td>2</td>
      <td>Honda Brio</td>
    </tr>
    <tr>
      <th>3687</th>
      <td>2012</td>
      <td>Car Models</td>
      <td>3</td>
      <td>Suzuki Ertiga</td>
    </tr>
    <tr>
      <th>3688</th>
      <td>2012</td>
      <td>Car Models</td>
      <td>4</td>
      <td>Mobil Esemka</td>
    </tr>
    <tr>
      <th>3689</th>
      <td>2012</td>
      <td>Car Models</td>
      <td>5</td>
      <td>Nissan Evalia</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>25160</th>
      <td>2020</td>
      <td>Siapa...</td>
      <td>1</td>
      <td>Bintang Emon</td>
    </tr>
    <tr>
      <th>25161</th>
      <td>2020</td>
      <td>Siapa...</td>
      <td>2</td>
      <td>Hyun Bin</td>
    </tr>
    <tr>
      <th>25162</th>
      <td>2020</td>
      <td>Siapa...</td>
      <td>3</td>
      <td>Kim Soo Hyun</td>
    </tr>
    <tr>
      <th>25163</th>
      <td>2020</td>
      <td>Siapa...</td>
      <td>4</td>
      <td>Najwa Shihab</td>
    </tr>
    <tr>
      <th>25164</th>
      <td>2020</td>
      <td>Siapa...</td>
      <td>5</td>
      <td>George Floyd</td>
    </tr>
  </tbody>
</table>
<p>415 rows × 4 columns</p>
</div>




```python
#data recorded Indonesia only from 2012-2020
indonesia['year'].unique()
```




    array([2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020], dtype=int64)



## Indonesia Top 10 terms in 2012-2020 


```python
indonesiatop10 = indonesia['query'].value_counts().head(10)
indonesiatop10
```




    Jokowi                 4
    Paul Walker            3
    Honda Brio             3
    Pisang Nugget          2
    Setya Novanto          2
    Kartu Pra Kerja        2
    Bucin                  2
    Rohingya               2
    Sakitnya Tuh Disini    2
    Batu Akik              2
    Name: query, dtype: int64



**wow, Our President, Pak 'Jokowi' is the most trending term in 2001-2020!**


```python
indonesiajokowi = indonesia.loc[:,['year','query','category']].set_index('year')
indonesiajokowi = indonesiajokowi[indonesiajokowi['query']=='Jokowi']
indonesiajokowi
```




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
      <th>query</th>
      <th>category</th>
    </tr>
    <tr>
      <th>year</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2012</th>
      <td>Jokowi</td>
      <td>People (Indonesian)</td>
    </tr>
    <tr>
      <th>2012</th>
      <td>Jokowi</td>
      <td>Searches</td>
    </tr>
    <tr>
      <th>2014</th>
      <td>Jokowi</td>
      <td>Penelusuran</td>
    </tr>
    <tr>
      <th>2017</th>
      <td>Jokowi</td>
      <td>Tokoh</td>
    </tr>
  </tbody>
</table>
</div>



**So, Our President 'Jokowi' was trending in 2012, 2014, and 2017!**

### Indonesia Top Google Trends every year from 2012-2020

**Below are Top Google trends on each category every year from 2012-2020**

#### Year 2012


```python
year2012 = indonesia[indonesia['year']==2012].set_index('year')
year2012 = year2012[year2012['rank']==1]
year2012

```




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
      <th>category</th>
      <th>rank</th>
      <th>query</th>
    </tr>
    <tr>
      <th>year</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2012</th>
      <td>Car Models</td>
      <td>1</td>
      <td>Toyota Agya</td>
    </tr>
    <tr>
      <th>2012</th>
      <td>Games</td>
      <td>1</td>
      <td>Angry Birds</td>
    </tr>
    <tr>
      <th>2012</th>
      <td>Indonesian Songs</td>
      <td>1</td>
      <td>Separuh Aku (Noah)</td>
    </tr>
    <tr>
      <th>2012</th>
      <td>Musicians</td>
      <td>1</td>
      <td>Noah</td>
    </tr>
    <tr>
      <th>2012</th>
      <td>People (Global)</td>
      <td>1</td>
      <td>Whitney Houston</td>
    </tr>
    <tr>
      <th>2012</th>
      <td>People (Indonesian)</td>
      <td>1</td>
      <td>Jokowi</td>
    </tr>
    <tr>
      <th>2012</th>
      <td>Searches</td>
      <td>1</td>
      <td>Gangnam Style</td>
    </tr>
  </tbody>
</table>
</div>



#### Year 2013


```python
year2013 = indonesia[indonesia['year']==2013].set_index('year')
year2013 = year2013[year2013['rank']==1]
year2013

```




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
      <th>category</th>
      <th>rank</th>
      <th>query</th>
    </tr>
    <tr>
      <th>year</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2013</th>
      <td>Penelusuran</td>
      <td>1</td>
      <td>Paul Walker</td>
    </tr>
    <tr>
      <th>2013</th>
      <td>Tokoh</td>
      <td>1</td>
      <td>Paul Walker</td>
    </tr>
  </tbody>
</table>
</div>



#### Year 2014


```python
year2014 = indonesia[indonesia['year']==2014].set_index('year')
year2014 = year2014[year2014['rank']==1]
year2014

```




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
      <th>category</th>
      <th>rank</th>
      <th>query</th>
    </tr>
    <tr>
      <th>year</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2014</th>
      <td>Penelusuran</td>
      <td>1</td>
      <td>Jokowi</td>
    </tr>
    <tr>
      <th>2014</th>
      <td>Tokoh Indonesia</td>
      <td>1</td>
      <td>Aliando Syarief</td>
    </tr>
    <tr>
      <th>2014</th>
      <td>Berita Nasional</td>
      <td>1</td>
      <td>Pilpres 2014</td>
    </tr>
    <tr>
      <th>2014</th>
      <td>Apa Itu...</td>
      <td>1</td>
      <td>ISIS</td>
    </tr>
    <tr>
      <th>2014</th>
      <td>Gadget</td>
      <td>1</td>
      <td>iPhone 6</td>
    </tr>
    <tr>
      <th>2014</th>
      <td>Lagu</td>
      <td>1</td>
      <td>Sakitnya Tuh Disini</td>
    </tr>
    <tr>
      <th>2014</th>
      <td>Otomotif</td>
      <td>1</td>
      <td>Honda Mobilio</td>
    </tr>
    <tr>
      <th>2014</th>
      <td>Resep Makanan</td>
      <td>1</td>
      <td>Nasi Goreng</td>
    </tr>
    <tr>
      <th>2014</th>
      <td>Acara Televisi</td>
      <td>1</td>
      <td>Mahabarata</td>
    </tr>
    <tr>
      <th>2014</th>
      <td>Pertandingan Piala Dunia</td>
      <td>1</td>
      <td>Jerman Vs Argentina</td>
    </tr>
    <tr>
      <th>2014</th>
      <td>Aplikasi Chat</td>
      <td>1</td>
      <td>BBM</td>
    </tr>
    <tr>
      <th>2014</th>
      <td>Penyanyi Korea</td>
      <td>1</td>
      <td>SNSD</td>
    </tr>
  </tbody>
</table>
</div>



#### Year 2015


```python
year2015 = indonesia[indonesia['year']==2015].set_index('year')
year2015 = year2015[year2015['rank']==1]
year2015

```




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
      <th>category</th>
      <th>rank</th>
      <th>query</th>
    </tr>
    <tr>
      <th>year</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2015</th>
      <td>Penelusuran Terpopuler</td>
      <td>1</td>
      <td>Batu Akik</td>
    </tr>
    <tr>
      <th>2015</th>
      <td>Peristiwa Nasional</td>
      <td>1</td>
      <td>Pembekuan PSSI</td>
    </tr>
    <tr>
      <th>2015</th>
      <td>Peristiwa Internasional</td>
      <td>1</td>
      <td>Tragedi Mina</td>
    </tr>
    <tr>
      <th>2015</th>
      <td>Tokoh</td>
      <td>1</td>
      <td>Valentino Rossi</td>
    </tr>
    <tr>
      <th>2015</th>
      <td>Apa Itu...</td>
      <td>1</td>
      <td>Baper</td>
    </tr>
    <tr>
      <th>2015</th>
      <td>Bagaimana Cara...</td>
      <td>1</td>
      <td>Bentuk Perut Six Pack Tanpa ke Gym</td>
    </tr>
    <tr>
      <th>2015</th>
      <td>Film Indonesia 2015</td>
      <td>1</td>
      <td>Filosofi Kopi</td>
    </tr>
    <tr>
      <th>2015</th>
      <td>Gadget</td>
      <td>1</td>
      <td>Samsung Galaxy A</td>
    </tr>
    <tr>
      <th>2015</th>
      <td>Game</td>
      <td>1</td>
      <td>Point Blank Garena</td>
    </tr>
    <tr>
      <th>2015</th>
      <td>Meme</td>
      <td>1</td>
      <td>Meme Haji Lulung</td>
    </tr>
    <tr>
      <th>2015</th>
      <td>Mode &amp; Kecantikan</td>
      <td>1</td>
      <td>Celana Jogger</td>
    </tr>
    <tr>
      <th>2015</th>
      <td>Resep</td>
      <td>1</td>
      <td>Kue Cubit</td>
    </tr>
    <tr>
      <th>2015</th>
      <td>Selebriti</td>
      <td>1</td>
      <td>Cita Citata</td>
    </tr>
  </tbody>
</table>
</div>



#### Year 2016


```python
year2016 = indonesia[indonesia['year']==2016].set_index('year')
year2016 = year2016[year2016['rank']==1]
year2016

```




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
      <th>category</th>
      <th>rank</th>
      <th>query</th>
    </tr>
    <tr>
      <th>year</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2016</th>
      <td>Penelusuran Terpopuler</td>
      <td>1</td>
      <td>Pokémon GO</td>
    </tr>
    <tr>
      <th>2016</th>
      <td>Tokoh</td>
      <td>1</td>
      <td>Ahok</td>
    </tr>
    <tr>
      <th>2016</th>
      <td>Peristiwa Nasional</td>
      <td>1</td>
      <td>Bom Sarinah</td>
    </tr>
    <tr>
      <th>2016</th>
      <td>Peristiwa Internasional</td>
      <td>1</td>
      <td>Panama Papers</td>
    </tr>
    <tr>
      <th>2016</th>
      <td>Selebriti</td>
      <td>1</td>
      <td>Saipul Jamil</td>
    </tr>
    <tr>
      <th>2016</th>
      <td>Atlet</td>
      <td>1</td>
      <td>Liliyana Natsir</td>
    </tr>
    <tr>
      <th>2016</th>
      <td>Peristiwa Olahraga</td>
      <td>1</td>
      <td>UEFA Euro 2016</td>
    </tr>
    <tr>
      <th>2016</th>
      <td>Kepergian Tokoh</td>
      <td>1</td>
      <td>Mike Mohede</td>
    </tr>
    <tr>
      <th>2016</th>
      <td>Lagu</td>
      <td>1</td>
      <td>Dia - Anji</td>
    </tr>
    <tr>
      <th>2016</th>
      <td>Film</td>
      <td>1</td>
      <td>The Conjuring 2</td>
    </tr>
    <tr>
      <th>2016</th>
      <td>Meme</td>
      <td>1</td>
      <td>Meme Valak</td>
    </tr>
    <tr>
      <th>2016</th>
      <td>Bagaimana Cara</td>
      <td>1</td>
      <td>Cara Shalat Gerhana</td>
    </tr>
    <tr>
      <th>2016</th>
      <td>Resep</td>
      <td>1</td>
      <td>Cake Tape</td>
    </tr>
    <tr>
      <th>2016</th>
      <td>Dekat Sini</td>
      <td>1</td>
      <td>Salon Dekat Sini</td>
    </tr>
    <tr>
      <th>2016</th>
      <td>Teknologi (Gim, Aplikasi, Gawai)</td>
      <td>1</td>
      <td>Samsung Z2</td>
    </tr>
    <tr>
      <th>2016</th>
      <td>Otomotif</td>
      <td>1</td>
      <td>Honda Brio</td>
    </tr>
  </tbody>
</table>
</div>



#### Year 2017


```python
year2017 = indonesia[indonesia['year']==2017].set_index('year')
year2017 = year2017[year2017['rank']==1]
year2017

```




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
      <th>category</th>
      <th>rank</th>
      <th>query</th>
    </tr>
    <tr>
      <th>year</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2017</th>
      <td>Penelusuran Terpopuler</td>
      <td>1</td>
      <td>Surat Cinta untuk Starla</td>
    </tr>
    <tr>
      <th>2017</th>
      <td>Tokoh</td>
      <td>1</td>
      <td>Habib Rizieq</td>
    </tr>
    <tr>
      <th>2017</th>
      <td>Peristiwa Nasional</td>
      <td>1</td>
      <td>Gunung Agung</td>
    </tr>
    <tr>
      <th>2017</th>
      <td>Peristiwa Internasional</td>
      <td>1</td>
      <td>Rohingya</td>
    </tr>
    <tr>
      <th>2017</th>
      <td>Selebriti</td>
      <td>1</td>
      <td>Nella Kharisma</td>
    </tr>
    <tr>
      <th>2017</th>
      <td>Lagu</td>
      <td>1</td>
      <td>Despacito - Luis Fonsi ft. Daddy Yankee</td>
    </tr>
    <tr>
      <th>2017</th>
      <td>Apa Itu...</td>
      <td>1</td>
      <td>Rubella</td>
    </tr>
    <tr>
      <th>2017</th>
      <td>Cara Menjadi..</td>
      <td>1</td>
      <td>Selebgram</td>
    </tr>
    <tr>
      <th>2017</th>
      <td>Resep</td>
      <td>1</td>
      <td>Minuman Mangga</td>
    </tr>
  </tbody>
</table>
</div>



#### Year 2018


```python
year2018 = indonesia[indonesia['year']==2018].set_index('year')
year2018 = year2018[year2018['rank']==1]
year2018
```




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
      <th>category</th>
      <th>rank</th>
      <th>query</th>
    </tr>
    <tr>
      <th>year</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2018</th>
      <td>Film</td>
      <td>1</td>
      <td>Dilan 1990</td>
    </tr>
    <tr>
      <th>2018</th>
      <td>Lagu</td>
      <td>1</td>
      <td>Karna Su Sayang</td>
    </tr>
    <tr>
      <th>2018</th>
      <td>Penelusuran Terpopuler</td>
      <td>1</td>
      <td>Piala Dunia Russia 2018</td>
    </tr>
    <tr>
      <th>2018</th>
      <td>Peristiwa Hiburan</td>
      <td>1</td>
      <td>Indonesian Idol</td>
    </tr>
    <tr>
      <th>2018</th>
      <td>Peristiwa Nasional</td>
      <td>1</td>
      <td>Bom Surabaya</td>
    </tr>
    <tr>
      <th>2018</th>
      <td>Selebriti</td>
      <td>1</td>
      <td>Nissa Sabyan</td>
    </tr>
  </tbody>
</table>
</div>



#### Year 2019


```python
year2019 = indonesia[indonesia['year']==2019].set_index('year')
year2019 = year2019[year2019['rank']==1]
year2019
```




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
      <th>category</th>
      <th>rank</th>
      <th>query</th>
    </tr>
    <tr>
      <th>year</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2019</th>
      <td>Apa itu...</td>
      <td>1</td>
      <td>Bucin</td>
    </tr>
    <tr>
      <th>2019</th>
      <td>Bagaimana cara...</td>
      <td>1</td>
      <td>Hidup sehat</td>
    </tr>
    <tr>
      <th>2019</th>
      <td>Film</td>
      <td>1</td>
      <td>Joker</td>
    </tr>
    <tr>
      <th>2019</th>
      <td>Kepergian Tokoh</td>
      <td>1</td>
      <td>BJ Habibie</td>
    </tr>
    <tr>
      <th>2019</th>
      <td>Lagu</td>
      <td>1</td>
      <td>Kemarin - Seventeen</td>
    </tr>
    <tr>
      <th>2019</th>
      <td>Penelusuran Terpopuler</td>
      <td>1</td>
      <td>Cinta Luar Biasa</td>
    </tr>
    <tr>
      <th>2019</th>
      <td>Peristiwa Nasional</td>
      <td>1</td>
      <td>Audrey</td>
    </tr>
    <tr>
      <th>2019</th>
      <td>Resep</td>
      <td>1</td>
      <td>Pisang Nugget</td>
    </tr>
    <tr>
      <th>2019</th>
      <td>Tokoh</td>
      <td>1</td>
      <td>Nadiem Makarim</td>
    </tr>
  </tbody>
</table>
</div>



#### Year 2020


```python
year2020 = indonesia[indonesia['year']==2020].set_index('year')
year2020 = year2020[year2020['rank']==1]
year2020
```




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
      <th>category</th>
      <th>rank</th>
      <th>query</th>
    </tr>
    <tr>
      <th>year</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2020</th>
      <td>Apa itu...</td>
      <td>1</td>
      <td>Ghosting</td>
    </tr>
    <tr>
      <th>2020</th>
      <td>Bagaimana cara...</td>
      <td>1</td>
      <td>Cara Daftar UMKM</td>
    </tr>
    <tr>
      <th>2020</th>
      <td>Berita</td>
      <td>1</td>
      <td>Kartu Pra Kerja</td>
    </tr>
    <tr>
      <th>2020</th>
      <td>Film / TV Series</td>
      <td>1</td>
      <td>Tilik</td>
    </tr>
    <tr>
      <th>2020</th>
      <td>Kepergian Tokoh</td>
      <td>1</td>
      <td>Glenn Fredly</td>
    </tr>
    <tr>
      <th>2020</th>
      <td>Lirik Lagu</td>
      <td>1</td>
      <td>Lathi - Weird Genius - ft. Sara Fajira</td>
    </tr>
    <tr>
      <th>2020</th>
      <td>Penelusuran Terpopuler</td>
      <td>1</td>
      <td>Virus Corona</td>
    </tr>
    <tr>
      <th>2020</th>
      <td>Resep</td>
      <td>1</td>
      <td>Donat</td>
    </tr>
    <tr>
      <th>2020</th>
      <td>Siapa...</td>
      <td>1</td>
      <td>Bintang Emon</td>
    </tr>
  </tbody>
</table>
</div>


