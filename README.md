# Flask Elasticsearch

An implementation of full text search for users to find information on a site using natural language.

## About Elasticsearch

[Elasticsearch](https://www.elastic.co/guide/en/elasticsearch/reference/current/install-elasticsearch.html) is an open-source full-text search engine.

## Getting Started

I've implemented all the text indexing and searching functions in a way that is very easy for you to switch to another engine. This will allow you to replace my implementation with any alternative search engines: [Apache Solr](http://lucene.apache.org/solr/), [Whoosh](http://whoosh.readthedocs.io/), [Xapian](https://xapian.org/), [Sphinx](http://sphinxsearch.com/)

### Prerequisites
- Elasticsearch

- Python 3.8.10 or higher

### Installing Elasticsearch
The documentation for Elasticsearch has an [Installation](https://www.elastic.co/guide/en/elasticsearch/reference/current/install-elasticsearch.html) page with detailed information on how to install it.

To verify that you've installed Elasticsearch on your computer run `http:localhost:9200` on your browser. This should return some basic information abou the service in JSON format.

### Project setup

```
# clone the repo
$ git clone https://github.com/AMuriuki/flask-elasticsearch.git

# enter the project directory
$ cd flask-elasticsearch
```

### Create & activate virtual environment

```
# included on all recent Python version
$ python3 -m venv venv

# activating the virtual env
$ . venv/bin/activate

# if using Microsoft Windows CMD
$ venv\Scripts\activate
```

### Initialize database

```
# migrate files to db
$ flask db upgrade
```
