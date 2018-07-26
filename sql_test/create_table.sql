CREATE TABLE apps (
pk int,
id varchar(256),
title varchar(256),
rating float,
last_update_date date);

INSERT INTO apps (pk, id, title, rating, last_update_date) VALUES
    (1, 'com.facebook.katana', 'Facebook', 4.0, date('2016-09-12')),
	(2, 'com.whatsapp', 'WhatsApp', 4.5, date('2016-09-11')),
    (3, 'com.whatsapp', 'WhatsApp', 4.4, date('2016-09-12')),
    (4, 'com.nianticlabs.pokemongo', 'Pokémon GO', 4.6, date('2016-09-05')),
    (5, 'com.nianticlabs.pokemongo', 'Pokémon GO', 4.3, date('2016-09-06')),
    (6, 'com.nianticlabs.pokemongo', 'Pokémon GO', 4.1, date('2016-09-07'));