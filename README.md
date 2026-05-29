# Learn Hadoop

A small collection of hands-on examples for learning the Hadoop ecosystem and the tools built on top
of it. The examples use the classic **[MovieLens 100k](https://grouplens.org/datasets/movielens/100k/)**
dataset (included under `ml-100k/`) to explore distributed data processing patterns.

## Examples

### 1. `RatingsBreakdown.py` — MapReduce with MRJob

Counts how many ratings each movie received and outputs them sorted by count, using
[MRJob](https://mrjob.readthedocs.io/) to express a multi-step MapReduce job in Python.

The job has two steps:

1. **Map** each rating to `(movieID, 1)` and **reduce** to a total count per movie.
2. A second **reduce** step sorts the output by the (zero-padded) count.

Run it locally:

```bash
python RatingsBreakdown.py ml-100k/u.data
```

Run it on a Hadoop cluster via Hadoop Streaming:

```bash
python RatingsBreakdown.py -r hadoop --hadoop-streaming-jar /path/to/hadoop-streaming.jar ml-100k/u.data
```

### 2. `test_hbase.py` — Loading data into HBase

Loads the MovieLens ratings into an **HBase** table through the HBase REST (Stargate) service using
the [starbase](https://pypi.org/project/starbase/) client. It creates a `ratings` table and batch-
writes each user's movie ratings.

```bash
python test_hbase.py
```

> Note: this script expects an HBase REST gateway to be reachable and the path to `u.data` to be set
> for your environment.

## Dataset

The `ml-100k/` directory contains the MovieLens 100k dataset (100,000 ratings from 943 users on
1,682 movies). See `ml-100k/README` for the original dataset documentation and column formats.

## Requirements

```bash
pip install mrjob starbase
```

Plus a Hadoop and/or HBase environment for the distributed examples.
