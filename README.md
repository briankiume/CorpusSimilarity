# Finding Similarity Between Two Different Corpora 
A bit complex Algorithm that uses **Cosine Distance** to find similarity between two documents.

## Description
The algo loops through both the vectors of *corpus2* (larger corpus) and *corpus1*, finding cosine similarity between each
document and returns the pair indexes with the lowest Cosine distance. 

It takes two zipped lists as arguments (where vectors of each corpus document are mapped to an index): 

> ***Zipped list:*** Follows the format: *[(array([-0.00051286, -0.00030816, -0.0012232], dtype=float32), 0),
> (array([0.01054019, 0.01054019, -0.00245288,], dtype=float32), 1)...]*
>
> - ***Corpus Vectors:*** Follows the format: *[array([-0.00051286, -0.00030816, -0.0012232], dtype=float32),
>array([0.01054019, 0.01054019, -0.00245288,], dtype=float32)...]*
>

## Usage
The code below shows its usage, pretty simple once the arguments are in the right format.  
```
id_pair_1, id_pair_2 = cosine_two(zipped_1, zipped_2)
```
## Features
🔥 Tip: If you haven't aggregated document vectors, use my [repository](https://github.com/briankiume/AggregateWordEmbeddings) 
then simply continue with this for easier integration.

⚠️ I'm using *Cosine Distance* from Scipy not *Cosine Similarity* from Sci-kit, therefore a 
***higher*** cosine distance means the documents are ***less similar***.

## Requirements
> - Scipy

## License
MIT License. Copyright (c) 2022 Brian Kiume