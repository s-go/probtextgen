# meteoblue

* four regions, with a total of 2088 scenarios
	* Baden-Württemberg ('DE-BW': 475)
	* Bayern ('DE-BY': 865)
	* Rheinland-Pfalz ('DE-RL': 278)
	* Thüringen ('DE-TH': 470)
* data fields
	1) Temperature  =  Temperature (°C) [2 m above gnd]
	2) Wind direction = Wind direction (°) [10 m above gnd]
	3) Cloudiness = Total cloud cover (%) [sfc]
	4) Snowfall = Snowfall amount (cm) [sfc]
	5) Wind gust = Wind Gust (m/s) [sfc]
	6) Precipitation = Total Precipitation (mm) [sfc]

## Data structure

Schema:

```
`weather_reports` (
  `id` int(11) NOT NULL,
  `title` varchar(80) NOT NULL,
  `text` text NOT NULL,
  `lang` char(2) NOT NULL DEFAULT 'de',
  `iso2` char(8) NOT NULL DEFAULT 'ch',
  `customer` int(15) DEFAULT NULL,
  `valid_date` date NOT NULL,
  `deleted` tinyint(1) NOT NULL DEFAULT '0',
  `active` tinyint(1) NOT NULL DEFAULT '1',
  `created_at` datetime NOT NULL,
  `modified_at` datetime NOT NULL,
  `creator_id` int(11) NOT NULL
```

## Text structure

```
SO: Nachtfrost, meist bewölkt, bis 7°C, Ostwind.

An der Ostflanke einer Hochdruckbrücke über Miitteleuropa fliesst weiter kühlere Luft heran. Der Hochdruckeinfluss hält voraussichtlich bis Donnerstag an.

In der Nacht zum Sonntag nimmt der Wind aus östlichen Richtungen zu, und wird dabei böiger, die Hochnebelfelder verdichten sich und die Temperaturen sinken bis 0°C  in den Ebenen, und -2°C am Alpenrand.
Der Sonntag beginnt von Westen her sonnig, die Hochnebelfelder lösen sich auch teils im Osten und die Temperaturen steigen bis 7°C in den Ebenen und Null Grad auf 1200 Metern Höhe bei zeitweise starkem, böigem Wind aus östlichen Richtungen.
Nachts lässt der Wind etwas nach, und es gibt verbreitet leichten Frost.
Am Montag frischt der Ostwind wieder auf bei Temperaturen bis  maximal 5°C und auflockernder Bewölkung, teils mit Sonne.
Am Dienstag frischt der Ostwind weiter auf und die Temperaturen erreichen bis 7°C in Franken, und 3°C in Niederbayern und am Alpenrand.
Am Mittwoch sind Sonne, höhere Temperaturen bis 10°C und abnehmender Wind aus Süd möglich.
```

## Challenges

* Data for 4-9 weather stations per region
* Regional geolocations:
	> die Temperaturen liegen bei 12°C im Südschwarzwald und 7°C auf der Alb

## Pre-processing

- [x] Extract texts that are covered by data.
- [x] Clean up data (see below).
- [x] Extract text segments that are covered by data (first day of forecast).
	* Determine day of the week
	* If another day of the week appears within the first five tokens of a paragraph, remove this and all subsequent paragraphs (5: "Der Sonntag", "Am Sonntag", "In der Nacht zum Sonntag")

### Data cleanup

- [x] Remove texts starting with "Test"
- [x] Remove heading from `text` ("Vorhersage für Rheinland-Pfalz, Dienstag, 15.12.2015")
- [x] Remove long-term overview (separated by blank lines)