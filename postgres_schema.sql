CREATE TABLE Towns (
 id SERIAL UNIQUE NOT NULL,
 code VARCHAR(10) NOT NULL, -- not unique
 article TEXT,
 name TEXT NOT NULL, -- not unique
 department VARCHAR(4) NOT NULL,
 UNIQUE (code, department)
);
