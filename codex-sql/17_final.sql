

CREATE TABLE bdays (
  number INTEGER,
  name TEXT,
  birthday DATE,
  location TEXT,
  note TEXT,
  wishlist TEXT
);

SELECT *
FROM bdays;

INSERT INTO bdays (number, name, birthday, location, note, wishlist)
VALUES (1, 'Dasha', '1999-12-23', 'Khachapuri i vino', 'total black dress code', 'coffee machine');

INSERT INTO bdays (number, name, birthday, location, note, wishlist)
VALUES (2, 'Olesya', '1999-05-31', 'Zima', 'does not like roses', 'socks');

SELECT *
FROM bdays;