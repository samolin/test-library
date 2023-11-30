# Library

Library is an application for renting books. 

## Installation

```bash
git clone https://github.com/samolin/test-library
cd test-library
```
After you download the repository you need to rename example.env to .env add your email for smtp server and change DJANGO settings and MYSQL settings to provide security. 

## Start container

```bash
make up
```
After start migrations will be executed automatically. 

## Stop container

```bash
make down
```

## Usage

Collect migrations

```python
make makemigrations
```

Migrate manually

```python
make migrate
```

Createsuperuser
```python
make createuser
```

## License

[MIT](https://choosealicense.com/licenses/mit/)