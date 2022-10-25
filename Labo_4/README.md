# Labo 4

## Opdracht 1

De script kijkt na of het een django website is of niet. Als er een csrfmiddlewaretoken wordt gevonden of als de title Django bevat dan is het een django website.

### Usage

python .\opdracht_1.py scheme + domain  
Voorbeeld: python .\opdracht_1.py https://realpython.com

## Opdracht 2

De script gaat filmreviews bruteforcen. Ik had wel "django.middleware.csrf.CsrfViewMiddleware" in de filmreviews settings moeten uitzetten, want anders ging het niet werken. Ik heb al account aangemaakt: username = arash en password = test

### Usage

1) Eerst de filmreviews opstarten met: python .\manage.py runserver
2) python .\opdracht_2.py

## Optionele opdracht

Alle gevonden paths worden opgeslagen in een output.txt file.

### Usage

1) Eerst de filmreviews opstarten met: python .\manage.py runserver
2) python .\optionele_opdracht.py

## Hoe moet je een django app beveiligen en is er een manier om te checken of het beveiligd is?

Je kan de volgende zaken toevoegen op je app te beveiligen:

- Add "djangosecure" to your INSTALLED_APPS setting.

- Add "djangosecure.middleware.SecurityMiddleware" to your MIDDLEWARE_CLASSES setting (where depends on your other middlewares, but near the beginning of the list is probably a good choice).

- Set the SECURE_SSL_REDIRECT setting to True if all non-SSL requests should be permanently redirected to SSL.

- Set the SECURE_HSTS_SECONDS setting to an integer number of seconds and SECURE_HSTS_INCLUDE_SUBDOMAINS to True, if you want to use HTTP Strict Transport Security.

- Set the SECURE_FRAME_DENY setting to True, if you want to prevent framing of your pages and protect them from clickjacking.

- Set the SECURE_CONTENT_TYPE_NOSNIFF setting to True, if you want to prevent the browser from guessing asset content types.

- Set the SECURE_BROWSER_XSS_FILTER setting to True, if you want to enable the browser’s XSS filtering protections.

- Set SESSION_COOKIE_SECURE and SESSION_COOKIE_HTTPONLY to True if you are using django.contrib.sessions. These settings are not part of django-secure, but they should be used if running a secure site, and the checksecure management command will check their values.

- Ensure that you’re using a long, random and unique SECRET_KEY.

Met deze link https://observatory.mozilla.org/ en deze commando "python manage.py check --deploy" kan je checken of je app goed beveiligd is.