CREATE TABLE IF NOT EXISTS status (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    description VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS user_type (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255),
    city VARCHAR(255),
    state VARCHAR(255),
    user_type INTEGER REFERENCES user_type(id),
    password VARCHAR(255),
    access_token VARCHAR(1024)
);

CREATE TABLE IF NOT EXISTS services (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS user_services (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    service_id INTEGER REFERENCES services(id)
);

CREATE TABLE IF NOT EXISTS service_order (
    id SERIAL PRIMARY KEY,
    service_client INTEGER REFERENCES users(id),
    service_provider INTEGER REFERENCES users(id),
    service INTEGER REFERENCES services(id),
    status INTEGER REFERENCES status(id),
    solicitation_date TIMESTAMP,
    service_conclusion_date TIMESTAMP,
    service_rating INTEGER,
    service_comment VARCHAR(255),
    value FLOAT
);
