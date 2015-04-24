# pytmdb2mysql
A simple library for obtaining data (and images) from TMDb API v3 and insert into a MySQL database.

![Picture](http://www.garpa.net/github/pytmdb2mysql.png)

Instructions to create the mysql tables:
**my_movies_db.sql**:
<pre>
CREATE TABLE IF NOT EXISTS `my_movies_db` (
  `pelis_id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `title` varchar(50) NOT NULL,
  `genre` varchar(50) DEFAULT NULL,
  `year` float(4,0) DEFAULT NULL,
  `color` varchar(10) DEFAULT NULL,
  `ref_cd` int(10) unsigned DEFAULT NULL,
  `country` varchar(50) DEFAULT NULL,
  `director` varchar(50) DEFAULT NULL,
  `stars` varchar(255) DEFAULT NULL,
  `comments` varchar(50) DEFAULT NULL,
  `tmdb_id` int(10) unsigned DEFAULT NULL,
  `original` enum('Y','N') NOT NULL,
  `owner` enum('C','P','O') DEFAULT NULL,
  `given` enum('Y','N') NOT NULL,
  `given_to` varchar(10) DEFAULT NULL,
  `quality` float(2,1) DEFAULT NULL,
  `viewed` enum('Y','N') NOT NULL,
  PRIMARY KEY (`pelis_id`),
  FULLTEXT KEY `buscador` (`title`,`comments`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8;
</pre>

**my_tmdb_info.sql**
<pre>
CREATE TABLE IF NOT EXISTS `my_tmdb_info` (
  `id_test` int(10) NOT NULL,
  `img` text NOT NULL,
  `banner` text NOT NULL,
  `title` text NOT NULL,
  PRIMARY KEY (`id_test`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
</pre>
